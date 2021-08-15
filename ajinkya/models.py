from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail

# Create your models here.
class Quotes(models.Model):
    """docstring for Quotes."""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
        
    def __str__(self):
        return self.title
