# Generated by Django 5.1.2 on 2024-11-06 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='curse',
            new_name='course',
        ),
    ]
