# Generated by Django 2.1.7 on 2019-04-10 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight_buddy', '0016_exercisesdetail_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AlterField(
            model_name='exercisesdetail',
            name='slug',
            field=models.SlugField(max_length=40),
        ),
    ]
