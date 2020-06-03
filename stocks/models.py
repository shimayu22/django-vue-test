from django.db import models


class Stock(models.Model):
    class Meta:
        db_table = 'stock'

    title = models.TextField()
    stock_count = models.IntegerField()
