# Generated by Django 3.1.5 on 2021-02-12 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210211_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendsuser',
            name='nickname',
        ),
    ]
