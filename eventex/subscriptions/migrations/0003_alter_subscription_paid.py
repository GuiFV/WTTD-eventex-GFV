# Generated by Django 3.2.9 on 2022-02-16 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_auto_20220216_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='pago'),
        ),
    ]
