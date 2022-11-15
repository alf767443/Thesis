# Generated by Django 3.2.13 on 2022-11-14 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('DepartmentId', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Employes',
            fields=[
                ('EmployesId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployesName', models.CharField(max_length=500)),
                ('Department', models.CharField(max_length=500)),
                ('DateOfJoining', models.DateField()),
                ('PhotoFieldName', models.CharField(max_length=500)),
            ],
        ),
    ]
