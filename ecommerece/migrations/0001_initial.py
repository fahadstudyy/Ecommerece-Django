# Generated by Django 3.2.2 on 2021-05-30 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('descreption', models.TextField(max_length=1000)),
                ('qty', models.IntegerField()),
                ('Image', models.ImageField(upload_to='myshop/produtc-images')),
                ('URL', models.URLField(blank=True)),
            ],
        ),
    ]
