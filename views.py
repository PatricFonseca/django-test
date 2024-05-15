from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from django_test.serializers.user_serializer import UserSerializer


# @api_view(['POST'])
# def login(req):
#     return Response()


User = get_user_model()  # Assuming default User model


# @api_view(['POST'])
# def signup(request):
#     try:
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(password=request.data['password'])
#             user = serializer.instance
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key, "user": serializer.data})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     except Exception as e:  # More specific exception handling later
#         return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def login(request):
    try:
        if not (request.data['username']):
            return Response({'error': 'Usuário não informado'})

        if not (request.data['password']):
            return Response({'error': 'Senha não informada'})

        user = User.objects.get(username=request.data['username'])
        if (not user.check_password(request.data['password'])):
            return Response({'message': 'Senha inválida'})

        serializer = UserSerializer(user)

        token, created = Token.objects.get_or_create(
            user=serializer.data['id'])
        return Response({'token': token.key, "user": serializer.data})
    except Exception as e:
        raise e
    # Implement login logic here (username/password check, token generation)
    # ...
    # return Response({'message': 'Login successful (placeholder)'})


@api_view(['POST'])
def signup(req):
    serializer = UserSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=req.data['username'])
        user.set_password(req.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def test(req):
    return Response({'message': 'funcionou'})

# @api_view(['PUT'])
# def login(req):
    # return Response()
