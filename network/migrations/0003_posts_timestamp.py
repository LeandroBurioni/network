# Generated by Django 3.2.5 on 2021-09-18 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
