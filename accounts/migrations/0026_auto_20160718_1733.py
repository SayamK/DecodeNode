# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-07-18 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_auto_20160718_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='profile_picture',
            field=models.ImageField(blank=True, default='static/assets/user_images/default.png', upload_to='static/assets/user_images/'),
        ),
    ]
