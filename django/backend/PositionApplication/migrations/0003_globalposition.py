# Generated by Django 3.2.13 on 2022-11-24 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PositionApplication', '0002_auto_20221115_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalPosition',
            fields=[
                ('GlobalPositionId', models.AutoField(primary_key=True, serialize=False)),
                ('GlobalPositionX', models.IntegerField()),
                ('GlobalPositionY', models.IntegerField()),
            ],
        ),
    ]
