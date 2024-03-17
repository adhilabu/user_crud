from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    profile_picture = models.TextField()
    
    def __str__(self):
        return self.name
