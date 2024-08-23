from django.db import models
from items.models import Item

class Monster(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    health = models.IntegerField()
    weakness = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DropItem(models.Model):
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    drop_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.item.name} dropped by {self.monster.name}"