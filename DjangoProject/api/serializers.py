from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Item


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

# ModelSerializer for Category model would go here - Commented out CategorySerializer
"""
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category', 'description')
"""
# Serializer for the Item model using ModelSerializer
# This is useful for converting model instances into JSON format and vice versa
class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        # Specifies the Item model to serialize
        model = Item
        # Lists the fields from the Item model to include in the serialized representation
        # The fields correspond to the database columns in the Item model
        fields = ['category', 'sku', 'name', 'inStock', 'availableStock', 'tag1', 'tag2', 'tag3', 'tag4', 'tag5']

