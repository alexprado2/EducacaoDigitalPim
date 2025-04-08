## Sobre o projeto

Este projeto é um sistema simples de gerenciamento de livros, implementado como um **CRUD** (Create, Read, Update, Delete) com funcionalidades essenciais para cadastro e manutenção de livros em uma biblioteca ou acervo pessoal. O sistema utiliza um arquivo JSON `(books.json)` para armazenar os dados e fornece uma interface de linha de comando `(CLI)` para interação.

<!-- 
![hero-image]
-->

### Features

- **Interface de Linha de Comando (CLI):** O sistema oferece um menu interativo simples, facilitando o uso mesmo para iniciantes.
- **Geração Automática de IDs:** Cada livro recebe um ID único automaticamente ao ser registrado no sistema, garantindo a integridade dos dados.
- **Armazenamento em JSON:** Todos os dados dos livros são armazenados em um arquivo `books.json`, proporcionando fácil manipulação e persistência. 
- **Registro de Data:** O sistema registra automaticamente a data de cadastro e atualização de cada livro.

### Construído com

![badge-phyton]
![badge-json]
![badge-visual-studio]


## Getting Started

Para obter uma cópia local funcionando, siga estes passos simples.

### Requisitos

* Visual Studio code versão 2022+ 
* Windows 10+ ou Linux/MacOS com [Python SDK][python-sdk] instalado

### Instalação

1. Clone o repositório:
    ```sh
    gh repo clone alexprado2/EducacaoDigitalPim
    ```

2. Entre na pasta do projeto com o comando: `cd educacaoDigital/src`.
3. Execute o projeto com: `python main.py`.
4. Execute o projeto e aproveite o seu teste :)



<!-- Links -->
[python-sdk]: https://www.python.org/downloads/

<!-- Images 
[hero-image]: images/heroimage.png
 -->

<!-- Badges -->
[badge-phyton]: https://img.shields.io/badge/Python-black?style=for-the-badge&logo=python
[badge-visual-studio]: https://img.shields.io/badge/VISUAL%20STUDIO%20CODE-blue?style=for-the-badge
[badge-json]: https://img.shields.io/badge/Json-blue?style=for-the-badge&logo=json

