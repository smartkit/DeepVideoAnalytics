# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 07:55
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0013_clusters_indexer_algorithm'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClusterCodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fine', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[], size=None)),
                ('coarse', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[], size=None)),
                ('clusters', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Clusters')),
                ('detection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Detection')),
                ('frame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Frame')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video')),
            ],
        ),
    ]
