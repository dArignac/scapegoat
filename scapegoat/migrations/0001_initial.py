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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Category',
                'ordering': ['title'],
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Tag',
                'ordering': ['title'],
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('is_important', models.BooleanField(verbose_name='Important?', default=False)),
                ('due_date', models.DateTimeField(verbose_name='Due date', blank=True, null=True)),
                ('category', models.ForeignKey(to='scapegoat.Category')),
                ('parent', models.ForeignKey(to='scapegoat.Task', null=True, blank=True, verbose_name='Parent task')),
                ('tags', models.ManyToManyField(to='scapegoat.Tag', blank=True)),
            ],
            options={
                'verbose_name': 'Task',
                'ordering': ['title'],
                'verbose_name_plural': 'Task',
            },
        ),
    ]
