# Generated by Django 3.2.22 on 2023-10-15 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_remove_person_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.CharField(blank=True, default='no', max_length=20, null=True),
        ),
    ]
