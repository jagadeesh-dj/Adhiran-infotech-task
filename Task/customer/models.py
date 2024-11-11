from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50,unique=True)
    address=models.TextField()
    phone_number=models.CharField(max_length=20,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name
    
class Products(models.Model):
    name=models.CharField(max_length=30,unique=True)
    price=models.IntegerField()
    stock=models.IntegerField()
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')

    def __str__(self):
        return self.name
    
class Order(models.Model):
    user_id=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="user_id")
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE,related_name='product_id')
    quantity=models.IntegerField()
    price=models.IntegerField(null=True,blank=True)

    def save(self, *args, **kwargs):
        self.price = self.product_id.price * self.quantity
        super().save(*args, **kwargs) 


    def __str__(self):
        return self.product_id.name
    
