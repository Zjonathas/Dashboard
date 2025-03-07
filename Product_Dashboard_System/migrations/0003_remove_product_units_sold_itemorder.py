# Generated by Django 5.0.6 on 2024-07-11 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_Dashboard_System', '0002_product_units_sold'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='units_sold',
        ),
        migrations.CreateModel(
            name='ItemOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product_Dashboard_System.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product_Dashboard_System.product')),
            ],
        ),
    ]
