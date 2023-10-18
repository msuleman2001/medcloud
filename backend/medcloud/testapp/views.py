from django.shortcuts import render
from rest_framework import generics
from testapp.models import Product
from  rest_framework.response import Response
from testapp.serializers import ProductSerializer
# from django.http import Http404
from django.shortcuts import get_object_or_404
from  rest_framework.decorators import api_view
# Create your views here.


class ProductListView(generics.ListAPIView):
  queryset=Product.objects.all()
  serializer_class=ProductSerializer