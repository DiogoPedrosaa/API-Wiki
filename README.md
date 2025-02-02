Primeira avaliação da materia de desenvolvimento de API'S utilizando o django rest framework, quis fazer uma especie de wiki basica inspirada num jogo que sou fascinado, Elden Ring :)

# API-Wiki

O projeto [API-Wiki](https://github.com/DiogoPedrosaa/API-Wiki) é uma aplicação desenvolvida como parte da primeira avaliação da disciplina de Desenvolvimento de APIs, utilizando o Django Rest Framework.

Esta aplicação é inspirada no jogo Elden Ring e tem como objetivo fornecer uma wiki básica sobre o jogo.

## Funcionalidades

- **Gerenciamento de Itens**: Permite a criação, leitura, atualização e exclusão de informações relacionadas aos itens do jogo.
- **Gerenciamento de Monstros**: Facilita a administração dos dados referentes aos monstros presentes no jogo.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal do projeto.
- **Django**: Framework web utilizado para o desenvolvimento da aplicação.
- **Django Rest Framework**: Ferramenta para a construção de APIs RESTful robustas e eficientes.

## Estrutura do Projeto

A estrutura de diretórios do projeto é organizada da seguinte forma:

```
API-Wiki/
├── core/
├── env/
├── items/
├── monsters/
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

- **core/**: Contém configurações e componentes centrais da aplicação.
- **env/**: Diretório destinado ao ambiente virtual do Python.
- **items/**: Módulo responsável pelo gerenciamento dos itens do jogo.
- **monsters/**: Módulo dedicado ao controle das informações dos monstros.

## Instalação e Configuração

Para configurar o ambiente de desenvolvimento, siga os passos abaixo:

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/DiogoPedrosaa/API-Wiki.git
   cd API-Wiki
   ```

2. **Crie e ative um ambiente virtual**:

   ```bash
   python3 -m venv env
   source env/bin/activate  # No Windows, use 'env\Scripts\activate'
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações do banco de dados**:

   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor de desenvolvimento**:

   ```bash
   python manage.py runserver
   ```

A aplicação estará disponível em `http://127.0.0.1:8000/`.

## Uso

A API oferece endpoints para o gerenciamento de itens e monstros. Utilize ferramentas como [Postman](https://www.postman.com/) ou [cURL](https://curl.se/) para interagir com a API.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias ou correções.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais informações.

---

*Nota: Este projeto é uma implementação educacional e não está associado oficialmente ao jogo Elden Ring.*


