# Generated by Django 3.2.9 on 2021-11-25 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default=None, upload_to='main/static/imagenes_productos/'),
        ),
    ]