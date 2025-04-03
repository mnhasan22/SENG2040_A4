from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet, appointment_form

router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', appointment_form, name='appointment_form'),
    path('api/', include(router.urls)),
]
