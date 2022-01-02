from django.db import models


# Create your models here.
class Links(models.Model):
    the_url = models.URLField()
