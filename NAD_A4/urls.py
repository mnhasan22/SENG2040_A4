from django.contrib import admin
from django.urls import path
from posts.views import post_list  # Corrected import
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list, name='post_list'),
]