# Generated by Django 2.1.7 on 2019-04-10 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight_buddy', '0017_auto_20190410_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercisesdetail',
            name='slug',
            field=models.SlugField(blank=True, max_length=40, null=True),
        ),
    ]