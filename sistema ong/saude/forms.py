from django import forms
from .models import FichaAnamnese

class FichaAnamneseForm(forms.ModelForm):
    class Meta:
        model = FichaAnamnese
        fields = ['aluno', 'tipo', 'historico', 'habitos', 'avaliacoes', 'diagnósticos', 'encaminhamentos']