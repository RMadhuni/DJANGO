# Generated by Django 4.2.3 on 2023-08-08 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0004_customer_datecreated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
