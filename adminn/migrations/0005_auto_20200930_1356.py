# Generated by Django 3.0.8 on 2020-09-30 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminn', '0004_userr_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userr',
            name='Favourite',
        ),
        migrations.AddField(
            model_name='account',
            name='Favourite',
            field=models.CharField(default='', max_length=100),
        ),
    ]
