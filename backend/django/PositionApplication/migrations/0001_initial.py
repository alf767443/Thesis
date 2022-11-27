# Generated by Django 3.2.13 on 2022-11-15 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fiducial',
            fields=[
                ('FiducialId', models.AutoField(primary_key=True, serialize=False)),
                ('FiducialMark', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Gyroscope',
            fields=[
                ('GyroscopeId', models.AutoField(primary_key=True, serialize=False)),
                ('GyroscopeAngle', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Odometry',
            fields=[
                ('OdometryId', models.AutoField(primary_key=True, serialize=False)),
                ('OdometryLeft', models.BinaryField()),
                ('OdometryRight', models.BinaryField()),
            ],
        ),
    ]