# Generated by Django 2.0.7 on 2020-01-25 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='summary',
            field=models.TextField(default='This is cool'),
        ),
    ]
