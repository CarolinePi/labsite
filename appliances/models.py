from django.db import models


# Create your models here.
class TvModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='photo_tv')
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class FridgeModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='photo_fridge')
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
