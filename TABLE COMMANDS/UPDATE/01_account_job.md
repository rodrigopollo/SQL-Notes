## UPDATE — Como atualizar um valor usando dados de outra tabela?

**Tabelas utilizadas:** `account_job`, `account`

```
account
+---------+----------+---------------------+
| user_id | username | created_on          |
+---------+----------+---------------------+
|       1 | Jose     | 2025-01-10 09:00:00 |
|       2 | Maria    | 2025-03-22 14:00:00 |
|       3 | Carlos   | 2025-07-05 11:00:00 |
+---------+----------+---------------------+

account_job (antes do UPDATE)
+---------+--------+------------+
| user_id | job_id | hire_date  |
+---------+--------+------------+
|       1 |    101 | NULL       |
|       2 |    102 | NULL       |
|       3 |    101 | NULL       |
+---------+--------+------------+
```



### Query
```sql
UPDATE account_job
SET
    hire_date = account.created_on
FROM account
WHERE
    account_job.user_id = account.user_id;
```



### Resultado — account_job após o UPDATE
```
+---------+--------+---------------------+
| user_id | job_id | hire_date           |
+---------+--------+---------------------+
|       1 |    101 | 2025-01-10 09:00:00 |
|       2 |    102 | 2025-03-22 14:00:00 |
|       3 |    101 | 2025-07-05 11:00:00 |
+---------+--------+---------------------+
```

---

A query atualizou a coluna `hire_date` de todos os
registros em `account_job`, usando como valor a data
de criação (`created_on`) do usuário correspondente
em `account`. Antes do `UPDATE` todos os `hire_date`
eram `NULL`. O `WHERE` garantiu que cada linha de
`account_job` recebesse o `created_on` do seu
próprio usuário — não de qualquer usuário.



### O que cada parte faz

- `UPDATE account_job` — seleciona a tabela que será
  modificada. Os dados alterados ficam aqui.

- `SET hire_date = account.created_on` — define qual
  coluna será alterada (`hire_date`) e qual será o
  novo valor (`account.created_on`). O valor vem de
  outra tabela, por isso é necessário indicar a
  tabela de origem com o prefixo `account.`.

- `FROM account` — **opcional:** usado apenas quando
  o novo valor vem de outra tabela. Indica de onde
  vêm os dados que serão atribuídos no `SET`. Sem
  o `FROM`, o `SET` só poderia usar valores fixos
  ou colunas da própria tabela do `UPDATE`.

- `WHERE account_job.user_id = account.user_id` —
  **obrigatório quando usa `FROM`:** conecta as duas
  tabelas pela coluna em comum (`user_id`). Garante
  que cada linha de `account_job` receba o valor
  do usuário correto de `account`. Sem o `WHERE`,
  o banco não saberia qual linha de `account`
  corresponde a qual linha de `account_job` —
  e atualizaria todas as linhas com o mesmo valor.



### O que acontece sem o WHERE
```sql
-- SEM WHERE → todas as linhas recebem
-- o mesmo valor (comportamento perigoso):
UPDATE account_job
SET hire_date = account.created_on
FROM account;

-- Resultado imprevisível:
-- todas as linhas de account_job receberiam
-- o created_on de um usuário aleatório
-- de account.
```

---

### Estrutura geral do UPDATE
```
UPDATE  → tabela que será modificada
SET     → coluna = novo valor
FROM    → tabela de onde vem o novo valor (opcional)
WHERE   → condição de ligação entre tabelas
          (obrigatório quando usa FROM)
          ou condição de filtro de linhas
```