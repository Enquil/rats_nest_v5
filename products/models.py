from django.db import models
from cloudinary.models import CloudinaryField


class Domain(models.Model):

    class Meta:
        verbose_name_plural = 'Domains'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    domain = models.ForeignKey('Domain', null=True, blank=True,
                               on_delete=models.SET_NULL)
    parent = models.ForeignKey('self',
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL)
    is_parent = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def save(self, *args, **kwargs):

        if not self.domain:
            if self.parent:
                self.domain = self.parent.domain

        return super().save(*args, **kwargs)


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


class Product(models.Model):

    domain = models.ForeignKey('Domain', null=True, blank=True,
                               on_delete=models.SET_NULL)
    category = models.ForeignKey('Category', null=True,
                                 on_delete=models.SET_NULL)
    brand = models.ForeignKey('Brand', null=True,
                              on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    color = models.ForeignKey('Color', null=True, blank=True,
                              on_delete=models.SET_NULL)
    description = models.TextField()
    feature_list = models.CharField(max_length=254, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True,)
    default_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    # Images
    image = CloudinaryField('image', default='placeholder')
    image2 = CloudinaryField('image', default='placeholder')
    image3 = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        domain = self.domain
        category = self.category

        if not self.price:
            self.price = self.default_price

        if not domain:

            if category.is_parent:
                self.domain = category.domain
            elif category.parent.domain:
                self.domain = category.parent.domain

        return super().save(*args, **kwargs)
