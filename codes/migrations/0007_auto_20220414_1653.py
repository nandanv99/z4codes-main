# Generated by Django 3.2.9 on 2022-04-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0006_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='collage',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='files',
            name='sem',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='files',
            name='year',
            field=models.CharField(default='', max_length=5),
        ),
    ]
