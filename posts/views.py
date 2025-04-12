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

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def service_booking_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        service = request.POST.get("service")
        date = request.POST.get("date")
        print(f"New Appointment: {name} | {email} | {service} | {date}")
        return render(request, 'posts/confirmation.html', {'name': name, 'service': service})

    return render(request, 'posts/services.html')


from .models import Post, Comment
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def forum_view(request):
    if request.method == "POST":
        # New post submission
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title and content:
            Post.objects.create(title=title, content=content)
    posts = Post.objects.all().order_by("-created_at")
    return render(request, 'posts/forum.html', {"posts": posts})

@csrf_exempt
def add_comment(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(pk=post_id)
        author = request.POST.get("author")
        text = request.POST.get("text")
        if author and text:
            Comment.objects.create(post=post, author=author, text=text)
    return redirect('forum')

@csrf_exempt
def like_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.likes += 1
    post.save()
    return redirect('forum')

@csrf_exempt
def dislike_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.dislikes += 1
    post.save()
    return redirect('forum')

def contact_view(request):
    return render(request, 'posts/contact.html')

def media_gallery_view(request):
    return render(request, 'posts/media.html')

