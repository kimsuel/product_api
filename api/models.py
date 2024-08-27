import uuid

from django.db import models


class TimeStampedModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class Product(TimeStampedModel):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)


class ShoppingCart(TimeStampedModel):
    user_id = models.UUIDField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
