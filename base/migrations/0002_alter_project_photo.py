# Generated by Django 4.1.5 on 2023-01-28 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='post_images/', verbose_name='Project photo'),
        ),
    ]
