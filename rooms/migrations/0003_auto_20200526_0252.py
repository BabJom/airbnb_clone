# Generated by Django 3.1a1 on 2020-05-25 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='img_file',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
