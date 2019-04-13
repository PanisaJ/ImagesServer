from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse

from rest_framework import generics

from .serializers import ImageSerializer,CommentSerializer

from .models import Image, Comment


class ImageUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        image_serializer = ImageSerializer(data=request.data)

        if image_serializer.is_valid():
            image_serializer.save()
            return Response(image_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentUploadView(APIView):

    def post(self, request, *args, **kwargs):

        comment_serializer = CommentSerializer(data=request.data)

        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageViewSet(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class CommentViewSet(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    

    

