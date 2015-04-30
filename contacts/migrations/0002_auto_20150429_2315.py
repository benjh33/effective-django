# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='salutation',
            field=models.CharField(max_length=5, blank=True, default='none', choices=[(None, ''), ('Mr.', 'Mr.'), ('Ms.', 'Ms.'), ('Dr.', 'Dr.'), ('none', 'none')]),
        ),
    ]
