# Generated by Django 3.0.4 on 2020-04-22 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_item_descrp'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
