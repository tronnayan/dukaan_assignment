# Generated by Django 4.0.1 on 2022-01-16 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0011_alter_products_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]