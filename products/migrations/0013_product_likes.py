# Generated by Django 3.2.21 on 2023-11-05 09:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0012_alter_product_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='product_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
