from django.db import models

from djcroco.fields import CrocoField

class Example(models.Model):
    name = models.CharField(max_length=255)
    document = CrocoField(thumbnail_field='test_thumbnail')
    test_thumbnail = models.ImageField(upload_to='crocodoc/uploads/')
    

    def __unicode__(self):
        return self.name
