from django.contrib import admin
from django.urls import path
from posts.views import post_list  # Corrected import
from django.http import HttpResponse

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet, post_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list, name='post_list'),
]


router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', post_list, name='post_list'),
    path('api/', include(router.urls)),
]
