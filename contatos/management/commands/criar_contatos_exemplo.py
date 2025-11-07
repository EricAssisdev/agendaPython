from django.core.management.base import BaseCommand
from contatos.models import Contato
from datetime import date

class Command(BaseCommand):
    help = 'Cria contatos de exemplo para testar a aplicação'

    def handle(self, *args, **kwargs):
        # Limpar contatos existentes (opcional)
        # Contato.objects.all().delete()
        
        contatos_exemplo = [
            {
                'nome': 'Maria Silva',
                'email': 'maria.silva@email.com',
                'celular': '+5511987654321',
                'categoria': 'familia',
                'empresa': 'Silva & Filhos',
                'cargo': 'Gerente',
                'favorito': True,
                'aniversario': date(1990, 3, 15),
                'observacoes': 'Prima querida, sempre disponível para ajudar.',
            },
            {
                'nome': 'João Santos',
                'email': 'joao.santos@techcorp.com',
                'celular': '+5511976543210',
                'telefone': '+551133334444',
                'categoria': 'trabalho',
                'empresa': 'TechCorp Brasil',
                'cargo': 'Desenvolvedor Senior',
                'endereco': 'Av. Paulista, 1000 - São Paulo, SP',
                'aniversario': date(1988, 7, 22),
                'favorito': True,
            },
            {
                'nome': 'Ana Paula Costa',
                'email': 'ana.costa@gmail.com',
                'celular': '+5511965432109',
                'categoria': 'amigo',
                'aniversario': date(1995, 11, 8),
                'observacoes': 'Melhor amiga desde o colégio. Adora viajar!',
                'favorito': False,
            },
            {
                'nome': 'Carlos Eduardo',
                'email': 'carlos.edu@email.com',
                'celular': '+5511954321098',
                'categoria': 'outros',
                'empresa': 'Freelancer',
                'observacoes': 'Designer gráfico. Contato para projetos.',
            },
            {
                'nome': 'Fernanda Oliveira',
                'email': 'fe.oliveira@empresa.com',
                'celular': '+5511943210987',
                'telefone': '+551122223333',
                'categoria': 'trabalho',
                'empresa': 'Empresa ABC',
                'cargo': 'Analista de Marketing',
                'endereco': 'Rua Augusta, 500 - São Paulo, SP',
                'favorito': False,
            },
            {
                'nome': 'Roberto Alves',
                'email': 'roberto.alves@email.com',
                'celular': '+5511932109876',
                'categoria': 'familia',
                'aniversario': date(1975, 5, 30),
                'observacoes': 'Tio Roberto - sempre conta histórias engraçadas.',
                'favorito': True,
            },
            {
                'nome': 'Patricia Mendes',
                'email': 'patricia.m@consulting.com',
                'celular': '+5511921098765',
                'categoria': 'trabalho',
                'empresa': 'Mendes Consulting',
                'cargo': 'CEO',
                'endereco': 'Av. Faria Lima, 2000 - São Paulo, SP',
                'aniversario': date(1982, 9, 12),
            },
            {
                'nome': 'Lucas Ferreira',
                'email': 'lucas.ferreira@hotmail.com',
                'celular': '+5511910987654',
                'categoria': 'amigo',
                'observacoes': 'Parceiro de academia. Gosta de futebol.',
                'favorito': False,
            },
            {
                'nome': 'Juliana Rodrigues',
                'email': 'ju.rodrigues@email.com',
                'celular': '+5511909876543',
                'categoria': 'familia',
                'aniversario': date(1992, 12, 25),
                'observacoes': 'Irmã mais nova. Estudante de medicina.',
                'favorito': True,
            },
            {
                'nome': 'Rafael Souza',
                'email': 'rafael.souza@startup.io',
                'celular': '+5511998765432',
                'telefone': '+551144445555',
                'categoria': 'trabalho',
                'empresa': 'Startup Innovation',
                'cargo': 'CTO',
                'endereco': 'Rua dos Pinheiros, 800 - São Paulo, SP',
                'favorito': False,
            },
        ]
        
        created_count = 0
        for dados in contatos_exemplo:
            contato, created = Contato.objects.get_or_create(
                email=dados.get('email'),
                defaults=dados
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'✓ Criado: {contato.nome}'))
            else:
                self.stdout.write(self.style.WARNING(f'○ Já existe: {contato.nome}'))
        
        self.stdout.write(self.style.SUCCESS(f'\n{created_count} contatos de exemplo criados com sucesso!'))
        self.stdout.write(self.style.SUCCESS(f'Total de contatos no banco: {Contato.objects.count()}'))
