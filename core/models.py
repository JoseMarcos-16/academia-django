from django.db import models


class Modalidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    modalidade = models.ForeignKey(
        Modalidade,
        on_delete=models.PROTECT
    )

    dia_semana = models.CharField(max_length=20)

    horario = models.TimeField()

    instrutor = models.CharField(max_length=100)

    vagas = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"{self.modalidade} - {self.dia_semana}"