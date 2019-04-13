from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.ImageUploadView.as_view()),
    path('images/', views.ImageViewSet.as_view()),
    path('comment/', views.CommentUploadView.as_view()),
    path('getcomment/', views.CommentViewSet.as_view()),
    
]

