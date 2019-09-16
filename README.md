# Quiz model Django
 Model du Quiz django

**Modules**
```
titre =  models.CharField(max_length = 255 )
image = models.ImageField(upload_to='image/', blank=True)
date_add = models.DateTimeField(auto_now_add = True)
date_upd = models.DateTimeField(auto_now = True)
statut = models.BooleanField(default = True)
```
**Quiz**
```
titre =  models.CharField(max_length = 255 )
auteur =  models.ForeignKey('User', on_delete = models.CASCADE, related_name = 'auteur')
user_id =  models.ManyToManyField ('User', related_name = 'user' )
description =  models.CharField(max_length = 255 )
model_id =  models.ForeignKey('Model', on_delete = models.CASCADE, related_name = 'model_quiz')
image = models.ImageField(upload_to='image/', blank=True)
duree = models.DateTimeField (auto_now_add = True)
date_add = models.DateTimeField(auto_now_add = True)
date_upd = models.DateTimeField(auto_now = True)
statut = models.BooleanField(default = True)
```
**Questions**
```
question =  models.CharField(max_length = 255 )
reponse_id =  models.ForeignKey('Reponse',on_delete = models.CASCADE, related_name = 'Rep_question')
quiz_id =  models.ForeignKey('Quiz',on_delete = models.CASCADE, related_name = 'Quiz_question')
date_add = models.DateTimeField(auto_now_add = True)
date_upd = models.DateTimeField(auto_now = True)
statut = models.BooleanField(default = True)
```
**Reponses**
```
reponse =  models.CharField(max_length = 255 )
point =  models.IntegerField(default=0)
statut = models.BooleanField(default = True)
```
**Resultat**
```
user_id = models.ForeignKey('User', on_delete = models.CASCADE, related_name = 'user_resultat')
quiz_id = models.ForeignKey('Quiz', on_delete = models.CASCADE, related_name = 'quiz_resultat')
date = models.DateTimeField(auto_now_add = True)
statut = models.BooleanField(default = True)
```
