# Generated by Django 3.0.5 on 2020-04-20 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notes_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_profile',
            new_name='user',
        ),
    ]
