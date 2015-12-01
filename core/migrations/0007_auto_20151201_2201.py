# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_place_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='comment',
        ),
    ]
