from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet, appointment_form
from .views import AppointmentViewSet, appointment_form, service_booking_view
from .views import forum_view, add_comment, like_post, dislike_post
from .views import contact_view
from .views import media_gallery_view


router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', appointment_form, name='appointment_form'),
    path('api/', include(router.urls)),
    path('services/', service_booking_view, name='service_booking'),
        path('forum/', forum_view, name='forum'),
    path('forum/comment/<int:post_id>/', add_comment, name='add_comment'),
    path('forum/like/<int:post_id>/', like_post, name='like_post'),
    path('forum/dislike/<int:post_id>/', dislike_post, name='dislike_post'),
    path('contact/', contact_view, name='contact'),
    path('gallery/', media_gallery_view, name='media_gallery'),
]
