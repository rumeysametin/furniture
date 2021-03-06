# Generated by Django 4.0.2 on 2022-02-19 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_productcode_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='product_imgs/')),
                ('detail', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productcode')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.color')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.material')),
            ],
        ),
    ]
