from django.contrib import admin
from .models import Product, Category, Condition, AgeGroup

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Condition)
admin.site.register(AgeGroup)