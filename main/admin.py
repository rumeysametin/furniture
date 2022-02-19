from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Productcode)
admin.site.register(Color)
admin.site.register(Material)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "cod", "brand", "color", "material", "price", "status")
    list_editable = ("status",)
    
admin.site.register(Product, ProductAdmin)