# Generated by Django 4.0.1 on 2022-01-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='otp',
            field=models.IntegerField(default=0),
        ),
    ]
