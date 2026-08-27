## ALTER TABLE — Como adicionar uma nova coluna a uma tabela existente?

**Tabela utilizada:** `account`

```
account (antes do ADD COLUMN)
+---------+----------+----------+---------------------+
| user_id | username | password | created_on          |
+---------+----------+----------+---------------------+
|       1 | Jose     | 12345    | 2025-01-10 09:00:00 |
|       2 | Maria    | abcde    | 2025-03-22 14:00:00 |
|       3 | Carlos   | qwerty   | 2025-07-05 11:00:00 |
+---------+----------+----------+---------------------+
```


### Query
```sql
ALTER TABLE account
ADD COLUMN age INTEGER CHECK (age >= 0);
```


### Resultado
```
account (depois do ADD COLUMN)
+---------+----------+----------+---------------------+-----+
| user_id | username | password | created_on          | age |
+---------+----------+----------+---------------------+-----+
|       1 | Jose     | 12345    | 2025-01-10 09:00:00 | NULL|
|       2 | Maria    | abcde    | 2025-03-22 14:00:00 | NULL|
|       3 | Carlos   | qwerty   | 2025-07-05 11:00:00 | NULL|
+---------+----------+----------+---------------------+-----+
```

---

A query adicionou a coluna `age` à tabela `account`.
Como os registros já existiam antes da coluna ser
criada, todos receberam `NULL` automaticamente —
o banco não tem como saber a idade de cada usuário.
O `CHECK (age >= 0)` garante que nenhuma idade
negativa seja inserida no futuro. A nova coluna
fica disponível imediatamente para `INSERT` e
`UPDATE`.



### O que cada parte faz

- `ALTER TABLE account` — seleciona a tabela
  que será modificada.

- `ADD COLUMN age` — **novo:** adiciona uma nova
  coluna chamada `age` à tabela. A coluna é
  inserida ao final da tabela, após todas as
  colunas já existentes.

- `INTEGER` — tipo de dado da nova coluna.
  Aceita números inteiros.

- `CHECK (age >= 0)` — restrição adicionada
  junto com a coluna, impedindo que idades
  negativas sejam inseridas. Funciona igual
  ao `CHECK` visto no `CREATE TABLE`.



### Adicionando coluna com DEFAULT
```sql
-- Sem DEFAULT → registros existentes recebem NULL:
ALTER TABLE account
ADD COLUMN age INTEGER;

-- Com DEFAULT → registros existentes recebem
-- o valor padrão definido:
ALTER TABLE account
ADD COLUMN age INTEGER DEFAULT 0;
```

---

### Preenchendo a nova coluna após adicionar
```sql
-- Após o ADD COLUMN, atualizar os valores
-- com UPDATE:
UPDATE account
SET age = 30
WHERE user_id = 1;

UPDATE account
SET age = 25
WHERE user_id = 2;

UPDATE account
SET age = 35
WHERE user_id = 3;
```