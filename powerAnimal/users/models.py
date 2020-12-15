from django.db import models
from penguin.models import Product
from django.contrib.auth.models import User


# Create your models here.


class Library(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_items = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.user.username} lib"
