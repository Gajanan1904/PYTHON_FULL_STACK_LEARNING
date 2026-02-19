from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer


# LIST + CREATE
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def student_list(request):

    # GET → fetch all students
    if request.method == 'GET':

        ordering = request.query_params.get('ordering')
        search = request.query_params.get('search')

        students = Student.objects.all()

        age = request.query_params.get('age')
        name = request.query_params.get('name')

        if age:
            students = students.filter(age=age)

        if name:
            students = students.filter(name__icontains=name)

        # (you created search but never used → fixed)
        if search:
            students = students.filter(name__icontains=search)

        if ordering:
            students = students.order_by(ordering)

        paginator = PageNumberPagination()
        paginator.page_size = 2

        paginated_students = paginator.paginate_queryset(students, request)
        serializer = StudentSerializer(paginated_students, many=True)

        return paginator.get_paginated_response(serializer.data)


    # POST → create new student
    if request.method == 'POST':

        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# DETAIL API (single student)
@api_view(['GET','PUT','DELETE','PATCH'])
@permission_classes([IsAuthenticated])
def student_detail(request, id):

    try:
        student = Student.objects.get(id=id)   # renamed (single object)
    except Student.DoesNotExist:
        return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    # GET → fetch one student
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    # PUT → full update
    if request.method == 'PUT':

        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH → partial update
    if request.method == 'PATCH':

        serializer = StudentSerializer(student, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE → remove student
    if request.method == 'DELETE':
        student.delete()
        return Response({'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
