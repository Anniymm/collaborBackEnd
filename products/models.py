from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True) # wakitxvadobistvis mara amas testing ar awyenda )))
    # description = models.TextField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=100) # "Color", "Size"
    value = models.CharField(max_length=100) # red, M
    
    def __str__(self):
        return f"{self.name}: {self.value}"


class Collection(models.Model):
    name = models.CharField(max_length=100, unique=True) # party and events, office looks....
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Featured(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, related_name='products')
    features = models.ManyToManyField(Feature, related_name='products') # many to many fieldebi minda rom ramdenime ertdroulad davamato
    featured = models.ManyToManyField(Featured, related_name='featured' )
    collections = models.ManyToManyField(Collection, related_name='products')
    image = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name