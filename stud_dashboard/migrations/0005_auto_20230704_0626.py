# Generated by Django 3.0.7 on 2023-07-04 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud_dashboard', '0004_auto_20230704_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(upload_to='media'),
        ),
    ]