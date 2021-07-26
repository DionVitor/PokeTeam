<h1 align="center">PokeTeam</h1>
<p align="center"> API de gerenciamento de time pokemon. </p>

<p align="center">
  <a>
    <img src="https://img.shields.io/badge/progress-100%25-brightgreen.svg" alt="progress">
  </a>
  <a>
    <img src="https://img.shields.io/badge/contribuition-welcome-brightgreen.svg" alt="contribution">
  </a>
  <a>
    <img src="https://img.shields.io/badge/version-1.0-brightgreen.svg" alt="version">
  </a>
</p>

[English](https://github.com/DionVitor/PokeTeam/) | Português

## :package: Instruções para rodar o app

- Instale o docker e compose [aqui](https://docs.docker.com/engine/install/)
- Clone o repositório ```git clone https://github.com/DionVitor/PokeTeam/```
- Vá para o repositório ```cd PokeTeam/```
- Crie os containers ```make start```
- Crie as tabelas no banco de dados ```make migrate```

## :keyboard: Como usar a api

- Entre na [documentação swagger](http://localhost:8000/swagger/)
- Registre seu usuário : ```/register```
- Login com seu usuário: ```/accounts/login``` ou no botão "Log in" no swagger
- Crie, delete ou visualize seu time: ```/manipulate_team```
- Procure pokemons para adicionar em seu time: ```/search_pokemon```
- Adicione ou remova pokemons do seu time: ```/pokemon_team```
- Para logout: ```/accounts/logout``` ou no botão "Django Logout" no swagger

## :heavy_check_mark: Patterns no projeto

- Clean Architecture
- MTV
- REST
- Repository Pattern

## :hammer: Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [PokeAPI](https://pokeapi.co)
- [PostgreSQL](https://www.postgresql.org/)

## :smile: Author

Feito por Dion Vítor, contatos:

[![Gmail Badge](https://img.shields.io/badge/-dionvictor11@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:dionvictor11@gmail.com)](mailto:dionvictor11@gmail.com)
[![WhatsApp Badge](https://img.shields.io/badge/-WhatsApp-green?style=flat-square&logo=WhatsApp&logoColor=white&link=https://api.whatsapp.com/send?phone=5561998822233)](https://api.whatsapp.com/send?phone=5561998822233)
[![Linkedin Badge](https://img.shields.io/badge/-Dion%20V%C3%ADtor-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/dion-v%C3%ADtor-a519631aa/)](https://www.linkedin.com/in/dion-v%C3%ADtor-a519631aa/)
