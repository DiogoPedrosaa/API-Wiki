# Generated by Django 5.1 on 2024-08-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_remove_item_drop_from'),
        ('monsters', '0005_remove_monster_drop_item_monster_drop_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monster',
            name='drop_item',
        ),
        migrations.AddField(
            model_name='monster',
            name='drop_item',
            field=models.ManyToManyField(to='items.item'),
        ),
    ]
