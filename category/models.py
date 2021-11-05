from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(null=True,blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/',blank=True, null=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('store:product_store',args=[self.slug])
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super(Category, self).save(*args,**kwargs)
    


    def __str__(self):
        return self.category_name