# Generated by Django 2.2 on 2019-05-02 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cse', '0008_auto_20190502_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='customuser',
            name='blood_group',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='customuser',
            name='department',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='customuser',
            name='designation',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='customuser',
            name='mobile_no',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='customuser',
            name='tel_no',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
