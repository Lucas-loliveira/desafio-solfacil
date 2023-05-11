# Desafio Solfácil
Autor da solução: Lucas da Silva de Oliveira (lucasoliveira783@gmail.com, https://www.linkedin.com/in/lucas-sil-oliveira)

## Apresentação do problema

Nosso cliente interno precisa atualizar rotineiramente os dados de nossos parceiros. O problema acontece que para atualizar, ele precisa entrar na página de edição de cada um dos parceiros. Isso é um trabalho muito tedioso e demorado.

Precisamos dar uma solução para este problema!

Nossa equipe de produtos pensou que poderíamos fazer uma atualização em lote através de um CSV.

[Baixe aqui um CSV de exemplo](assets/exemplo.csv)


## Tecnologias usadas

  * python3
  * django 4.2
  * django-rest framework
  * PostgreSQL
 
Requisitos
============
  * [docker](https://www.docker.com/)
  * [docker-compose](https://docs.docker.com/compose/)

Como executar a aplicação
============

### Execute os containers
```bash
$ make build up
```

### Execute as migrações
```bash
$ make migrate
```

Testes
=====

```bash
$ make test
```

Documentação (local)
=====
http://0.0.0.0:8000/docs/

Página HTML para upload de arquivos (local)
=====
[http://0.0.0.0:8000/docs/](http://0.0.0.0:8000/upload/)


Futuras melhorias
=====
  * Preparar projeto para deploy, adicionando .env e guardando variaveis sensiveis. criar pipelines de CI/CD;
  * Paginação na listagem de parceiros;
  * Alterar a arquitetura de acordo com a necessidade. A aplicação atual é suficiente para o upload de arquivo pequenos (ainda é necessario realizar testes de carga da aplicação para explorar esses limites). Em um contexto de na qual forem necessarios o upload de arquivos de arquivos de grande porte, é necessario a alteracao na arquitetura da aplicação, uma sugestao é apresentada no artigo [Run Celery workers for compute-intensive tasks with AWS Batch](https://aws.amazon.com/pt/blogs/hpc/run-celery-workers-for-compute-intensive-tasks-with-aws-batch/)


