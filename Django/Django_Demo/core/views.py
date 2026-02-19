# from django.shortcuts import render
# from django.http import HttpResponse #-->to send http response to browser
# from django.http import JsonResponse #--> used to send a Json response to the browser

# # Create your views here.
# def hello(request):
#     return HttpResponse("Hello Django...!")

# def name(request):
#     return JsonResponse({"name": "Hello Gajanan"})


from rest_framework.views import APIView
from rest_framework.response import Response

# Import Product model → used to fetch data from database
from .models import Product

# Import serializer → converts database data into JSON format
from .serializers import ProductSerializer

from django.shortcuts import render


# Create API class to handle requests
class ProductList(APIView):

    # This function runs when GET request is sent
    def get(self, request):

        # Get all product records from database table
        # "objects" is Django's default manager to access database
        products = Product.objects.all()

        # Convert database data into JSON format
        serializer = ProductSerializer(products, many=True)

        # Send JSON response to user
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
    


def add_product(request):
    return render(request, "add_product.html")

