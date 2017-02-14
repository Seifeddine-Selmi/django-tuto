#-*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.text import Truncator


from .models import Category, Article, Motor, Car


class ArticleAdmin(admin.ModelAdmin):
 # Personnalisons l'administration
    list_display   = ('title', 'author','category', 'date', 'display_content')
    list_filter    = ('author','category', 'date')
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('title', 'content', 'date')

    def display_content(self, article):
        """
        Retourne les 40 premiers caractères du contenu de l'article,
        suivi de points de suspension si le texte est plus long.
        """
        return Truncator(article.content).chars(40, truncate='...')

    # En-tête de notre colonne
    display_content.short_description = 'Aperçu du contenu'


  # Modifier le formulaire d'édition
    #fields = ('title', 'slug', 'author', 'category', 'content')
   # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (title, author…)
       ('Général', {
            'classes': ['collapse', ],
            'fields': ('title', 'slug', 'author', 'category')
        }),
        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article', {
           'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
           'fields': ('content', )
        }),
    )
    prepopulated_fields = {'slug': ('title', ), }


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)


#admin.site.register(Motor)
#admin.site.register(Car)