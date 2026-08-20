## DELETE + SUBQUERY — Como remover vínculos de usuários que nunca fizeram login?

**Tabelas utilizadas:** `account_job`, `account`
```
account
+---------+----------+---------------------+------------+
| user_id | username | created_on          | last_login |
+---------+----------+---------------------+------------+
|       1 | Jose     | 2025-01-10 09:00:00 | 2025-09-29 |
|       2 | Maria    | 2025-03-22 14:00:00 | 2025-09-29 |
|       3 | Carlos   | 2025-07-05 11:00:00 | NULL       |
+---------+----------+---------------------+------------+

account_job (antes do DELETE)
+---------+--------+---------------------+
| user_id | job_id | hire_date           |
+---------+--------+---------------------+
|       1 |    101 | 2025-01-10 09:00:00 |
|       2 |    102 | 2025-03-22 14:00:00 |
|       3 |    101 | 2025-07-05 11:00:00 |
+---------+--------+---------------------+
```



### Query
```sql
DELETE FROM account_job
WHERE user_id IN (
    SELECT user_id
    FROM account
    WHERE last_login IS NULL
)
RETURNING *;
```


### Resultado
```
+---------+--------+---------------------+
| user_id | job_id | hire_date           |
+---------+--------+---------------------+
|       3 |    101 | 2025-07-05 11:00:00 |
+---------+--------+---------------------+
```

---

A query removeu o vínculo de Carlos (user_id 3) da
tabela `account_job` pois ele nunca fez login
(`last_login IS NULL`). Jose e Maria permaneceram
intactos pois têm registro de login. A subquery
identificou quais usuários nunca acessaram o sistema,
e o `DELETE` usou essa lista como filtro — combinando
dois conceitos já vistos: `DELETE` e `SUBQUERY`.



### O que cada parte faz

- `DELETE FROM account_job` — seleciona a tabela
  `account_job` como origem da remoção.

- `WHERE user_id IN (...)` — usa o resultado da
  subquery como filtro. Apenas as linhas cujo
  `user_id` esteja na lista retornada pela subquery
  serão deletadas.

- **Subquery:**
  - `SELECT user_id FROM account` — busca os ids
    de usuários na tabela `account`.
  - `WHERE last_login IS NULL` — filtra apenas os
    usuários que nunca fizeram login. `IS NULL` é
    a forma correta de verificar campos vazios no
    SQL — `= NULL` não funciona.

- `RETURNING *` — retorna todas as colunas das
  linhas removidas, confirmando o que foi deletado.

---

### Estado da tabela após o DELETE
```
account_job (depois do DELETE)
+---------+--------+---------------------+
| user_id | job_id | hire_date           |
+---------+--------+---------------------+
|       1 |    101 | 2025-01-10 09:00:00 |
|       2 |    102 | 2025-03-22 14:00:00 |
+---------+--------+---------------------+
```


### Ordem de execução

```
1º → a subquery roda e busca usuários com
     last_login IS NULL em account:
     user_id 3 (Carlos) → last_login NULL ✓
     lista retornada: [3]

2º → o DELETE filtra account_job:
     user_id 1 → não está em [3] → mantido
     user_id 2 → não está em [3] → mantido
     user_id 3 → está em [3]    → deletado ✓

3º → RETURNING exibe a linha removida
```

---

### IS NULL vs = NULL
```sql
-- ERRADO — nunca use = NULL:
WHERE last_login = NULL   → não retorna nada,
                            mesmo com campos vazios

-- CORRETO — sempre use IS NULL:
WHERE last_login IS NULL  → funciona corretamente
```

No SQL, `NULL` representa ausência de valor —
ele não é igual a nada, nem a si mesmo. Por isso
a comparação com `=` nunca funciona para verificar
campos vazios.