from django import forms
from .models import Cronograma, Conteudoprog

class CronogramaForm(forms.ModelForm):
    class Meta:
     model = Cronograma
     fields = ('title', 'description', 'datainicio')


class ConteudoprogForm(forms.ModelForm):
    class Meta:
     model = Conteudoprog
     fields = ('title', 'description', 'datainicio')