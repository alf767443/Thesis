# Generated by Django 3.2.13 on 2022-11-24 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('RouteId', models.AutoField(primary_key=True, serialize=False)),
                ('RouteDistanceEstimated', models.FloatField()),
                ('RouteConsumptionEstimated', models.FloatField()),
                ('RouteDistanceReal', models.FloatField()),
                ('RouteConsumptionReal', models.FloatField()),
                ('RouteStartPoint', models.JSONField()),
                ('RouteEndPoint', models.JSONField()),
            ],
        ),
    ]
