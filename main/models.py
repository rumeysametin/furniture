from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cat_imgs/")

    def __str__(self):
        return self.title
    
class Productcode(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Brand(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Color(models.Model):
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Material(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="product_imgs/")
    detail = models.TextField()
    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    cod =models.ForeignKey(Productcode, on_delete=models.CASCADE)
    brand =models.ForeignKey(Brand, on_delete=models.CASCADE)
    color =models.ForeignKey(Color, on_delete=models.CASCADE)
    material =models.ForeignKey(Material, on_delete=models.CASCADE)
    status =models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class ProductAttribute(models.Model):
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    color =models.ForeignKey(Color, on_delete=models.CASCADE)
    material =models.ForeignKey(Material, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.product.title