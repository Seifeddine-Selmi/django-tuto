#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import random
import string


class MiniURL(models.Model):
    url = models.URLField(verbose_name="URL à réduire", unique=True)
    code = models.CharField(max_length=6, unique=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date d'enregistrement")
    pseudo = models.CharField(max_length=255, blank=True, null=True)
    nb_access = models.IntegerField(default=0, verbose_name="Nombre d'accès à l'URL")

    def __unicode__(self):
        return "[{0}] {1}".format(self.code, self.url)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.generate(6)

        super(MiniURL, self).save(*args, **kwargs)

    def generate(self, nb_characters):
        characters = string.ascii_letters + string.digits
        mini_url = [random.choice(characters) for _ in range(nb_characters)]

        self.code = ''.join(mini_url)

    class Meta:
        verbose_name = "Mini URL"
        verbose_name_plural = "Minis URL"
