# Generated by Django 3.2.4 on 2021-06-10 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user',
        ),
    ]
