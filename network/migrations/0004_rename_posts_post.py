# Generated by Django 3.2.5 on 2021-09-18 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_posts_timestamp'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]
