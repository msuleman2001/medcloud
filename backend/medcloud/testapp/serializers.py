from rest_framework import serializers
from testapp.models import Product


class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model=Product
    fields=['name','description','price','stock_quantity']
  
