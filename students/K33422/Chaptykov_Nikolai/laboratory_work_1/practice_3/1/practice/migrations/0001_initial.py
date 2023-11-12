# Generated by Django 3.2.18 on 2023-11-11 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=15)),
                ('brand', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CarOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('birthdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice.car')),
                ('owner_id', models.ManyToManyField(to='practice.CarOwner')),
            ],
        ),
        migrations.CreateModel(
            name='DriverLicence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licence_id', models.CharField(max_length=10)),
                ('licence_type', models.CharField(max_length=10)),
                ('recieved_date', models.DateField()),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice.carowner')),
            ],
        ),
    ]
