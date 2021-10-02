from datetime import datetime
from django.db import models

# Create your models here.
class Caruosel(models.Model):
    
   title = models.CharField(max_length=50)
   short_discription = models.TextField()

   image = models.ImageField(upload_to='carousel/')
   creations = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.title   