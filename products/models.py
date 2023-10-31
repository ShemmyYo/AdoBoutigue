from django.db import models



class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    cat_desc = models.CharField(max_length=254, null=True, blank=True)
    cat_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Condition(models.Model):

    class Meta:
        verbose_name_plural = 'Condition'

    name = models.CharField(max_length=254)
    condition_desc = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class AgeGroup(models.Model):

    class Meta:
        verbose_name_plural = 'Age Group'

    name = models.CharField(max_length=6)
    restriction_name = models.CharField(max_length=54, null=True, blank=True)
    restriction_desc = models.CharField(max_length=254, null=True, blank=True)
    restriction_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    age = models.ForeignKey(
        'AgeGroup', null=True, blank=True, on_delete=models.SET_NULL, default=3)
    min_players = models.CharField(max_length=1, null=False, blank=False, default=1)
    max_players = models.CharField(max_length=2, null=False, blank=False)
    game_play_time = models.CharField(max_length=3, null=False, blank=False)
    condition = models.ForeignKey(
        'Condition', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    stock = models.IntegerField(default=1)

    def __str__(self):
        return self.name
