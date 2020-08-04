# Generated by Django 3.0.8 on 2020-08-04 05:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0002_thread_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='user',
            field=models.ForeignKey(default='guest', on_delete=models.SET('Deleted'), to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
