# Generated by Django 4.1.2 on 2022-11-09 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_order_options_alter_order_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='subtotal',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
