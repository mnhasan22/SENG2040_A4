from django.contrib import admin
from .models import Post, Comment
from .models import Appointment


# Register your models here.


admin.site.register(Post)
admin.site.register(Appointment)
from django.contrib import admin

admin.site.register(Comment)

