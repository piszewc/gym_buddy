# Generated by Django 2.1.3 on 2018-12-01 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight_buddy', '0023_auto_20181201_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercises',
            name='workout_type',
            field=models.CharField(choices=[('CHEST', 'CHEST'), ('DELTS', 'DELTS'), ('TRICEPS', 'TRICEPS'), ('BACK', 'BACK'), ('BICEPS', 'BICEPS'), ('FOREARMS', 'FOREARMS'), ('LEGS', 'LEGS'), ('ABS', 'ABS')], default='CHEST', max_length=10),
        ),
    ]
