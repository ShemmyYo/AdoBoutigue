from django.contrib import admin
from .models import Product, Category, Condition, AgeGroup, SpecialCategory

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Condition)
admin.site.register(AgeGroup)
admin.site.register(SpecialCategory)
