from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse

from rest_framework import generics

from .serializers import ImageSerializer, CommentSerializer, UserSerializer

from .models import Image, Comment, User


class ImageUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        image_serializer = ImageSerializer(data=request.data)
        
        if image_serializer.is_valid():
            image_serializer.save(user = User.objects.get(pk=request.data['user']))
            return Response(image_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentUploadView(APIView):

    def post(self, request, *args, **kwargs):

        comment_serializer = CommentSerializer(data=request.data)

        if comment_serializer.is_valid():
            print("nnnnnnnnnnnnnnnnnnnnnnnnnnnn")
            print(Image.objects.get(pk=1).photo)
            comment_serializer.save(image = Image.objects.filter(photo__contains=request.data['image']))
            return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):

    def post(self, request, *args, **kwargs):

        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageViewSet(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class CommentViewSet(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UserViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

    

