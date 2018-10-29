# Generated by Django 2.1.2 on 2018-10-25 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_posts_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='my_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
