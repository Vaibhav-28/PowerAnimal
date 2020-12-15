from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    pub_date = models.DateField()
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="penguin/images", default="")

    def __str__(self):
        return self.product_name
