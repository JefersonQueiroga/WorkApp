from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Cria os grupos (papéis) de usuários do sistema: GERENTE e USUARIO_SIMPLES'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('=' * 70))
        self.stdout.write(self.style.WARNING('Iniciando carga de grupos de usuários...'))
        self.stdout.write(self.style.WARNING('=' * 70))
        
        # Lista de grupos para criar
        grupos = ['GERENTE', 'USUARIO_SIMPLES']
        
        grupos_criados = []
        grupos_existentes = []
        
        # Criar cada grupo
        for nome_grupo in grupos:
            grupo, created = Group.objects.get_or_create(name=nome_grupo)
            
            if created:
                grupos_criados.append(nome_grupo)
                self.stdout.write(
                    self.style.SUCCESS(f'   ✓ Grupo "{nome_grupo}" criado com sucesso!')
                )
            else:
                grupos_existentes.append(nome_grupo)
                self.stdout.write(
                    self.style.WARNING(f'   → Grupo "{nome_grupo}" já existe')
                )
        
        # ==================================================
        # RESUMO FINAL
        # ==================================================
        self.stdout.write('\n' + '=' * 70)
        self.stdout.write(self.style.SUCCESS('✓ PROCESSO CONCLUÍDO!'))
        self.stdout.write('=' * 70)
        
        self.stdout.write('\n📊 RESUMO:\n')
        
        if grupos_criados:
            self.stdout.write(f'   ✓ Grupos criados: {", ".join(grupos_criados)}')
        
        if grupos_existentes:
            self.stdout.write(f'   → Grupos já existentes: {", ".join(grupos_existentes)}')
        
        self.stdout.write(f'\n   📌 Total de grupos no sistema: {Group.objects.count()}')
        
        # Listar todos os grupos
        self.stdout.write('\n📋 GRUPOS CADASTRADOS NO SISTEMA:\n')
        
        self.stdout.write('┌' + '─' * 68 + '┐')
        self.stdout.write(f'│ {"ID":<5} │ {"NOME DO GRUPO":<58} │')
        self.stdout.write('├' + '─' * 68 + '┤')
        
        for grupo in Group.objects.all().order_by('name'):
            self.stdout.write(f'│ {grupo.id:<5} │ {grupo.name:<58} │')
        
        self.stdout.write('└' + '─' * 68 + '┘')
        
        self.stdout.write('\n💡 PRÓXIMOS PASSOS:\n')
        self.stdout.write('   1. Para atribuir um usuário a um grupo:')
        self.stdout.write('      → Acesse o Django Admin (http://localhost:8000/admin/)')
        self.stdout.write('      → Vá em "Usuários" > Selecione o usuário')
        self.stdout.write('      → Na seção "Permissões", adicione aos "Grupos"\n')
        
        self.stdout.write('   2. Ou crie usuários de exemplo com grupos:')
        self.stdout.write('      → Execute: python manage.py load_usuarios_exemplo\n')
        
        self.stdout.write('=' * 70 + '\n')