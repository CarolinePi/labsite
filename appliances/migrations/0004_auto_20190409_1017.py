# Generated by Django 2.1.7 on 2019-04-09 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appliances', '0003_auto_20190409_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fridgemodel',
            name='clicks',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tvmodel',
            name='clicks',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
