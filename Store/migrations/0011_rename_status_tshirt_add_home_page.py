# Generated by Django 3.2.8 on 2021-11-15 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0010_alter_tshirt_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tshirt',
            old_name='Status',
            new_name='Add_Home_Page',
        ),
    ]