# Generated by Django 2.0.2 on 2020-07-15 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='image',
            new_name='imagepath',
        ),
    ]
