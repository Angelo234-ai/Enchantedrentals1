# Generated by Django 3.2.9 on 2021-12-10 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_remove_category_pricing_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='pricing_table',
            field=models.TextField(blank=True, null=True),
        ),
    ]
