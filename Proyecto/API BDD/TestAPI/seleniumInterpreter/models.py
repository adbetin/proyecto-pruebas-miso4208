from django.db import models

# Create your models here.
class Feature(models.Model):
    feature_name=models.CharField(max_length=250)
    user_story=models.CharField
