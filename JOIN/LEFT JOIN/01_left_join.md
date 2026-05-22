# LEFT JOIN - Explicacao Completa

--------------------------------------------------
TABELAS UTILIZADAS
--------------------------------------------------

Registrations

| reg_id | name    |
|--------|---------|
| 1      | Andrew  |
| 2      | Bob     |
| 3      | Charlie |
| 4      | David   |

Logins

| log_id | name     |
|--------|----------|
| 1      | Xavier   |
| 2      | Andrew   |
| 3      | Yolanda  |
| 4      | Bob      |

--------------------------------------------------
QUERY
--------------------------------------------------

SELECT
    r.reg_id,
    r.name,
    l.log_id,
    l.name
FROM Registrations AS r

LEFT JOIN Logins AS l
    ON r.name = l.name;


## RESULTADO

| reg_id | name      | log_id | name     |
|--------|-----------|--------|----------|
| 1      | Andrew    | 2      | Andrew   |
| 2      | Bob       | 4      | Bob      |
| 3      | Charlie   | NULL   | NULL     |
| 4      | David     | NULL   | NULL     |

--------------------------------------------------
EXPLICACAO
--------------------------------------------------

* FROM Registrations AS r
    --> tabela principal
    --> o LEFT JOIN sempre prioriza a tabela do FROM

* LEFT JOIN Logins AS l
    --> junta a tabela Logins com Registrations

* ON r.name = l.name
    --> compara os nomes das duas tabelas

--------------------------------------------------
COMO O LEFT JOIN FUNCIONA
--------------------------------------------------

O LEFT JOIN:

* mostra TODAS as linhas da tabela da esquerda (FROM)
* tenta encontrar correspondencias na tabela da direita
* quando nao encontra:
    --> retorna NULL

--------------------------------------------------
PASSO A PASSO
--------------------------------------------------


| Nome     | Existe em Logins? | Resultado   |
|----------|-------------------|-------------|
| Andrew   | SIM               | junta dados |
| Bob      | SIM               | junta dados |
| Charlie  | NAO               | NULL        |
| David    | NAO               | NULL        |

PASSO A PASSO:        
        Linha 1 (Andrew)  →  Andew existe também em Logins  →  junta com log_id=2
        Linha 2 (Bob)     →  Bob existe também em Logins    →  junta com log_id=4
        Linha 3 (Charlie) →  Charlie NÃO existe em Logins   →  log_id e name = NULL
        Linha 4 (David)   →  David NÃO existe em Logins     →  log_id e name = NULL

--------------------------------------------------
REGRA PRINCIPAL DO LEFT JOIN
--------------------------------------------------

LEFT JOIN:
* Mantem TODAS as linhas da tabela da esquerda
* Se encontrar dados correspondentes:
    --> junta os dados
* Se nao encontrar:
    --> Coloca com NULL


```