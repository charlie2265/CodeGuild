from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    first_name = models.CharField(max_length=30)

   
    
    
class Book(models.Model):
    title = models.CharField(max_length= 128)
    published = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)



    # author = models.ForeignKey(on_delete=models.CASCADE)

