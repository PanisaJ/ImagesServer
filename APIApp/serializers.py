from rest_framework import serializers
from .models import Image, Comment, User

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('photo','caption')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment_text',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
