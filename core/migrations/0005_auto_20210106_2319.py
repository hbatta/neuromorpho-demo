# Generated by Django 3.1.5 on 2021-01-06 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210106_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neuron',
            name='scientific_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]