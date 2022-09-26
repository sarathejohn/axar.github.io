from django.db import models
from django.core.validators import validate_image_file_extension

# Create your models here.
class image(models.Model):
    image=models.ImageField(null = True,blank = True,upload_to='gallery_image',default='Null',validators=[validate_image_file_extension])
    created_at = models.DateTimeField(auto_now_add=True)
    