# Generated by Django 3.2.8 on 2021-10-12 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_sizevariant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sizevariant',
            name='price',
            field=models.IntegerField(),
        ),
    ]
