# Generated by Django 5.0.6 on 2024-07-16 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itempedido',
            name='preco',
            field=models.FloatField(verbose_name='preço'),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='preco_promocional',
            field=models.FloatField(default=0, verbose_name='preço promocional'),
        ),
    ]
