# Generated by Django 3.0 on 2021-05-14 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0006_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]