# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=127)),
                ('title_en', models.CharField(max_length=127, null=True)),
                ('title_ar', models.CharField(max_length=127, null=True)),
                ('info', models.TextField()),
                ('info_en', models.TextField(null=True)),
                ('info_ar', models.TextField(null=True)),
            ],
        ),
    ]
