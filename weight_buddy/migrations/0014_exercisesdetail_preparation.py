# Generated by Django 2.1.7 on 2019-04-09 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight_buddy', '0013_auto_20190409_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercisesdetail',
            name='preparation',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
