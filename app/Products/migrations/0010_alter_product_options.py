# Generated by Django 3.2.10 on 2022-01-04 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0009_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
    ]