# RIGHT JOIN - Mostra todos os registros da tabela da direita (Logins)

## Tabelas

**Registrations**

| reg_id | name    |
|--------|---------|
| 1      | Andrew  |
| 2      | Bob     |
| 3      | Charlie |
| 4      | David   |

**Logins**

| log_id | name    |
|--------|---------|
| 1      | Xavier  |
| 2      | Andrew  |
| 3      | Yolanda |
| 4      | Bob     |

## Query
SELECT 
    r.reg_id,
    r.name,
    l.log_id,
    l.name
FROM Registrations AS r
RIGHT JOIN Logins AS l
    ON r.name = l.name;

## Resultado
    +--------+---------+--------+---------+
    | reg_id | name    | log_id | name    |
    +--------+---------+--------+---------+
    | 1      | Andrew  | 2      | Andrew  |  ←  match (Andrew)
    | 2      | Bob     | 4      | Bob     |  ←  match (Bob)
    | null   | null    | 1      | Xavier  |  ←  só na direita (Logins)
    | null   | null    | 3      | Yolanda |  ←  só na direita (Logins)
    +--------+---------+--------+---------+

