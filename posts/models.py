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