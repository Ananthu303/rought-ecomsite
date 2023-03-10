# Generated by Django 4.1.5 on 2023-02-21 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='audiomodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audioname', models.CharField(max_length=30)),
                ('audioimage', models.ImageField(upload_to='djangoapp/static')),
                ('audiofile', models.FileField(upload_to='djangoapp/static')),
            ],
        ),
        migrations.CreateModel(
            name='buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('des', models.CharField(max_length=500)),
                ('pimage', models.ImageField(upload_to='')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('pname', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('des', models.CharField(max_length=500)),
                ('pimage', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='customerdetailsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('cardno', models.CharField(max_length=30)),
                ('cardexpiry', models.CharField(max_length=30)),
                ('security', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='productuploadmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopid', models.IntegerField()),
                ('pname', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('des', models.CharField(max_length=500)),
                ('pimage', models.ImageField(upload_to='djangoapp/static')),
            ],
        ),
        migrations.CreateModel(
            name='shop_notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('dtime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='shopregmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopname', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('password', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user_notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='wishlistm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('pname', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('des', models.CharField(max_length=500)),
                ('pimage', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(max_length=100)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
