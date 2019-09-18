
# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from . import models

#configuration du site

admin.site.site_title = " mon site "
admin.site.site_header = " NaN "

class ModuleAdmin(admin.ModelAdmin):

    list_display = ('affiche_image', 'id', 'titre', 'image', 'date_add', 'date_upd', 'statut')
    list_filter = (
        'date_add',
        'date_upd',
        'statut',
        'id',
        'titre',
        'image',
        'date_add',
        'date_upd',
        'statut',
    )
    search_fields = ( 'titre' , 'date_add' ,)
    def affiche_image(self, obj):
        return mark_safe('<img src = "{url}" width = " 100px " heigth = " 50px " />'.format(url= obj.image.url))


class QuizAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'module_id',
        'duree',
        'date_add',
        'date_upd',
        'statut',
    )
    list_filter = (
        'module_id',
        'duree',
        'date_add',
        'date_upd',
        'statut',
        'id',
        'titre',
        'description',
        'module_id',
        'duree',
        'date_add',
        'date_upd',
        'statut',
    )
    search_fields = ( 'titre' , 'date_add' ,)

class QuestionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'question',
        'quiz_id',
        'date_add',
        'date_upd',
        'statut',
    )
    list_filter = (
        'quiz_id',
        'date_add',
        'date_upd',
        'statut',
        'id',
        'question',
        'quiz_id',
        'date_add',
        'date_upd',
        'statut',
    )


class ReponseAdmin(admin.ModelAdmin):

    list_display = ('id', 'reponse', 'point', 'question_id', 'statut')
    list_filter = (
        'question_id',
        'statut',
        'id',
        'reponse',
        'point',
        'question_id',
        'statut',
    )


class ResultatAdmin(admin.ModelAdmin):

    list_display = ('id', 'quiz_id', 'date', 'statut')
    list_filter = (
        'quiz_id',
        'date',
        'statut',
        'id',
        'quiz_id',
        'date',
        'statut',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Module, ModuleAdmin)
_register(models.Quiz, QuizAdmin)
_register(models.Question, QuestionAdmin)
_register(models.Reponse, ReponseAdmin)
_register(models.Resultat, ResultatAdmin)
