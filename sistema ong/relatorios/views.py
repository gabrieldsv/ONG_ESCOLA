from django.shortcuts import render

def relatorio_frequencia(request):
    # Implementar lógica para gerar relatório de frequência
    return render(request, 'relatorios/relatorio_frequencia.html')

def relatorio_cursos(request):
    # Implementar lógica para gerar relatório de cursos
    return render(request, 'relatorios/relatorio_cursos.html')

def relatorio_certificados(request):
    # Implementar lógica para gerar relatório de certificados
    return render(request, 'relatorios/relatorio_certificados.html')