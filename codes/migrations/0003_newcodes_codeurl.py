# Generated by Django 3.2.9 on 2022-01-04 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0002_newcodes_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcodes',
            name='codeurl',
            field=models.URLField(default='', max_length=2000),
        ),
    ]
