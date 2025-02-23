# Testes Automatizados para Autenticação

Este repositório contém os testes automatizados para a funcionalidade de autenticação do nosso sistema. Os testes foram desenvolvidos usando o framework de testes do Django (`TestCase`).

## Funcionalidades Testadas

* Login de usuário (sucesso e falha)
* Registro de usuário (validação de nome de usuário duplicado)

## Tecnologias

* Python
* Django
* unittest (framework de testes do Django)

## Pré-requisitos

* Python 3.x instalado
* Django instalado
* Ambiente virtual (recomendado)

## Configuração

1.  Clone este repositório:

    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <DIRETORIO_DO_REPOSITORIO>
    ```

2.  Crie e ative um ambiente virtual (recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/macOS
    venv\Scripts\activate  # No Windows
    ```

3.  Instale as dependências:

    ```bash
    pip install -r requirements.txt #Caso tenha um arquivo requirements.txt
    ```

4.  Execute as migrations do Django:

    ```bash
    python manage.py migrate
    ```

## Executando os Testes

Para executar os testes, utilize o seguinte comando:

```bash
python manage.py test accounts
