from django.db import models
from django.db.models import Avg
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True, default='')
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    
    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('products:product_list_by_category', args=[self.slug])



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=254, db_index=True, default='')
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    brand = models.CharField(max_length=50, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('products:product_detail', args=[self.id, self.slug])
   