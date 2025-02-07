from django.shortcuts import render, get_object_or_404, redirect
from .models import FichaAnamnese
from .forms import FichaAnamneseForm

def lista_fichas(request):
    fichas = FichaAnamnese.objects.all()
    return render(request, 'saude/lista_fichas.html', {'fichas': fichas})

def cadastro_ficha(request):
    if request.method == 'POST':
        form = FichaAnamneseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_fichas')
    else:
        form = FichaAnamneseForm()
    return render(request, 'saude/cadastro_ficha.html', {'form': form})

def detalhes_ficha(request, pk):
    ficha = get_object_or_404(FichaAnamnese, pk=pk)
    return render(request, 'saude/detalhes_ficha.html', {'ficha': ficha})