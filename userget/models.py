from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name



class Article(models.Model):

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title