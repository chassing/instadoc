# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.CharField(max_length=254)),
                ('url', models.CharField(max_length=254, blank=True)),
            ],
            options={
                'ordering': ('item',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.CharField(max_length=254)),
                ('url', models.CharField(max_length=254)),
                ('html', models.TextField(blank=True)),
                ('category', models.ForeignKey(related_name='docs', to='main.Category')),
            ],
            options={
                'ordering': ('-item',),
            },
            bases=(models.Model,),
        ),
    ]
