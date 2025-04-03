from django.contrib import admin
# from django.urls import path
# # from posts.views import post_list  # Corrected import
# from django.http import HttpResponse

from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from posts.views import AppointmentViewSet, appointment_form

from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', post_list, name='post_list'),
# ]

# router = DefaultRouter()
# router.register(r'appointments', AppointmentViewSet)

# # urlpatterns = [
# #     path('', appointment_form, name='appointment_form'),
# #     path('api/', include(router.urls)),
# # ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

