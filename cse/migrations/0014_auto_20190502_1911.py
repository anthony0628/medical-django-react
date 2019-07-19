# Generated by Django 2.2 on 2019-05-02 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cse', '0013_auto_20190502_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='blood_group',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='department',
            field=models.CharField(default=None, max_length=90),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='designation',
            field=models.CharField(default=None, max_length=90),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='height',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mobile_no',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='photos',
            field=models.FileField(default=None, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='tel_no',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
