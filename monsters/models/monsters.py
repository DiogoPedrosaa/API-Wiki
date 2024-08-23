from django.db import models
from items.models import Item

class Monster(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    health = models.IntegerField()
    weakness = models.CharField(max_length=100)
    drop_item = models.ManyToManyField(Item)

    def __str__(self):
        return self.name

