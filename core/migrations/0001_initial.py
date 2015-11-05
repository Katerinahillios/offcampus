# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.IntegerField(default=0, choices=[(0, b'Select...'), (1, b'Fall Festivities'), (2, b'Winter Festivities'), (3, b'Spring Festivities'), (4, b'Bite To Eat'), (5, b'Night Life'), (6, b'Girls Night Out'), (7, b'Date Night')])),
                ('place', models.CharField(default=b'', max_length=300)),
                ('description', models.TextField(default=b'', null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
