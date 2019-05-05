from django.contrib import admin

from .models import Image, Comment, User

admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(User)
