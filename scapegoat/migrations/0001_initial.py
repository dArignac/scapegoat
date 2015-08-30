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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
                ('url', models.URLField(verbose_name='URL', null=True, blank=True)),
                ('is_important', models.BooleanField(verbose_name='Important?', default=False)),
                ('due_date', models.DateTimeField(verbose_name='Due date', null=True, blank=True)),
                ('category', models.ForeignKey(to='scapegoat.Category')),
                ('parent', models.ForeignKey(verbose_name='Parent task', to='scapegoat.Task', null=True, blank=True)),
                ('tags', models.ManyToManyField(to='scapegoat.Tag', blank=True)),
            ],
            options={
                'verbose_name': 'Task',
                'ordering': ['title'],
                'verbose_name_plural': 'Task',
            },
        ),
    ]
