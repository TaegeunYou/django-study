# Generated by Django 3.1.3 on 2021-09-26 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0007_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
