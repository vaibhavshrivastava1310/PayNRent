# Generated by Django 3.2.17 on 2023-03-16 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paynrentapp', '0006_alter_subcategory_categoryid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]