from django.db import models

# Create your models here.



class Skills(models.Model):
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)

    name = models.CharField(max_length=20)

    description = models.TextField(max_length=20)