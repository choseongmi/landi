# Generated by Django 2.0.7 on 2018-08-07 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
    ]
