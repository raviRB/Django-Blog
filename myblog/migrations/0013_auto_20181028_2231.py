# Generated by Django 2.1.2 on 2018-10-28 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0012_auto_20181028_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='password',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='username',
            field=models.CharField(max_length=254),
        ),
    ]