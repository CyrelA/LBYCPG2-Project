from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Vtuber(models.Model):
    name = models.CharField(max_length=128)
    Ddate = models.DateField(null=True)
    slug = models.SlugField(max_length=128, unique=True, null=True)
    tags = TaggableManager()
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    content = models.TextField(null=True)
    infoo = models.TextField(null=True)

    def __str__(self):
        return self.name
