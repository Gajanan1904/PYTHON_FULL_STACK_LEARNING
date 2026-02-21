from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Tickets
from rest_framework.permissions import IsAuthenticated
from .serializers import TicketSerializer
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def ticket_list(request):
    if request.method == 'GET':
        tickets=Tickets.objects.all()
        ordering=request.query_params.get('ordering')
        search=request.query_params.get('search')
        title=request.query_params.get('title')
        description=request.query_params.get('description')
        category=request.query_params.get('category')
        priority=request.query_params.get('priority')
        
        if ordering:
            tickets=tickets.order_by(ordering)
        if title:
            tickets=tickets.filter(title__icontains=title)
        if description:
            tickets=tickets.filter(description__icontains=description)
        if category:
            tickets=tickets.filter(category__icontains=category)
        if priority:
            tickets=tickets.filter(priority__icontains=priority)
        
        
        paginator=PageNumberPagination()
        paginator.page_size=2
        paginated_tickets=paginator.paginate_queryset(tickets,request)
        serializer=TicketSerializer(paginated_tickets,many=True)
        return paginator.get_paginated_response(serializer.data)
    
    if request.method == 'POST':
        serializer=TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=201)
    return Response(serializer.errors,status=400)

@api_view(['GET','PUT','DELETE','PATCH'])
@permission_classes([IsAuthenticated])
def ticket_detail(request,id):
    try:
        tickets=Tickets.objects.get(id=id)
    except Tickets.DoesNotExist:
        return Response({'error':'Not found'},status=404)
    if request.method =='GET':
        serializer=TicketSerializer(tickets)
        return Response(serializer.data)
    if request.method =='PUT':
        serializer=TicketSerializer(tickets,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors,status=400)

    if request.method =='PATCH':
        serializer=TicketSerializer(tickets,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

    if request.method =='DELETE':
        tickets.delete()
        return Response({'message':'deleted successfully'},status=204)
    


    
    

    


    
    
        
        
    


