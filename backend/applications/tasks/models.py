
from django.db import models
from django.contrib.auth.models import User
from applications.utils.custom_managers import ApplicationsManager

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)
    
    objects = ApplicationsManager()
    
    def __str__(self):
        return self.title