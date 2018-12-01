# Generated by Django 2.1.3 on 2018-12-01 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weight_buddy', '0021_auto_20181201_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercises',
            name='workout_type',
            field=models.CharField(choices=[('CHEST', 'CHEST'), ('DELTS', 'DELTS'), ('TRICEPS', 'TRICEPS'), ('BACK', 'BACK'), ('BICEPS', 'BICEPS'), ('FOREARMS', 'FOREARMS'), ('LEGS', 'LEGS'), ('ABS', 'ABS')], default='CHEST', max_length=2),
        ),
        migrations.AddField(
            model_name='training',
            name='exercise_one',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='exercise_one', to='weight_buddy.Exercises'),
        ),
        migrations.AddField(
            model_name='training',
            name='weight_one',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='exercise',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='exercise', to='weight_buddy.Exercises'),
        ),
        migrations.AlterField(
            model_name='training',
            name='weight',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]