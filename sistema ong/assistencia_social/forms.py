from django import forms
from .models import AtendimentoSocial

class AtendimentoSocialForm(forms.ModelForm):
    class Meta:
        model = AtendimentoSocial
        fields = ['aluno', 'data_atendimento', 'necessidades_identificadas', 'encaminhamentos_realizados']