from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from .models import User
from .serializers import UserSerializer


class RegisterUserView(APIView):
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def post(self, request):
        # Check if the email is already in use
        if User.objects.filter(email=request.data['email']).exists():
            return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)

        # Instantiate the serializer with the request data
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            # Save the valid data and create the user
            user = serializer.save()
            user.set_password(request.data['password'])  # Hash the password
            user.save()  # Save the user with the hashed password

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Return the errors if the data is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
class UserView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get(self, request):
        serializer = UserSerializer(request.user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # update user profile image
    def put(self, request):
        user = User.objects.get(email=request.user.email)
        user.username = request.data['username']
        user.save()
        return Response({'message': 'Image updated'}, status=status.HTTP_200_OK)

class AllUsersView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)