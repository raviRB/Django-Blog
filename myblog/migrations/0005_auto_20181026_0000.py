# Generated by Django 2.1.2 on 2018-10-25 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_detail',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_picture/'),
        ),
    ]
