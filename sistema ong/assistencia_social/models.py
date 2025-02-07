from django.db import models

class AtendimentoSocial(models.Model):
    aluno = models.ForeignKey('alunos.Aluno', on_delete=models.CASCADE)
    data_atendimento = models.DateField()
    necessidades_identificadas = models.TextField()
    encaminhamentos_realizados = models.TextField()

    def __str__(self):
        return f'{self.aluno.nome_completo} - {self.data_atendimento}'