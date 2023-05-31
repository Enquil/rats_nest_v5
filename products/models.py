from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    parent = models.ForeignKey('self',
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):

    class Meta:
        verbose_name_plural = 'Brands'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Color(models.Model):

    class Meta:
        verbose_name_plural = 'Colors'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class ProductManager(models.Manager):

    def create_product(self, price, default_price):

        if not self.price:
            self.price = self.default_price
        return self


class Product(models.Model):

    domain = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey('Category', null=True,
                                 on_delete=models.SET_NULL)
    brand = models.ForeignKey('Brand', null=True,
                              on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    color = models.ForeignKey('Color', null=True, blank=True,
                              on_delete=models.SET_NULL)
    description = models.TextField()
    feature_list = models.CharField(max_length=254)
    has_sizes = models.BooleanField(default=False, null=True, blank=True,)
    default_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    # Images
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True,
                              blank=True)
    image_url2 = models.URLField(max_length=1024, null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image_url3 = models.URLField(max_length=1024, null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        color = str(self.color)
        name = self.name
        category = self.category

        if not self.price:
            self.price = self.default_price

        if not self.domain:
            self.domain = self.category.parent.pk

        if color is not None and color not in self.name:
            self.name = None
            self.name = name + ', ' + color

        return super().save(*args, **kwargs)
