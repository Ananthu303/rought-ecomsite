# Generated by Django 4.1.5 on 2023-02-21 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_notification',
            name='dtime',
            field=models.DateField(auto_now_add=True),
        ),
    ]
