# Generated by Django 3.2.17 on 2023-03-15 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paynrentapp', '0002_alter_category_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryid', models.IntegerField(default='', max_length=200)),
                ('companyname', models.CharField(default='', max_length=200)),
                ('subcategoryname', models.CharField(default='', max_length=200)),
                ('description', models.CharField(default='', max_length=200)),
                ('icon', models.ImageField(upload_to='static/')),
            ],
        ),
    ]
