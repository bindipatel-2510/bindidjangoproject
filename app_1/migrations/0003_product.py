# Generated by Django 3.0 on 2021-05-04 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0002_user_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(choices=[('kid', 'kid'), ('men', 'men'), ('women', 'women')], max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.IntegerField()),
                ('product_desc', models.TextField()),
                ('product_color', models.CharField(choices=[('red', 'red'), ('black', 'black'), ('green', 'green'), ('blue', 'blue'), ('yellow', 'yellow')], max_length=100)),
                ('product_size', models.CharField(choices=[('s', 's'), ('m', 'm'), ('l', 'l')], max_length=100)),
                ('product_image', models.ImageField(upload_to='product_images/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.User')),
            ],
        ),
    ]
