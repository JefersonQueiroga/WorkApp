# WorkApp

Sistema de gerenciamento de vagas de emprego desenvolvido em Django.

## Tecnologias

- Django 5.2.6
- Bootstrap 5
- SQLite3
- Python 3.x

## Instalação

1. **Clone o repositório**

2. **Crie e ative o ambiente virtual**:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

4. **Execute as migrações**:
```bash
python manage.py migrate
```

5. **Crie um superusuário**:
```bash
python manage.py createsuperuser
```

6. **Carregue dados de exemplo** (opcional):
```bash
python manage.py load_data
```

7. **Inicie o servidor**:
```bash
python manage.py runserver
```

8. **Acesse**:
- Sistema: http://localhost:8000/
- Admin: http://localhost:8000/admin/

## Funcionalidades

- Cadastro e gerenciamento de vagas
- Sistema de autenticação
- Interface responsiva
- Upload de fotos
- Status ativo/inativo

---

**IFRN - Programação para Internet -  2025**