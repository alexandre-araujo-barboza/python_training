# Generated by Django 5.0.6 on 2024-07-16 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_alter_itempedido_preco_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itempedido',
            name='variacao',
            field=models.CharField(max_length=255, verbose_name='variação'),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='variacao_id',
            field=models.PositiveIntegerField(verbose_name='variação id'),
        ),
    ]
