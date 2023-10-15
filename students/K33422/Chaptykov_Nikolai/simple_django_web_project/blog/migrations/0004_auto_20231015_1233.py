# Generated by Django 3.2.22 on 2023-10-15 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_ownershipupdated_cartoperson'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartoperson',
            old_name='owners',
            new_name='cars',
        ),
        migrations.AddField(
            model_name='cartoperson',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.person'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='helpingtable',
            name='person',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.person'),
            preserve_default=False,
        ),
    ]
