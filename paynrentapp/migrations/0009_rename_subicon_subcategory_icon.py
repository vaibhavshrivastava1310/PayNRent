# Generated by Django 3.2.17 on 2023-03-16 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paynrentapp', '0008_subcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='subicon',
            new_name='icon',
        ),
    ]