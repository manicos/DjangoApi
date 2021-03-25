from django.db import models

# Create your models here.

class Dogs(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=250, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dogs'


class Types(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'types'

class DogFoods(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    brand = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dog_foods'

