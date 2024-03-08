from django.db import models
# Define the Item model with its fields and behaviors
class Item(models.Model):


    category = models.CharField(max_length=255)
    # Unique identifier field for the item (Stock Keeping Unit), max length 255 characters
    sku = models.CharField(max_length=255, unique=True,null=False)
    name = models.CharField(max_length=255)
    inStock = models.PositiveBigIntegerField()
    # Positive integer field for the number of available items in stock for sale
    availableStock = models.PositiveBigIntegerField()
    # Boolean fields representing five different tags for the item, defaulting to False
    tag1 = models.BooleanField(null=False,default=False)
    tag2 = models.BooleanField(null=False,default=False)
    tag3 = models.BooleanField(null=False,default=False)
    tag4 = models.BooleanField(null=False,default=False)
    tag5 = models.BooleanField(null=False,default=False)
    # An automatically incremented integer field that serves as the primary key for the item
    id = models.AutoField(primary_key=True)

    # String representation method to return the name of the item when it is printed
    def __str__(self) -> str:
        return self.name
