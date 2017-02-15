#-*- coding: utf-8 -*-
from django.db import models
import os
 
# Create your models here.

########## Relation ForeignKey #######

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    author = models.CharField(max_length=42)
    content = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de publication")
    category = models.ForeignKey('Category')

    def __unicode__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que nous
        traiterons plus tard et dans l'administration
        """
        return u"%s" % self.title

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

########## Relation OneToOneField #######

class Motor(models.Model):
    name = models.CharField(max_length=25)
    def __unicode__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=25)
    motor = models.OneToOneField(Motor)

    def __unicode__(self):
        return self.name

########## Relation ManyToManyField #######

class Product(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=30)
    products = models.ManyToManyField(Product, through='Offer')

    def __unicode__(self):
        return self.name


class Offer(models.Model):
    price = models.IntegerField()
    product = models.ForeignKey(Product)
    vendor = models.ForeignKey(Vendor)

    def __unicode__(self):
        return "{0} vendu par {1}".format(self.product, self.vendor)

########## Contact : Gestion des fichiers #######
class Contact(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    image = models.ImageField(upload_to="images/")

    def __unicode__(self):
           return self.name

def rename(instance, name):
     file_name = os.path.splitext(name)[0] # on retire l'extension
     return "{}-{}".format(instance.id, file_name)


class Document(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="files/", verbose_name="Document")
    #file = models.FileField(upload_to=rename, verbose_name="Document")


