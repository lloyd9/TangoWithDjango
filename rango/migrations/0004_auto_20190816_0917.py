# Generated by Django 2.1.5 on 2019-08-16 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20190816_0813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='category',
            name='views',
        ),
    ]
