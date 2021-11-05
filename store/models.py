from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from category.models import Category
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(null=True,blank=True)
    description = models.TextField(max_length=500,blank=True,null=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='products/')
    stocks = models.IntegerField()
    is_avaliable = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('store:product_detail',args=[self.category.slug,self.slug])

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        super(Product, self).save(*args,**kwargs)
    


    def __str__(self):
        return self.product_name