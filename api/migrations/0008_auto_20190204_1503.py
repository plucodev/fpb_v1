# Generated by Django 2.1.5 on 2019-02-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190204_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provider',
            name='price',
        ),
        migrations.AddField(
            model_name='provider',
            name='location',
            field=models.ManyToManyField(to='api.Location'),
        ),
    ]
