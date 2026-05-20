# FULL OUTER JOIN + WHERE IS NULL

## Explicacao


# Tabela Registrations
| reg_id | name    |
|--------|---------|
| 1      | Andrew  |
| 2      | Bob     |
| 3      | Charlie |
| 4      | David   |

# Tabela Logins
| log_id | name    |
|--------|---------|
| 1      | Xavier  |
| 2      | Andrew  |
| 3      | Yolanda |
| 4      | Bob     |


# Comando SQL
SELECT *
FROM Registrations AS r

FULL OUTER JOIN Logins AS l
    ON r.name = l.name

WHERE
    r.reg_id IS NULL
    OR l.log_id IS NULL;


# Resultado Esperado
| reg_id | r.name  | log_id | l.name  |
|--------|---------|--------|---------|
| 3      | Charlie | NULL   | NULL    |
| 4      | David   | NULL   | NULL    |
| NULL   | NULL    | 1      | Xavier  |
| NULL   | NULL    | 3      | Yolanda |

---

# Explicacao Linha por Linha

| Registro | Explicacao                      |
|----------|---------------------------------|
| Charlie  | Existe somente em Registrations |
| David    | Existe somente em Registrations |
| Xavier   | Existe somente em Logins        |
| Yolanda  | Existe somente em Logins        |


Neste exemplo, o `FULL OUTER JOIN` eh usado junto com `WHERE IS NULL`
para mostrar apenas os registros que NAO deram match entre as tabelas.

Ou seja:
- registros que existem somente na tabela da esquerda
- registros que existem somente na tabela da direita

Os registros que coincidem entre as tabelas sao removidos pelo `WHERE`.
Neste caso:
- `r.reg_id` NAO eh NULL
- `l.log_id` NAO eh NULL

Resultado:
- linha removida pelo WHERE

# Quando aparece no resultado?
A linha aparece quando:

| Situacao              | Resultado          |
|-----------------------|--------------------|
| So existe na esquerda | l.log_id vira NULL |
| So existe na direita  | r.reg_id vira NULL |


# Uso Profissional
Esse padrao eh MUITO usado para:

- encontrar dados faltando
- comparar tabelas
- detectar inconsistencias
- auditoria de dados
- validacao de ETL
- reconciliacao de sistemas

# Exemplo Real de Mercado
Comparar:
- clientes cadastrados
- clientes que fizeram login

ou:
- produtos vendidos
- produtos entregues

ou:
- dados do ERP
- dados do CRM

# Resumo

| Query                           | O que retorna              |
|---------------------------------|----------------------------|
| FULL OUTER JOIN                 | Tudo das duas tabelas      |
| FULL OUTER JOIN + WHERE IS NULL | Apenas registros sem match |


# Observacao do professor:
Nem todos os bancos suportam `FULL OUTER JOIN`.

Exemplo:
- PostgreSQL -> suporta
- SQL Server -> suporta
- Oracle -> suporta
- MySQL -> nao suporta diretamente

No MySQL normalmente para simular um `FULL OUTER JOIN` se usa:
- LEFT JOIN
- RIGHT JOIN
- UNION
