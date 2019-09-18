from django.db import models

# Create your models here.

class Module (models.Model):
    titre =  models.CharField(max_length = 255 )
    image = models.ImageField(upload_to='module', blank=True)
    date_add = models.DateTimeField(auto_now_add = True)
    date_upd = models.DateTimeField(auto_now = True)
    statut = models.BooleanField(default = False)

class Quiz (models.Model):
    titre =  models.CharField(max_length = 255 )
    #auteur =  models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'auteur')
    description =  models.CharField(max_length = 255 )
    module_id =  models.ForeignKey('Module', on_delete = models.CASCADE, related_name = 'modulr_quiz')
    duree = models.DateTimeField (auto_now_add = True)
    date_add = models.DateTimeField(auto_now_add = True)
    date_upd = models.DateTimeField(auto_now = True)
    statut = models.BooleanField(default = True)

class Question (models.Model):
    question =  models.CharField(max_length = 255 )
    quiz_id =  models.ForeignKey('Quiz',on_delete = models.CASCADE, related_name = 'Quiz_question')
    date_add = models.DateTimeField(auto_now_add = True)
    date_upd = models.DateTimeField(auto_now = True)
    statut = models.BooleanField(default = False)

class Reponse (models.Model):
    reponse =  models.CharField(max_length = 255 )
    point =  models.IntegerField(default=0)
    question_id =  models.ForeignKey('Question',on_delete = models.CASCADE, related_name = 'question_rep')
    statut = models.BooleanField(default = False)

class Resultat (models.Model):
    #user_id = models.ForeignKey('User', on_delete = models.CASCADE, related_name = 'user_resultat')
    quiz_id = models.ForeignKey('Quiz', on_delete = models.CASCADE, related_name = 'quiz_resultat')
    date = models.DateTimeField(auto_now_add = True)
    statut = models.BooleanField(default = False)

