# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from products.models import Product
from .serializers import ProductSer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets

@api_view(["GET", "POST"])
def product_list(request):

    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSer(products, many=True)
        return Response(serializer.data)

    serializer = ProductSer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def product_detail(request, pk):

    product = Product.objects.get(pk=pk)

    if request.method == "GET":
        serializer = ProductSer(product)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ProductSer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class ProductList(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors)


class ProductDetail(APIView):

    def get_object(self, pk):
        return  get_object_or_404(Product, pk=pk) 
    def get(self, request, pk):
        serializer = ProductSer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk) 
        serializer = ProductSer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):
        get_object_or_404(Product, pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductListGen(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSer


class ProductDetailGen(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSer