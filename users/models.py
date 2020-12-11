from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile_pic', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} profile'
   
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)    
        img = Image.open(self.image.path)
        output_size = (400, 400)
        img.thumbnail(output_size)     
        img.save(self.image.path)    
