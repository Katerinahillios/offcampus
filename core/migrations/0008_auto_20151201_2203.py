# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20151201_2201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='text',
        ),
    ]
