from django.shortcuts import render, get_object_or_404, redirect
from .models import AtendimentoSocial
from .forms import AtendimentoSocialForm

def lista_atendimentos(request):
    atendimentos = AtendimentoSocial.objects.all()
    return render(request, 'assistencia_social/lista_atendimentos.html', {'atendimentos': atendimentos})

def cadastro_atendimento(request):
    if request.method == 'POST':
        form = AtendimentoSocialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_atendimentos')
    else:
        form = AtendimentoSocialForm()
    return render(request, 'assistencia_social/cadastro_atendimento.html', {'form': form})

def detalhes_atendimento(request, pk):
    atendimento = get_object_or_404(AtendimentoSocial, pk=pk)
    return render(request, 'assistencia_social/detalhes_atendimento.html', {'atendimento': atendimento})