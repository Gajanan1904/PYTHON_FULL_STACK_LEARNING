#import serializer tool
from rest_framework import serializers
#importimg product.model
from .models import Product
#Creating serializer for product model/class/table
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product     #tells serializer which model to convert
        fields='__all__'    #includes all model/class/table fields
        

