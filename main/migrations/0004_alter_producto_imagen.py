# Generated by Django 3.2.9 on 2021-11-23 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default=None, upload_to='static/products/'),
        ),
    ]
