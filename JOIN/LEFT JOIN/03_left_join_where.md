# LEFT JOIN + WHERE IS NULL - Explicacao Completa


## TABELAS UTILIZADAS
Registrations

| reg_id | name    |
|--------|----------|
| 1      | Andrew   |
| 2      | Bob      |
| 3      | Charlie  |
| 4      | David    |

Logins

| log_id | name    |
|--------|----------|
| 1      | Xavier   |
| 2      | Andrew   |
| 3      | Yolanda  |
| 4      | Bob      |


## QUERY
SELECT
    r.reg_id,
    r.name
FROM Registrations AS r
LEFT JOIN Logins AS l
    ON r.name = l.name
WHERE l.log_id IS NULL;

## RESULTADO 

| reg_id | name    |
|--------|---------|
| 3      | Charlie |
| 4      | David   |

---

### EXPLICACAO
* LEFT JOIN
    --> mostra TODAS as linhas da tabela Registrations

* ON r.name = l.name
    --> compara os nomes entre as tabelas

* WHERE l.log_id IS NULL
    --> mantem apenas as linhas que NAO encontraram correspondencia


## IMPORTANTE
LEFT JOIN + IS NULL eh MUITO usado para:

* encontrar dados faltando
* encontrar usuarios inativos
* encontrar registros sem correspondencia
* auditoria de dados
* ETL/Data Engineering

"Mostre tudo da tabela da esquerda que NAO existe na tabela da direita."

--------------------------------------------------
RESUMO VISUAL
--------------------------------------------------

| Pessoa    | Registrou?     | Fez login?   | Aparece no resultado? |
|-----------|----------------|--------------|-----------------------|
| Andrew    | ✅            | ✅          | ❌                     |
| Bob       | ✅            | ✅          | ❌                     |
| Charlie   | ✅            | ❌          | ✅                     |
| David     | ✅            | ❌          | ✅                     |
