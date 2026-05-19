# FULL OUTER JOIN

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
| 1      | Xavier  |
| 2      | Andrew  |
| 3      | Yolanda |
| 4      | Bob     |


# Comando SQL:
SELECT *
FROM registrations AS r
FULL OUTER JOIN logins AS l
    ON r.name = l.name;


# Resultado Esperado:
| reg_id | r.name  | log_id | l.name  |
|--------|---------|--------|---------|
| 1      | Andrew  | 2      | Andrew  |
| 2      | Bob     | 4      | Bob     |
| 3      | Charlie | NULL   | NULL    |
| 4      | David   | NULL   | NULL    |
| NULL   | NULL    | 1      | Xavier  |
| NULL   | NULL    | 3      | Yolanda |

---

# Explicacao: 
O `FULL OUTER JOIN` retorna:
- os registros que deram match entre as tabelas
- os registros que existem somente na tabela da esquerda
- os registros que existem somente na tabela da direita

Quando nao existe correspondencia, o SQL preenche com `NULL`.

# Linha por Linha:
| Situacao | Explicacao                       |
|----------|----------------------------------|
| Andrew   | Existe nas duas tabelas -> MATCH |
| Bob      | Existe nas duas tabelas -> MATCH |
| Charlie  | Existe somente em Registrations  |
| David    | Existe somente em Registrations  |
| Xavier   | Existe somente em Logins         |
| Yolanda  | Existe somente em Logins         |



# Visualizacao Mental
FULL OUTER JOIN faz:
Tabela esquerda
+
Matches
+
Tabela direita



# Resumo
| JOIN             | O que retorna              |
|------------------|----------------------------|
| INNER JOIN       | Apenas matches             |
| LEFT JOIN        | Tudo da esquerda + matches |
| RIGHT JOIN       | Tudo da direita + matches  |
| FULL OUTER JOIN  | Tudo das duas tabelas      |


# Observacao Importante
Nem todos os bancos suportam `FULL OUTER JOIN`.

Exemplo:
- PostgreSQL -> suporta
- SQL Server -> suporta
- Oracle -> suporta
- MySQL -> NAO suporta diretamente
