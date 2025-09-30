from django.db import models
from django.utils import timezone


class VagaEmprego(models.Model):
    descricao = models.TextField(verbose_name="Descrição")
    foto = models.ImageField(upload_to='vagas/', null=True, blank=True, verbose_name="Foto")
    data_cadastro = models.DateTimeField(default=timezone.now, verbose_name="Data de Cadastro")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
    telefone_contato = models.CharField(max_length=20, verbose_name="Telefone de Contato")

    class Meta:
        verbose_name = "Vaga de Emprego"
        verbose_name_plural = "Vagas de Emprego"
        ordering = ['-data_cadastro']

    def __str__(self):
        return f"Vaga {self.id} - {self.telefone_contato}"