# Generated by Django 3.1.1 on 2022-01-21 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Snacks_App', '0004_auto_20220121_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product_description',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product_image',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product_price',
        ),
    ]
