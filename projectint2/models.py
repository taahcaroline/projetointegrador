from django.db import models
from django.contrib.auth import get_user_model

STATUS = (
    ('doing', 'Doing'),
    ('done', 'Done'),
)

class Cronograma(models.Model):
    title = models.CharField(max_length=500)
    datainicio = models.DateField()
    description = models.TextField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.title

class Conteudoprog(models.Model):
    title = models.CharField('Nome da Vaga', max_length=500)
    description = models.TextField('Conteúdo Progmático')
    datainicio = models.DateField('Data da prova')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title