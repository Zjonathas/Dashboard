# Generated by Django 5.0.6 on 2024-07-08 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_client', models.CharField(max_length=200)),
                ('email_client', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=9)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=400, null=True)),
                ('status', models.CharField(choices=[('P', 'Pedido realizado'), ('F', 'Fazendo'), ('E', 'Saiu para entrega')], max_length=1)),
                ('products', models.ManyToManyField(to='Product_Dashboard_System.product')),
            ],
        ),
    ]
