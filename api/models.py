from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=250, unique=True)
    content = RichTextField()
    created_at = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
