# Generated by Django 3.2.22 on 2023-10-15 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20231015_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='address',
        ),
        migrations.RemoveField(
            model_name='person',
            name='nationality',
        ),
        migrations.RemoveField(
            model_name='person',
            name='passport',
        ),
    ]
