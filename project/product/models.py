from django.db import models


class Product(models.Model):
    product = models.CharField(max_length=300, unique=True)
    quantity = models.IntegerField("estoque atual")

    class Meta:
        ordering = ("product",)

    def __str__(self):
        return self.product

