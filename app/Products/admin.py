from django.contrib import admin
from .models import Category, Product
from django.contrib import admin
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ["category", ]
    list_display = ["Name", "category"]


admin.site.register(Category)
