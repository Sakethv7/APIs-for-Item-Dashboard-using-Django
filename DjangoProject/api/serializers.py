from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Item


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


"""
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category', 'description')
"""
class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['category', 'sku', 'name', 'inStock', 'availableStock', 'tag1', 'tag2', 'tag3', 'tag4', 'tag5']

