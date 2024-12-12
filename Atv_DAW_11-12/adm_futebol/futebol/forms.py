from django.forms import ModelForm
from .models import Equipe, Jogador

class EquipeForm(ModelForm):
    class Meta:
        model = Equipe
        fields = ['nome', 'cidade']

class JogadorForm(ModelForm):
    class Meta:
        model = Jogador
        fields = ['nome', 'idade', 'equipe']
