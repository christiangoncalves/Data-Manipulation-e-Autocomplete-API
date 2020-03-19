# Api Autocomplete

Para executar esse projeto foi usado o "pipenv" para fazer gerenciamentos de dependencias

Essa api foi feita utilizando os seguintes plugins para o Python:

- Flask
- flask_sqlalchemy
- flask_migrate
- flask_marshmallow
- marshmallow_sqlalchemy
É DE EXTREMA IMPORTANCIA A INSTALAÇÃO DOS PLUGINS PARA O FUNCIONAMENTO DA APLICAÇÃO

Antes de rodar esse aplicativo sera necessario alterar uma Variavel de sistema para que o Flask consiga rodar o projeto de maneira correta para isso execute no Terminal/CMD o seguinte comando:

- WINDOWS:
```sh

set FLASK_APP=app

```

- LINUX
```sh

export FLASK_APP=app

```

Apos a configuração da variavel de ambiente do Flask basta somente executar o comando de inicialização para subir a aplicação:

```sh

flask run

```

Para fazer as migrações do Banco de Dados caso necessario, execute os comandos:

```sh

flask db init
flask db migrate
flask db upgrade

```

O banco utilizado foi o sqlite fornecido pelo flask_sqlalchemy e o mesmo se encontra na pasta 'app' ja populado

As rotas para dessa api são:

```sh

'/' ('pagina inicial do auto complete com formulario para testes')
GET: '/mostrar' ('Retorna um JSON com todos os registros do Banco')
POST: '/cadastrar' ('Recebe o JSON modelo e cria um registro do mesmo no Banco')
GET: '/deletar/<id>' ('Deleta do Banco o registo com id= <id>')
POST: '/modificar/<id>' ('Altera no banco o registo com id= <id> inserindo no lugar o JSON enviado')
POST: '/autocomplete' ('função de autocomplete em si, ROTA É UTILIZADA NA PAGINA INICIAL DA ROTA (/)')
POST: '/autocompletejson' ('Rota similar a anterior, porem essa recebe no corpo da requisição um JSON e nao um FORM, sendo melhor para testes posteriores)

```
