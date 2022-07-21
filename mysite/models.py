from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255,default="")

    def __str__(self):
        return self.title

class Tag(models.Model):
    tag = models.CharField(max_length=255, default='')
    slug = models.SlugField(blank=True, default="")

    def __str__(self):
        return self.tag

    def save(self, *args, **kwargs):
        self.slug = slugify(self.tag)
        super(Tag, self).save()

class Flowers(models.Model):
    name = models.CharField(max_length=255,default="")
    description = models.TextField(default="")
    slug = models.SlugField(blank=True, default="")
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    tag = models.ManyToManyField(Tag)



    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) 
        super(Flowers, self).save()
    
    def get_absolute_url(self):
        arg = [str(self.slug)]
        return reverse('detail',args=arg)

    