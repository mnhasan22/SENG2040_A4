from django.db import models
# Create your models here.

class Appointment(models.Model):
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    email = models.EmailField()
    purpose = models.TextField()
    preferred_date = models.DateTimeField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Declined', 'Declined')],
        default='Pending'
    )

    def __str__(self):
        return f"{self.student_name} ({self.student_id}) - {self.preferred_date.strftime('%Y-%m-%d %H:%M')}"
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"