# Generated by Django 5.0.6 on 2024-07-23 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_alter_itempedido_variacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='quantidade',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
