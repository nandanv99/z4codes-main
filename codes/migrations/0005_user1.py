# Generated by Django 3.2.9 on 2022-03-06 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0004_exp'),
    ]

    operations = [
        migrations.CreateModel(
            name='user1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passwor', models.CharField(max_length=200)),
            ],
        ),
    ]