from django.shortcuts import render

# Create your views here.
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Item
from .serializers import ItemSerializer, UserSerializer




@api_view(['POST'])# Decorator 'api_view' defines the allowed HTTP methods; here, only POST is allowed
@authentication_classes([SessionAuthentication, TokenAuthentication])# 'authentication_classes' specifies the ways a user can be authenticated; this view allows, Session-based or Token-based authentication
@permission_classes([IsAuthenticated]) # 'permission_classes' defines the permissions required; 'IsAuthenticated' means the user must be logged in
def add_items(request):
    item_serializer = ItemSerializer(data=request.data)
    if 'sku' in request.data and Item.objects.filter(sku=request.data['sku']).exists():
        raise serializers.ValidationError('This data already exists')

    if item_serializer.is_valid():
        item_serializer.save()
        return Response(item_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
z
@api_view(['POST']) # No authentication or permission decorators here, means this view is accessible without authentication
def login(request): # This view handles user login and is accessible to any user without prior authentication
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"details": "Not Found"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})


@api_view(['POST']) # This is another view accessible without authentication, meant for users to create an account
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])  # This GET endpoint requires the user to be authenticated to test the validity of their token
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response({"passed for {}".format(request.user.email)})



@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_all_items(request):   # Users must be authenticated to access this view that returns all items in the database
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])  # Similar to 'get_all_items', but allows filtering items based on query parameters
# Authentication and permissions are required as above
@permission_classes([IsAuthenticated])
def get_all_itemsbyParameters(request):
    # Retrieve query parameters from the request
    sku = request.query_params.get('sku')
    name = request.query_params.get('name')
    category = request.query_params.get('category')

    # Add more parameters as needed

    # Construct a filter dictionary based on provided parameters
    filters = {}
    if sku:
        filters['sku__icontains'] = sku
    if name:
        filters['name__icontains'] = name
    if category:
        filters['category__icontains'] = category
    # Add more filters based on additional parameters

    # Apply filters to the queryset
    items = Item.objects.filter(**filters)

    # Serialize the filtered queryset
    serializer = ItemSerializer(items, many=True)

    # Return the serialized data in the response
    return Response(serializer.data, status=status.HTTP_200_OK)



