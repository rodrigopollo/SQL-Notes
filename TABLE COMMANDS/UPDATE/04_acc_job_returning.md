## UPDATE + RETURNING — Como registrar a promoção de um funcionário e confirmar a alteração?

**Tabela utilizada:** `account_job`

```
account_job (antes do UPDATE)
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
UPDATE account_job
SET
    job_id = 102
WHERE
    user_id = 3
RETURNING
    user_id,
    job_id,
    hire_date;
```


### Resultado
```
+---------+--------+---------------------+
| user_id | job_id | hire_date           |
+---------+--------+---------------------+
|       3 |    102 | 2025-07-05 11:00:00 |
+---------+--------+---------------------+
```

---

A query promoveu Carlos (user_id 3) do cargo 101
para o cargo 102, sem alterar sua data de contratação.
`RETURNING` confirmou imediatamente os dados da linha
afetada após a alteração — o novo `job_id` já aparece
no resultado sem precisar de um `SELECT` separado.
Apenas 1 linha foi afetada, exatamente como esperado
ao filtrar pela chave primária.



### O que cada parte faz

- `UPDATE account_job` — seleciona a tabela que
  será modificada.

- `SET job_id = 102` — atualiza o cargo do
  funcionário filtrado para 102. Número inteiro,
  sem aspas.

- `WHERE user_id = 3` — limita a alteração apenas
  à linha de Carlos. Sem esse filtro, todos os
  funcionários seriam movidos para o cargo 102.

- `RETURNING user_id, job_id, hire_date` — retorna
  as colunas escolhidas já com o novo valor aplicado,
  confirmando que o `job_id` correto foi atualizado
  na linha certa.


### Estado da tabela após o UPDATE
```
account_job (depois do UPDATE)
+---------+--------+---------------------+
| user_id | job_id | hire_date           |
+---------+--------+---------------------+
|       1 |    101 | 2025-01-10 09:00:00 |
|       2 |    102 | 2025-03-22 14:00:00 |
|       3 |    102 | 2025-07-05 11:00:00 |← alterado
+---------+--------+---------------------+
```