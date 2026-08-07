## UPDATE + RETURNING — Como atualizar e visualizar o resultado sem um SELECT separado?

**Tabela utilizada:** `account`
```
account (antes do UPDATE)
+---------+----------+---------------------+------------+
| user_id | username | created_on          | last_login |
+---------+----------+---------------------+------------+
|       1 | Jose     | 2025-01-10 09:00:00 | NULL       |
|       2 | Maria    | 2025-03-22 14:00:00 | NULL       |
|       3 | Carlos   | 2025-07-05 11:00:00 | NULL       |
+---------+----------+---------------------+------------+
```

### Query
```sql
UPDATE account
SET
    last_login = CURRENT_TIMESTAMP
RETURNING
    user_id,
    username,
    last_login;
```


### Resultado
```
+---------+----------+---------------------+
| user_id | username | last_login          |
+---------+----------+---------------------+
|       1 | Jose     | 2025-09-29 14:37:52 |
|       2 | Maria    | 2025-09-29 14:37:52 |
|       3 | Carlos   | 2025-09-29 14:37:52 |
+---------+----------+---------------------+
```

---

A query atualizou `last_login` de todos os registros
para a data e hora atuais, e imediatamente retornou
as colunas escolhidas com os novos valores já aplicados
— sem precisar de um `SELECT` separado. Como não há
`WHERE`, todos os usuários foram afetados. Na prática,
`RETURNING` é usado quando você precisa confirmar ou
usar os dados da linha modificada logo após a operação.



### O que cada parte faz

- `UPDATE account` — seleciona a tabela `account`
  como destino da modificação.

- `SET last_login = CURRENT_TIMESTAMP` — atualiza
  a coluna `last_login` com a data e hora atuais
  do sistema. Como não há `WHERE`, todas as linhas
  da tabela são afetadas.

- `RETURNING user_id, username, last_login` —
  **novo:** retorna as colunas escolhidas das linhas
  que foram modificadas, já com os novos valores
  aplicados. Evita a necessidade de um `SELECT`
  separado após o `UPDATE`. Também é possível usar
  `RETURNING *` para retornar todas as colunas da
  linha afetada.



### RETURNING * vs colunas específicas
```sql
-- Retorna só o necessário (recomendado):
RETURNING user_id, username, last_login

-- Retorna tudo (útil para depuração rápida):
RETURNING *
```


### Quando usar RETURNING na prática
```
1. Descobrir o ID gerado ou atualizado
   → você não sabia o valor antes da operação

2. Confirmar qual linha foi afetada
   → especialmente com WHERE complexo

3. Evitar uma segunda consulta ao banco
   → ganho de performance

4. Usar os dados na mesma transação
   → ex: gravar em uma tabela de log ou auditoria
```

---

### RETURNING é exclusivo do PostgreSQL
```sql
-- PostgreSQL → suportado:
UPDATE account
SET last_login = CURRENT_TIMESTAMP
RETURNING user_id, username;

-- MySQL → NÃO suportado.
-- Para obter o mesmo resultado no MySQL seria
-- necessário um SELECT separado após o UPDATE.
```