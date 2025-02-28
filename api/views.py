from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product
from .serializers import ProductSerializer

# Create your views here.

@api_view(["GET"])
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view(["GET"])
def daargaanwe(request):
    return Response({"message": "dit is de tweede"})


@api_view(["GET"])
def metpathvar(request, mijntext):
    print(mijntext) # print naar de console
    return Response({"message": "dit is de derde: "+str(mijntext)})



@api_view(["GET"])
def get_all_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

    
