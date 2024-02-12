from django.db import models
"""
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Ensure unique category names
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name  # Provide a meaningful string representation
"""
class Item(models.Model):

    #category = models.ForeignKey(
    #    'api.Category', on_delete=models.PROTECT, related_name='items')
    category = models.CharField(max_length=255)
    sku = models.CharField(max_length=255, unique=True,null=False)  # Ensure unique SKU
    name = models.CharField(max_length=255)
    inStock = models.PositiveBigIntegerField()  # Enforce non-null
    availableStock = models.PositiveBigIntegerField()  # Enforce non-null
    tag1 = models.BooleanField(null=False,default=False)  # Enforce non-null
    tag2 = models.BooleanField(null=False,default=False)  # Enforce non-null
    tag3 = models.BooleanField(null=False,default=False)  # Enforce non-null
    tag4 = models.BooleanField(null=False,default=False)  # Enforce non-null
    tag5 = models.BooleanField(null=False,default=False)  # Enforce non-null
    id = models.AutoField(primary_key=True)  # Use Django's automatic ID field

    def __str__(self) -> str:
        return self.name
