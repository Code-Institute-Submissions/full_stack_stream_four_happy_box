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

    @property
    def average_rating(self):
        if self.reviews_received.all():
            average = self.reviews_received.all().aggregate(Avg('rating'))
            n = average['rating__avg']
            return float(round(n, 2))
        else:
            return 0
        
    @property
    def stars(self):
        return range(int(self.average_rating))
        
    @property 
    def needs_half_star(self):
        remainder = self.average_rating - int(self.average_rating)
        return 0.4 < remainder


    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('products:product_detail', args=[self.id, self.slug])
   