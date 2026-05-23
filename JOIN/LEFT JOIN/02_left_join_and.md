# LEFT JOIN + AND - Filtro na tabela da direita

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
    l.log_id
FROM Registrations AS r
LEFT JOIN Logins AS l
    ON r.name = l.name
    AND l.log_id >= 3;

## Resultado
| reg_id | name    | log_id |
|--------|---------|--------|
| 1      | Andrew  | NULL   |
| 2      | Bob     | 4      |
| 3      | Charlie | NULL   |
| 4      | David   | NULL   |

---

## Explicação
- `LEFT JOIN` garante que **todos** os registros da tabela `Registrations` apareçam no resultado, 
independentemente de se os datos coincidem com a tabela `Logins`
- A condição `AND l.log_id >= 3` eh aplicada **durante o JOIN**, nao depois (diferença fundamental do `WHERE`)
- Os registros de `Logins` são unidos apenas se **ambas**  condiçoes forem verdadeiras:
  1. `r.name = l.name` (nome igual)
  2. `l.log_id >= 3` (log_id maior ou igual a 3)
- Se nenhum registro em `Logins` compror com as condiçoes, o SQL mantem `Registrations` e preenche
as colunas de `Logins` com `NULL`

## Diferença crucial: AND no JOIN vs WHERE
  * `AND` no `LEFT JOIN` ->  Filtra **quais linhas da tabela da direita vao se juntar**. As linhas da esquerda
  sempre aparecem.                                     
  * `WHERE` depois do `LEFT JOIN` -> Filtra o **resultado final** e pode **remover** linhas da esquerda
  que nao cumprem com a condiçao

## Exemplo comparativo
-- AND no JOIN (mantem todos da esquerda)
LEFT JOIN Logins l 
    ON r.name = l.name 
    AND l.log_id >= 3

-- WHERE após JOIN (pode remover linhas da esquerda)
LEFT JOIN Logins l 
    ON r.name = l.name
WHERE 
    l.log_id >= 3  -- Remove linhas onde l.log_id IS NULL
