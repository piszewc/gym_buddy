# Generated by Django 2.1.7 on 2019-04-10 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight_buddy', '0015_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercisesdetail',
            name='slug',
            field=models.SlugField(blank=True, max_length=60, verbose_name='slug'),
        ),
    ]
