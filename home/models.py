from django.db import models

# Create your models here.



class Skills(models.Model):
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)

    name = models.CharField(max_length=20)

    description = models.TextField(max_length=20)



class Message(models.Model):

    # subject, and name inclusion?

    # SUBJECTS = {
    #     "FR": "Freshman",
    #     "SO": "Sophomore",
    #     "JR": "Junior",
    #     "SR": "Senior",
    #     "GR": "Graduate",
    # }

    email = models.EmailField(blank=False, null=True)

    # subject = models.CharField(max_length=28, choices=SUBJECTS, default='',)

    message = models.TextField(max_length=255)