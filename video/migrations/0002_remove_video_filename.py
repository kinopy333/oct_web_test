# Generated by Django 3.1.2 on 2020-11-02 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='filename',
        ),
    ]
