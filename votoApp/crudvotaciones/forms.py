from django import forms
from django.forms import ModelForm
from crudvotaciones.models import Ciudadanos
from crudvotaciones.models import Candidaturas
from crudvotaciones.models import Votos
class CiudadanosForm(forms.ModelForm):
    class Meta:
        model = Ciudadanos
        fields = '__all__'
class CandidaturasForm(forms.ModelForm):
    class Meta:
        model = Candidaturas
        fields = '__all__'
class VotosForm(forms.ModelForm):
    class Meta:
        model = Votos
        fields = '__all__'