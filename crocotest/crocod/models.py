from django.db import models

# djcroco import
from djcroco.fields import CrocoField

class Example(models.Model):
    name = models.CharField(max_length=255)
    # Can also pass thumbnail_size=(150,150) in CrocoField, right now it defaults to 100,100
    # Also for the CrocoField, make sure the thumbnail_filed is an ImageField, as so below
    document = CrocoField(thumbnail_field='thumbnail')
    thumbnail = models.ImageField(upload_to='uploads/')
    

    def __unicode__(self):
        return self.name
    
class NullableExample(models.Model):
    name = models.CharField(max_length=255)
    document = CrocoField(null=True)
    
    def __unicode__(self):
        return self.name
