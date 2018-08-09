from django.contrib import admin
from .models import Category, Product, Image

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)



class ProductImageInline(admin.TabularInline):
    model = Image
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ ProductImageInline, ]
   


admin.site.register(Product, ProductAdmin)
admin.site.register(Image)   