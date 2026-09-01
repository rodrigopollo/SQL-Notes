## INSERT INTO — Como inserir dados em uma tabela com chave estrangeira?


### Query
```sql
INSERT INTO account_job (
    user_id,
    job_id,
    hire_date
)
VALUES
    (1, 101, CURRENT_TIMESTAMP),
    (2, 102, CURRENT_TIMESTAMP),
    (3, 101, CURRENT_TIMESTAMP);
```



### Tabelas envolvidas antes do INSERT
```
account
+---------+----------+
| user_id | username |
+---------+----------+
|       1 | Jose     |
|       2 | Maria    |
|       3 | Carlos   |
+---------+----------+

job
+--------+------------------+
| job_id | title            |
+--------+------------------+
|    101 | Analista         |
|    102 | Engenheiro       |
+--------+------------------+
```



### Resultado — linhas inseridas na tabela account_job
```
+---------+--------+---------------------+
| user_id | job_id | hire_date           |
+---------+--------+---------------------+
|       1 |    101 | 2025-09-29 14:37:52 |
|       2 |    102 | 2025-09-29 14:37:52 |
|       3 |    101 | 2025-09-29 14:37:52 |
+---------+--------+---------------------+
```

---

A query vincula 3 usuários a seus respectivos cargos.
Jose e Carlos foram contratados como Analistas (101),
e Maria como Engenheira (102). Como `account_job` tem
chaves estrangeiras para `account` e `job`, o banco
valida automaticamente se cada `user_id` e `job_id`
existem em suas tabelas de origem antes de aceitar
o registro. Dois usuários podem ter o mesmo `job_id`
— um cargo pode ter vários funcionários.



### O que cada parte faz

- `INSERT INTO account_job (...)` — seleciona a tabela
  de junção `account_job` como destino da inserção.

- `user_id` e `job_id` — números inteiros que
  **precisam existir** nas tabelas `account` e `job`
  respectivamente. O banco valida isso antes de
  aceitar o `INSERT` por causa das `FOREIGN KEYS`
  definidas na criação da tabela.

- `CURRENT_TIMESTAMP` — preenche `hire_date` com a
  data e hora do momento da execução, sem aspas pois
  é uma função do banco.

- Múltiplas linhas separadas por vírgula — inserção
  de 3 registros em um único comando.



### O que acontece ao tentar inserir um valor inválido

```sql
-- Tentando vincular user_id 99 que não existe
-- em account:
INSERT INTO account_job (user_id, job_id, hire_date)
VALUES (99, 101, CURRENT_TIMESTAMP);

-- O banco rejeita com erro:
-- ERROR: insert or update on table "account_job"
-- violates foreign key constraint "fk_customer"
-- DETAIL: Key (user_id)=(99) is not present
-- in table "account".
```

A `FOREIGN KEY` age como um guardião: qualquer
tentativa de inserir um valor que não existe na
tabela referenciada é bloqueada automaticamente,
sem precisar de nenhuma validação extra na aplicação.



### Ordem de validação do banco no INSERT
```
1º → verifica se user_id existe em account
     user_id 1 → existe ✓
     user_id 2 → existe ✓
     user_id 3 → existe ✓

2º → verifica se job_id existe em job
     job_id 101 → existe ✓
     job_id 102 → existe ✓
     job_id 101 → existe ✓

3º → todas as validações passaram
     → registros inseridos com sucesso
```