# Flix API RESTful


## 🎬 API de Catálogo de Filmes

Uma API RESTful desenvolvida com Django Rest Framework (DRF) que permite gerenciar filmes, atores, gêneros e avaliações (reviews).
O projeto utiliza autenticação JWT e controle de permissões baseado em grupos de usuários.

## 🚀 Funcionalidades

👤 Atores – Cadastro e listagem de atores.

🎭 Gêneros – Organização dos filmes por gênero.

🎥 Filmes – Informações detalhadas de cada filme.

⭐ Reviews – Avaliações com comentários e notas de 1 a 5 estrelas.

🔐 Autenticação JWT – Login seguro com geração de tokens.

⚙️ Controle de permissões – Diferentes níveis de acesso via grupos de usuários.


## 📦 Tecnologias Utilizadas

Python 3.x

Django 4.x

Django REST Framework

SimpleJWT

## 🛠️ Instalação e Configuração

Clone o repositório
```
git clone https://github.com/seu-usuario/flix-api.git
cd flix-api
```

Crie e ative um ambiente virtual
```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

Instale as dependências

```
pip install -r requirements.txt
```

Aplique as migrações
```
python manage.py migrate
```

Crie um superusuário
```
python manage.py createsuperuser
```
Execute o servidor
```
python manage.py runserver
```

## 🔐 Autenticação (JWT)

Obter token de acesso

```
POST /api/v1/authentication/token/
{
    "username": "seu_usuario",
    "password": "sua_senha"
}
```
Resposta:
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOi...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOi..."
}
```
Atualizar token
POST /api/v1/authentication/token/refresh/
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOi..."
}
```

## 📌 Endpoints Principais

🎭 Gêneros

GET POST /api/v1/genre/ → Lista e cria gêneros

PUT PATCH DEL /api/v1/genre/ID → Edita, Visualiza e deleta gênero

👤 Atores

GET POST /api/v1/actors/ → Lista e cria atores

PUT PATCH DEL /api/v1/actors/ID → Edita, Visualiza e deleta atores

🎥 Filmes

GET POST /api/v1/movie/ → Lista e cria filmes

PUT PATCH DEL /v1/movie/ID → Edita, Visualiza e deleta filme

⭐ Reviews

GET POST /v1/review/ → Lista e cria avaliações

PUT PATCH DEL  /api/v1/review/ID → Edita, Visualiza e deleta avaliação


## 🧪 Exemplo de Requisição

Filme

```
    {
        "id": 1,
        "rate": 2.9,
        "title": "Titanic",
        "release_date": "1975-01-01",
        "resume": "Titanic é um filme épico de romance e drama norte-americano de 1997, escrito, dirigido, co-produzido e co-editado por James Cameron. É uma história de ficção do naufrágio real do RMS Titanic, estrelando Leonardo DiCaprio como Jack Dawson, e Kate Winslet como Rose DeWitt Bukater, membros de diferentes classes sociais que se apaixonam durante a fatídica viagem inaugural no navio saindo de Southampton para Nova Iorque em 15 de abril de 1912. Apesar dos personagens principais serem fictícios, alguns personagens são figuras históricas. Gloria Stuart interpreta Rose idosa, que narra o filme, enquanto Billy Zane interpreta Cal Hockley, o arrogante noivo rico da jovem Rose. Cameron viu a história de amor como um jeito de cativar o público para o desastre real.",
        "genre": 2,
        "actors": [
            1,
            4
        ]
    }
```