# Generated by Django 3.2.17 on 2023-03-26 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paynrentapp', '0011_vehicles_varient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicles',
            old_name='varient',
            new_name='variant',
        ),
    ]
