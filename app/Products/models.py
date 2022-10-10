from django.db import models
import uuid
from django.db.models.fields.related import ForeignKey
# Create your models here.


class Category(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    conditional_text = models.CharField(max_length=50, null=True, blank=True)
    description_title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    pricing_table = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.Name


class Product(models.Model):
    category = ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True, related_name="product")
    Name = models.CharField(max_length=50, null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    short_des = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    pricing_table = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ('created',)
