from django.db import models

# Create your models here.


class List(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    order = models.PositiveSmallIntegerField(default=10)

    class Meta:  # NOQA
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class ListItem(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField(default=10)
    list = models.ForeignKey(List)

    class Meta:  # NOQA
        ordering = ['list__order', 'order', 'title']

    def __str__(self):
        return '{} (#{} in "{}")'.format(
            self.title,
            self.list.order,
            self.list.title
        )
