from django.db import models

# Create your models here.
class mywatchlistItem(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.TextField()


    # class mywatchlistItem(models.Model):
    # item_name = models.CharField(max_length=255)
    # item_price = models.BigIntegerField()
    # item_stock = models.IntegerField()
    # description = models.TextField()
    # rating = models.IntegerField()
    # item_url = models.URLField()