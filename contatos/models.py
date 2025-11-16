from django.db import models
from django.core.validators import RegexValidator

class Contato(models.Model):
    CATEGORIAS = [
        ('familia', 'Família'),
        ('amigo', 'Amigo'),
        ('trabalho', 'Trabalho'),
        ('outros', 'Outros'),
    ]
    
    nome = models.CharField(max_length=200, verbose_name='Nome Completo')
    email = models.EmailField(blank=True, null=True, verbose_name='E-mail')
    
    telefone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="O telefone deve estar no formato: '+999999999'. Até 15 dígitos permitidos."
    )
    telefone = models.CharField(
        validators=[telefone_regex],
        max_length=17,
        blank=True,
        null=True,
        verbose_name='Telefone'
    )
    
    celular = models.CharField(
        validators=[telefone_regex],
        max_length=17,
        blank=True,
        null=True,
        verbose_name='Celular'
    )
    
    endereco = models.TextField(blank=True, null=True, verbose_name='Endereço')
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS,
        default='outros',
        verbose_name='Categoria'
    )
    
    empresa = models.CharField(max_length=200, blank=True, null=True, verbose_name='Empresa')
    cargo = models.CharField(max_length=200, blank=True, null=True, verbose_name='Cargo')
    aniversario = models.DateField(blank=True, null=True, verbose_name='Aniversário')
    observacoes = models.TextField(blank=True, null=True, verbose_name='Observações')
    
    favorito = models.BooleanField(default=False, verbose_name='Favorito')
    
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
    
    def __str__(self):
        return self.nome
    
    def get_iniciais(self):
        """Retorna as iniciais do nome para o avatar"""
        nomes = self.nome.split()
        if len(nomes) >= 2:
            return f"{nomes[0][0]}{nomes[-1][0]}".upper()
        return self.nome[0].upper() if self.nome else "?"
