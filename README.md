# 25Books - API de Sistema de Gerenciamento de Biblioteca

Esta é a API de um sistema de gerenciamento de biblioteca desenvolvido utilizando Python e Flask. A seguir está uma descrição detalhada das funcionalidades oferecidas por esta API, que segue o padrão REST.

## Funcionalidades

### Usuários

- **Criar Usuário**: Permite adicionar um novo usuário ao sistema.
- **Deletar Usuário**: Permite remover um usuário existente do sistema.
- **Atualizar Usuário**: Permite atualizar as informações de um usuário existente no sistema.

### Livros

- **Criar Livro**: Permite adicionar um novo livro ao catálogo da biblioteca.
- **Deletar Livro**: Permite remover um livro existente do catálogo da biblioteca.
- **Atualizar Livro**: Permite atualizar as informações de um livro existente no catálogo da biblioteca.
- **Buscar Livro por Autor**: Permite buscar livros no catálogo pelo nome do autor.
- **Buscar Livro por Nome**: Permite buscar livros no catálogo pelo nome do livro.

### Empréstimos

- **Criar Empréstimo**: Permite registrar o empréstimo de um livro para um usuário.
- **Deletar Empréstimo**: Permite cancelar o empréstimo de um livro.
- **Atualizar Empréstimo**: Permite atualizar as informações de um empréstimo existente.

### Funções Específicas

- **Emprestar Livro**: Permite emprestar um livro para um usuário. Um livro só pode ser emprestado para uma pessoa por vez.
- **Restrição de Deleção**: Um livro que esteja emprestado não pode ser deletado do catálogo da biblioteca.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para implementar a lógica da API.
- **Flask**: Framework web utilizado para criar a API REST.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) e enviar pull requests para melhorar esta API de sistema de gerenciamento de biblioteca.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
