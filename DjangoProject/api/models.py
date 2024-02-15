from django.db import models

class Item(models.Model):


    category = models.CharField(max_length=255)
    sku = models.CharField(max_length=255, unique=True,null=False)
    name = models.CharField(max_length=255)
    inStock = models.PositiveBigIntegerField()
    availableStock = models.PositiveBigIntegerField()
    tag1 = models.BooleanField(null=False,default=False)
    tag2 = models.BooleanField(null=False,default=False)
    tag3 = models.BooleanField(null=False,default=False)
    tag4 = models.BooleanField(null=False,default=False)
    tag5 = models.BooleanField(null=False,default=False)
    id = models.AutoField(primary_key=True)

    def __str__(self) -> str:
        return self.name
