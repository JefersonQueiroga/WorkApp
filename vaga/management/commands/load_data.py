from django.core.management.base import BaseCommand
from vaga.models import VagaEmprego
from django.utils import timezone


class Command(BaseCommand):
    help = 'Carrega dados de exemplo para vagas de emprego'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Iniciando carga de dados...'))
        
        # Lista de vagas de exemplo
        vagas_exemplo = [
            {
                'descricao': 'Desenvolvedor Full Stack para atuar com Django e React. Experiência com APIs REST e banco de dados PostgreSQL. Regime CLT, trabalho híbrido. Benefícios: Vale alimentação, plano de saúde e home office flexível.',
                'telefone_contato': '(84) 98765-4321',
                'ativo': True,
            },
            {
                'descricao': 'Designer UX/UI para criação de interfaces modernas e responsivas. Conhecimento em Figma, Adobe XD e prototipagem. Portfólio obrigatório. Experiência com Design System será um diferencial.',
                'telefone_contato': '(84) 99876-5432',
                'ativo': True,
            },
            {
                'descricao': 'Analista de Marketing Digital para gerenciar campanhas de Google Ads e redes sociais. Experiência com métricas e análise de dados essencial. Conhecimento em SEO e ferramentas de analytics.',
                'telefone_contato': '(84) 97654-3210',
                'ativo': False,
            },
            {
                'descricao': 'Administrador de Banco de Dados (DBA) para gerenciar servidores MySQL e PostgreSQL. Conhecimento em otimização, backup e recuperação de dados essencial. Experiência com MongoDB será um plus.',
                'telefone_contato': '(84) 98123-4567',
                'ativo': True,
            },
            {
                'descricao': 'Analista de Segurança da Informação para implementar políticas de segurança e realizar auditorias. Certificação em segurança (CEH, CISSP) desejável. Experiência com pentest e análise de vulnerabilidades.',
                'telefone_contato': '(84) 99234-5678',
                'ativo': True,
            },
            {
                'descricao': 'Gerente de Projetos com experiência em metodologias ágeis (Scrum/Kanban). Certificação PMP será um diferencial. Liderança de equipes multidisciplinares e gestão de stakeholders.',
                'telefone_contato': '(84) 98345-6789',
                'ativo': True,
            },
            {
                'descricao': 'Desenvolvedor Mobile (React Native) para criar aplicativos iOS e Android. Conhecimento em integração com APIs, Firebase e publicação nas lojas. Experiência com testes automatizados.',
                'telefone_contato': '(84) 97890-1234',
                'ativo': True,
            },
            {
                'descricao': 'Analista de Suporte Técnico N2 para atendimento de chamados e resolução de problemas. Conhecimento em redes, Windows Server e Active Directory. Disponibilidade para trabalhar em escala.',
                'telefone_contato': '(84) 96789-0123',
                'ativo': False,
            },
            {
                'descricao': 'Product Owner com experiência em gestão de backlog e priorização de funcionalidades. Capacidade de traduzir necessidades de negócio em requisitos técnicos. Conhecimento do mercado tech.',
                'telefone_contato': '(84) 95678-9012',
                'ativo': True,
            },
            {
                'descricao': 'Engenheiro de Dados para construir pipelines de dados e ETL. Experiência com Python, Apache Airflow, Spark e cloud (AWS/Azure). Conhecimento em Data Lake e Data Warehouse.',
                'telefone_contato': '(84) 94567-8901',
                'ativo': True,
            },
            {
                'descricao': 'QA Automation Engineer para criar e manter testes automatizados. Conhecimento em Selenium, Cypress ou Playwright. Experiência com CI/CD e integração contínua.',
                'telefone_contato': '(84) 93456-7890',
                'ativo': True,
            },
            {
                'descricao': 'Desenvolvedor Backend Python/Django para APIs escaláveis. Conhecimento em arquitetura de microsserviços, Docker e Kubernetes. Experiência com bancos NoSQL será valorizada.',
                'telefone_contato': '(84) 92345-6789',
                'ativo': True,
            },
        ]

        # Limpar vagas existentes (opcional)
        if self.confirmar_limpeza():
            VagaEmprego.objects.all().delete()
            self.stdout.write(self.style.WARNING('Vagas antigas removidas.'))

        # Criar as vagas
        contador = 0
        for vaga_data in vagas_exemplo:
            vaga, created = VagaEmprego.objects.get_or_create(
                telefone_contato=vaga_data['telefone_contato'],
                defaults={
                    'descricao': vaga_data['descricao'],
                    'ativo': vaga_data['ativo'],
                    'data_cadastro': timezone.now(),
                }
            )
            
            if created:
                contador += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Vaga criada: {vaga.telefone_contato}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'→ Vaga já existe: {vaga.telefone_contato}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\n✓ Processo concluído! {contador} vagas criadas.')
        )

    def confirmar_limpeza(self):
        """Pergunta se deseja limpar os dados existentes"""
        resposta = input('\nDeseja limpar as vagas existentes antes de carregar? (s/N): ')
        return resposta.lower() in ['s', 'sim', 'y', 'yes']