# -*- coding: utf-8 -*-
from django.db import models


class Matriz(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    w = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.w)
