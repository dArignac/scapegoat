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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
                ('is_important', models.BooleanField(verbose_name='Important?', default=False)),
                ('due_date', models.DateTimeField(verbose_name='Due date', null=True, blank=True)),
                ('category', models.ForeignKey(to='scapegoat.Category')),
                ('parent', models.ForeignKey(verbose_name='Parent task', to='scapegoat.Task', blank=True, null=True)),
                ('tags', models.ManyToManyField(to='scapegoat.Tag', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Task',
                'ordering': ['title'],
            },
        ),
    ]
