# LEFT JOIN + WHERE - Filtros que afetam o resultado do LEFT JOIN

## Tabela: Registrations

| reg_id | name    |
|--------|---------|
| 1      | Andrew  |
| 2      | Bob     |
| 3      | Charlie |
| 4      | David   |

## Tabela: Logins

| log_id | name    |
|--------|---------|
| 1      | Andrew  |
| 2      | Andrew  |
| 3      | Andrew  |
| 4      | Bob     |
| 5      | Bob     |
| 6      | Charlie |

## Query
SELECT 
    r.reg_id,
    r.name,
    l.log_id,
    l.name
FROM Registrations AS r
LEFT JOIN Logins AS l
    ON r.name = l.name
WHERE 
    r.reg_id >= 2
    AND (l.log_id IS NULL OR l.log_id >= 2)
ORDER BY 
    r.reg_id ASC;


## Resultado

| reg_id | name    | log_id | name    |
|--------|---------|--------|---------|
| 2      | Bob     | 4      | Bob     |
| 3      | Charlie | NULL   | NULL    |
| 4      | David   | NULL   | NULL    |


---


## Explicação
- `LEFT JOIN` garante que **todos** os registros de `Registrations` apareçam inicialmente
- As condiçoes no `WHERE` sao aplicadas **depois do JOIN** e filtram o resultado final
- O `WHERE` filtra e **remove as linha** que apareceram no `LEFT JOIN`


**Por que Charlie aparece com log_id = 6?**

Porque Charlie tem `log_id = 6` e a condiçao `r.reg_id >= 2` **nao elimina a linha**. 
O `LEFT JOIN` mantem Charlie com seu login.


## 🎯 Lição importante
Filtro no `ON`** do `LEFT JOIN`
    * Aplica na tabela da direita **antes** de unir as tabelas. Todas as linhas da esquerda sao mantidas

Filtro no `WHERE`** após `LEFT JOIN`  
    * Aplica no resultado **depois** da uniao. Pode eliminar linhas da esquerda (inclusive as que têm `NULL`)



