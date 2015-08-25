from django.db import models
from django.utils.translation import (
    gettext,
    gettext_lazy,
)


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name=gettext('Title'))

    def __str__(self):
        return 'Category: {}'.format(self.title)

    class Meta:
        ordering = ['title']
        verbose_name = gettext_lazy('Category')
        verbose_name_plural = gettext_lazy('Categories')


class Tag(models.Model):
    title = models.CharField(max_length=255, verbose_name=gettext('Title'))

    def __str__(self):
        return 'Tag: {}'.format(self.title)

    class Meta:
        ordering = ['title']
        verbose_name = gettext_lazy('Tag')
        verbose_name_plural = gettext_lazy('Tags')


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name=gettext('Title'))
    is_important = models.BooleanField(default=False, verbose_name=gettext('Important?'))
    due_date = models.DateTimeField(null=True, blank=True, verbose_name=gettext('Due date'))
    category = models.ForeignKey(Category)
    parent = models.ForeignKey('self', null=True, blank=True, verbose_name=gettext('Parent task'))
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return 'Task: {}'.format(self.title)

    class Meta:
        ordering = ['title']
        verbose_name = gettext_lazy('Task')
        verbose_name_plural = gettext_lazy('Task')
