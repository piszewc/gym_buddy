# Generated by Django 2.1.7 on 2019-03-30 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight_buddy', '0010_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='equipment_images/'),
        ),
    ]