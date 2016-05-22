from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length = 50)
    book_content = models.CharField(max_length = 255)
    book_image = models.ImageField(upload_to='books/image',null=True)
    book_image_R = models.PositiveIntegerField(default = 0)
    book_image_G = models.PositiveIntegerField(default = 0)
    book_image_B = models.PositiveIntegerField(default = 0)
    
    
#class Chapter(models.Model):
#    chapter_content = models.CharField(max_length = 500)