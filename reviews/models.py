from django.db import models
from products.models import Product
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Review(models.Model):
    reviewer = models.ForeignKey('auth.User', blank=False, related_name="reviews_written", on_delete=models.PROTECT)   
    product = models.ForeignKey(Product, blank=False, related_name="reviews_received", on_delete=models.PROTECT)
    title = models.CharField(max_length=250, blank=True, null=True)
    content = models.TextField()
    rating = models.IntegerField(blank=False, default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    date = models.DateTimeField(auto_now_add=True, null=True)
    
    @property
    def stars(self):
        return range(0,self.rating)
    
    def __str__(self):
        return self.content

