# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse

# def post_list(request):
#     return HttpResponse("Hello, this is the post list view.")


# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Post
# from .serializers import PostSerializer

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# def post_list(request):
#     return render(request, 'posts/index.html')

from rest_framework import viewsets, parsers, permissions
from django.shortcuts import render
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('-preferred_date')
    serializer_class = AppointmentSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    permission_classes = [permissions.AllowAny] 

def appointment_form(request):
    return render(request, 'posts/index.html')

