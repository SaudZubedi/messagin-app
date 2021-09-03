from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    message = models.CharField(max_length=225)
    description = models.TextField(max_length=5000, null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{str(self.id)}, {str(self.message)}"

    class Meta:
        ordering = ['-published_date']