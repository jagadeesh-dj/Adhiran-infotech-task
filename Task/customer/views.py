from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerSerializer,ProductSerializer,OrderSerializer
from .models import Customer,Category,Products,Order
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST'])
def Customer_list(request):
    if request.method=='GET':
        result=Customer.objects.all()
        serializer=CustomerSerializer(result,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method=='POST':
        serializer=CustomerSerializer(result,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Customers(request,pk):
    try:
        user=Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = CustomerSerializer(user)
        return Response(serializer.data)
   
    elif request.method=='PUT':
        serializer=CustomerSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','POST'])
def Product_view(request):
    if request.method=='GET':
        result=Products.objects.all()
        serializer=ProductSerializer(result,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method=='POST':
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Product(request,pk):
    try:
        user=Products.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = ProductSerializer(user)
        return Response(serializer.data)
   
    elif request.method=='PUT':
        serializer=ProductSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','POST'])
def Order_view(request):
    if request.method=='GET':
        result=Order.objects.all()
        serializer=OrderSerializer(result,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method=='POST':
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Orders(request,pk):
    try:
        user=Order.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = OrderSerializer(user)
        return Response(serializer.data)
   
    elif request.method=='PUT':
        serializer=OrderSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)