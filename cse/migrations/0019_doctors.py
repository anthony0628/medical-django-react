# Generated by Django 2.2 on 2019-05-07 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cse', '0018_auto_20190507_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('doctor_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('email', models.EmailField(default=None, max_length=254)),
            ],
        ),
    ]