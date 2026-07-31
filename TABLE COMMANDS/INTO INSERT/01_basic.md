## INSERT INTO — Como inserir um novo registro em uma tabela?


### Query
```sql
INSERT INTO account (
    username,
    password,
    email,
    created_on
)
VALUES
    ('Jose', '12345', 'jose@mail.com', CURRENT_TIMESTAMP);
```


### Resultado — linha inserida na tabela account
```
+---------+----------+-------+---------------+---------------------+------------+
| user_id | username | pass  | email         | created_on          | last_login |
+---------+----------+-------+---------------+---------------------+------------+
|       1 | Jose     | 12345 | jose@mail.com | 2025-09-29 14:37:52 | NULL       |
+---------+----------+-------+---------------+---------------------+------------+
```

---


A query adiciona 1 nova linha na tabela `account`. As
colunas não mencionadas (`user_id`, `last_login`) foram
preenchidas automaticamente pelo banco: `user_id` recebeu
o próximo valor da sequência `SERIAL`, e `last_login`
recebeu `NULL` pois não tem `DEFAULT` definido e não
foi informada. O `INSERT` sempre cria uma linha inteira
— mesmo que só algumas colunas sejam mencionadas, todas
as colunas da tabela recebem algum valor.



### O que cada parte faz

- `INSERT INTO account (...)` — seleciona a tabela
  `account` como destino da inserção. Entre parênteses
  vão as colunas que receberão valores explícitos,
  na ordem que preferir.

- `(username, password, email, created_on)` — lista
  das colunas que serão preenchidas. As colunas não
  listadas recebem automaticamente:
  - `SERIAL` → próximo número da sequência
  - `DEFAULT` → valor padrão definido na criação
  - Sem nenhum dos dois → `NULL`

- `VALUES (...)` — os valores a serem inseridos,
  na **mesma ordem** das colunas listadas acima.
  O primeiro valor vai para a primeira coluna, o
  segundo para a segunda, e assim por diante.

- `'Jose'`, `'12345'`, `'jose@mail.com'` — strings
  (texto), que **obrigatoriamente** vão entre aspas
  simples. Nunca aspas duplas no PostgreSQL.

- `CURRENT_TIMESTAMP` — não vai entre aspas pois não
  é um texto — é uma função do banco que retorna a
  data e hora atuais. O mesmo vale para números
  inteiros, `TRUE`, `FALSE` e `NULL`.




### Regra de indentação
```sql
-- ATÉ 4 colunas → pode ficar em uma linha:
INSERT INTO account (username, password, email, created_on)
VALUES ('Jose', '12345', 'jose@mail.com', CURRENT_TIMESTAMP);

-- 5 OU MAIS colunas → modo vertical obrigatório:
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


### O que precisa de aspas simples e o que não precisa
```
COM aspas simples:
  texto / string   → 'Jose', 'jose@mail.com'
  datas manuais    → '2025-09-29'

SEM aspas simples:
  inteiros         → 1, 42, 100
  decimais         → 10.99
  booleanos        → TRUE, FALSE
  nulo             → NULL
  funções do banco → CURRENT_TIMESTAMP, NOW()
```