from __future__ import unicode_literals

from django.db import models


class Messages(models.Model):

    create_time = models.DateTimeField('Date', auto_now_add=True, db_index=True)
    city        = models.CharField('City',  max_length=64, db_index=True)
    message     = models.TextField('Message')
    state       = models.CharField('State', max_length=64, db_index=True)
    username    = models.CharField('User',  max_length=64)

    class Meta:
        ordering = ['state', 'city', 'create_time']

    @classmethod
    def countdistinct(cls, field):
        return cls.objects.filter().values(field).distinct().count()

    @classmethod
    def count_cities(cls):
        return cls.countdistinct('city')

    @classmethod
    def count_usernames(cls):
        return cls.countdistinct('username')

