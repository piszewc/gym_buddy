# Generated by Django 2.1.3 on 2018-12-01 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight_buddy', '0019_training_workout_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercises',
            name='repetitions_number',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exercises',
            name='set_number',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]