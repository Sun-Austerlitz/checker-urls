# Generated by Django 4.1.2 on 2022-10-28 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='status_code',
        ),
    ]
