# Generated by Django 3.2.9 on 2021-12-09 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_category_pricing_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='pricing_table',
        ),
    ]