# Generated by Django 4.0.3 on 2022-05-21 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickle',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
