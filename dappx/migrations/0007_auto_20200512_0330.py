# Generated by Django 3.0.6 on 2020-05-12 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0006_products_changedprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]