CREATE TABLE
    -> comando usado para criar uma tabela no banco de dados

* account
    -> nome da tabela
    -> poderia ser qualquer outro nome
    -> exemplos:
        - users
        - clientes
        - pagamentos
        - estoque

* () -> dentro dos parenteses ficam todas as colunas da tabela

    --------------------------------------------------
                    COLUNA: user_id
    --------------------------------------------------

* user_id
    -> nome da coluna

* SERIAL
    -> tipo especial usado para criar numeros automaticamente
    -> geralmente usado para IDs
    -> cada novo registro recebe um numero automatico

    EXEMPLO:
        1
        2
        3
        4

* PRIMARY KEY
    -> chave primaria da tabela (Primary Key)

    SIGNIFICA:
        - identifica cada linha de forma unica
        - nao pode repetir
        - nao pode ser NULL

    EXEMPLO:
        CERTO:
            1
            2
            3

        ERRADO:
            1
            1  <-- repetido

    --------------------------------------------------
                    COLUNA: username
    --------------------------------------------------

* username
    --> nome da coluna

* VARCHAR(50)
    --> tipo texto (string) e com maximo de 50 caracteres

    SIGNIFICA:
        - pode armazenar letras, numeros e simbolos
        - o numero 50 eh o limite maximo de caracteres

    EXEMPLO:
        'Rodrigo'
        'Maria123'

* UNIQUE
    --> nao permite valores repetidos

* NOT NULL
    --> a coluna nao pode ficar vazia, ou seja, obrigatorio preencher

    SIGNIFICA:
        ERRADO:
            NULL

        CERTO:
            'Rodrigo'

    --------------------------------------------------
                    COLUNA: password
    --------------------------------------------------

* password
    --> nome da coluna

* VARCHAR(50)
    --> coluna de texto com maximo de 50 caracteres

* NOT NULL
    --> obrigatorio preencher

    --------------------------------------------------
                    COLUNA: email
    --------------------------------------------------

* email
    --> nome da coluna

* VARCHAR(250)
    --> texto com maximo de 250 caracteres

* UNIQUE
    --> nao permite valores repetidos

    EXEMPLO:

        CERTO:
            rodrigo@gmail.com
            maria@gmail.com

        ERRADO:
            rodrigo@gmail.com
            rodrigo@gmail.com  <-- repetido

* NOT NULL
    --> obrigatorio preencher

    --------------------------------------------------
                    COLUNA: created_on
    --------------------------------------------------

* created_on
    --> nome da coluna

* TIMESTAMP
    --> guarda data e hora

    EXEMPLO:
        2026-05-21 14:30:00

* NOT NULL
    --> obrigatorio preencher

    --------------------------------------------------
                    COLUNA: last_login
    --------------------------------------------------

* last_login
    --> nome da coluna

* TIMESTAMP
    --> guarda data e hora do ultimo login

    EXEMPLO:
        2026-05-21 18:40:22

* sem NOT NULL
    --> significa que pode ficar vazio (NULL)

    ISSO EH UTIL porque:
        - talvez o usuario nunca tenha feito login ainda


    --------------------------------------------------
               RESULTADO FINAL DA TABELA
    --------------------------------------------------

| user_id | username | password | email           | created_on          | last_login          |
|---------|----------|----------|-----------------|---------------------|---------------------|
| 1       | Rodrigo  | 12345    | ro@gmail.com    | 2026-05-21 10:00:00 | 2026-05-21 18:00:00 |
| 2       | Maria    | abc123   | maria@gmail.com | 2026-05-21 11:00:00 | NULL                |