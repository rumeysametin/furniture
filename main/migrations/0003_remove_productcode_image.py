# Generated by Django 4.0.2 on 2022-02-19 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_color_material_productcode_alter_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcode',
            name='image',
        ),
    ]
