from django.db import models

class FichaAnamnese(models.Model):
    aluno = models.ForeignKey('alunos.Aluno', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=[('dentista', 'Dentista'), ('psicologo', 'Psicólogo'), ('nutricionista', 'Nutricionista'), ('medico', 'Médico')])
    historico = models.TextField()
    habitos = models.TextField(blank=True, null=True)
    avaliacoes = models.TextField(blank=True, null=True)
    diagnósticos = models.TextField(blank=True, null=True)
    encaminhamentos = models.TextField(blank=True, null=True)
    data_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.aluno.nome_completo} - {self.tipo}'