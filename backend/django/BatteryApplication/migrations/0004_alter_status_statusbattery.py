# Generated by Django 3.2.13 on 2022-11-15 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BatteryApplication', '0003_auto_20221115_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='StatusBattery',
            field=models.IntegerField(),
        ),
    ]