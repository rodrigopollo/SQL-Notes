## CREATE TABLE — Explicação Completa

**Tabela criada:** `account`
```
account (estrutura após o CREATE TABLE)
+------------+--------------+--------------------+
| coluna     | tipo         | restrições         |
+------------+--------------+--------------------+
| user_id    | SERIAL       | PRIMARY KEY        |
| username   | VARCHAR(50)  | NOT NULL           |
| password   | VARCHAR(50)  | NOT NULL           |
| email      | VARCHAR(250) | UNIQUE, NOT NULL   |
| created_on | TIMESTAMP    | NOT NULL           |
| last_login | TIMESTAMP    | (nenhuma)          |
+------------+--------------+--------------------+
```



### Query
```sql
CREATE TABLE account (
    user_id     SERIAL        PRIMARY KEY,
    username    VARCHAR(50)   NOT NULL,
    password    VARCHAR(50)   NOT NULL,
    email       VARCHAR(250)  UNIQUE NOT NULL,
    created_on  TIMESTAMP     NOT NULL,
    last_login  TIMESTAMP
);
```



### Resultado
```
account (pronta para receber dados)
+---------+----------+----------+-------+------------+------------+
| user_id | username | password | email | created_on | last_login |
+---------+----------+----------+-------+------------+------------+
| (vazia) |          |          |       |            |            |
+---------+----------+----------+-------+------------+------------+
```

---

A query cria a tabela `account` com 6 colunas, cada
uma com seu tipo de dado e restrições. A tabela nasce
vazia — sem nenhum dado. As restrições definidas aqui
são as regras que o banco vai aplicar em todo `INSERT`
ou `UPDATE` futuro. `user_id` é gerado automaticamente;
`last_login` é a única coluna opcional — um usuário
recém-criado ainda não fez login.



### O que cada parte faz

- `CREATE TABLE account` — cria uma nova tabela
  chamada `account` no banco de dados. Se já existir
  uma tabela com esse nome, o banco retorna erro.
  Para evitar o erro usar:
```sql
  CREATE TABLE IF NOT EXISTS account (...);
```

- `user_id SERIAL PRIMARY KEY`:
  - `SERIAL` — gera um número inteiro
    automaticamente a cada `INSERT`, incrementando
    em 1 (1, 2, 3...). Não precisa ser informado
    no `INSERT`.
  - `PRIMARY KEY` — define essa coluna como
    identificador único da tabela. Garante que
    nenhuma linha tenha o mesmo `user_id` e que
    o valor nunca seja `NULL`. Toda tabela deve
    ter uma `PRIMARY KEY`.

- `username VARCHAR(50) NOT NULL`:
  - `VARCHAR(50)` — texto de até 50 caracteres.
    Se o valor inserido ultrapassar o limite,
    o banco retorna erro.
  - `NOT NULL` — campo obrigatório. O banco
    rejeita qualquer `INSERT` que não informe
    este campo.

- `password VARCHAR(50) NOT NULL` — mesmo
  comportamento do `username`. Na prática real,
  senhas nunca são armazenadas como texto puro
  — passam por uma função de hash antes de
  serem salvas.

- `email VARCHAR(250) UNIQUE NOT NULL`:
  - `VARCHAR(250)` — texto de até 250 caracteres.
    E-mails podem ser longos, por isso o limite
    maior que `username`.
  - `UNIQUE` — garante que nenhum outro registro
    tenha o mesmo valor nessa coluna. Dois
    usuários não podem ter o mesmo e-mail.
  - `NOT NULL` — campo obrigatório.

- `created_on TIMESTAMP NOT NULL`:
  - `TIMESTAMP` — armazena data e hora juntas
    (ex: `2025-01-10 09:00:00`). Usado para
    registrar o momento exato de um evento.
  - `NOT NULL` — todo usuário deve ter uma
    data de cadastro.

- `last_login TIMESTAMP` — armazena data e hora
  do último acesso. Sem `NOT NULL` pois um usuário
  recém-criado ainda não fez login — o valor
  inicial é `NULL` (vazio).

---

### Com um INSERT nessa tabela ficaria
```sql
INSERT INTO account (
    username,
    password,
    email,
    created_on
)
VALUES (
    'Jose',
    '12345',
    'jose@mail.com',
    CURRENT_TIMESTAMP
);
```

```
+---------+----------+----------+---------------+---------------------+------------+
| user_id | username | password | email         | created_on          | last_login |
+---------+----------+----------+---------------+---------------------+------------+
|       1 | Jose     | 12345    | jose@mail.com | 2025-01-10 09:00:00 | NULL       |
+---------+----------+----------+---------------+---------------------+------------+
```

---

### Regras que o banco aplica automaticamente
```
user_id     → gerado pelo SERIAL (não informar)
username    → obrigatório (NOT NULL)
password    → obrigatório (NOT NULL)
email       → obrigatório e único
              (NOT NULL + UNIQUE)
created_on  → obrigatório (NOT NULL)
last_login  → opcional (aceita NULL)
```



### O que acontece se violar uma restrição
```sql
-- Tentando inserir e-mail duplicado (UNIQUE):
INSERT INTO account (username, password,
email, created_on)
VALUES ('Maria', 'abcde',
'jose@mail.com', CURRENT_TIMESTAMP);

ERROR: duplicate key value violates unique
constraint "account_email_key"
DETAIL: Key (email)=(jose@mail.com)
already exists.

-- Tentando inserir sem username (NOT NULL):
INSERT INTO account (password, email,
created_on)
VALUES ('abcde', 'maria@mail.com',
CURRENT_TIMESTAMP);

ERROR: null value in column "username"
violates not-null constraint
```