# Generated by Django 3.2.2 on 2021-06-04 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerece', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='qty',
            field=models.IntegerField(default=0),
        ),
    ]
