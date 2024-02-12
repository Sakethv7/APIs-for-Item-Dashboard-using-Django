# from django.shortcuts import render
#
# # Create your views here.
# from rest_framework import status, serializers
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404
# from rest_framework.decorators import authentication_classes,permission_classes
# from rest_framework.authentication import SessionAuthentication, TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from .models import Item
# from .serializers import ItemSerializer,CategorySerializer,UserSerializer
#
# @api_view(['POST'])
# def login(request):
#     user = get_object_or_404(User, username=request.data['username'])
#     if not user.check_password(request.data['password']):
#         return Response({"details": "Not Found"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
#     token, created = Token.objects.get_or_create(user=user)
#     serializer = UserSerializer(instance=user)
#     return Response({"token": token.key, "user": serializer.data})
#
#
# @api_view(['POST'])
# def signup(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         user = User.objects.get(username=request.data['username'])
#         user.set_password(request.data['password'])
#         user.save()
#         token = Token.objects.create(user=user)
#         return Response({"token": token.key, "user": serializer.data})
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET'])
# @authentication_classes([SessionAuthentication,TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def test_token(request):
#     return Response({"passed for {}".format(request.user.email)})
#
#
# @api_view(['GET'])
# @authentication_classes([SessionAuthentication,TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def dataget(request):
#
#     return Response("data is accessible")
#
#
# @api_view(['GET'])
# def ApiOverview(request):
#     api_urls = {
#         'all_items': '/',
#         'Add': '/create',
#         'login':'/login',
#         'sign up':'/signup',
#         'Test Token': '/test_token'
#     }
#
#     return Response(api_urls)
#
#
# @api_view(['POST'])
# def add_items(request):
#     item = ItemSerializer(data=request.data)
#
#     # validating for already existing data
#     if Item.objects.filter(**request.data).exists():
#         raise serializers.ValidationError('This data already exists')
#
#     if item.is_valid():
#         item.save()
#         return Response(item.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)


from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import Item
from .serializers import ItemSerializer, UserSerializer

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Check if username and password are provided
    if not username or not password:
        return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

    # Check if the user exists
    user = get_object_or_404(User, username=username)

    # Verify the password
    if not user.check_password(password):
        return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

    # Generate or retrieve the token for the user
    token, created = Token.objects.get_or_create(user=user)

    # Serialize the user data
    serializer = UserSerializer(instance=user)

    # Return token and user data
    return Response({"token": token.key, "user": serializer.data})

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response({"message": "Token is valid."})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def dataget(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Add': '/create',
        'login': '/login',
        'sign_up': '/signup',
        'Test Token': '/test_token'
    }
    return Response(api_urls)

@api_view(['POST'])
def add_items(request):
    item = ItemSerializer(data=request.data)

    # Validate for already existing data
    if Item.objects.filter(**request.data).exists():
        return Response({'error': 'This data already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    if item.is_valid():
        item.save()
        return Response(item.data, status=status.HTTP_201_CREATED)
    else:
        return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)
