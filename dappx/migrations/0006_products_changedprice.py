# Generated by Django 3.0.5 on 2020-05-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0005_cartitem_carttable_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='changedprice',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]