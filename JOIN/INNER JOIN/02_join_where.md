# INNER JOIN + WHERE

## Tabela: customers:
---------------------------------------------------------------------------
| customer_id | first_name | last_name | email              | city   |
---------------------------------------------------------------------------
| 1           | Steven     | Cole      | steven@example.com | Rome   |
| 2           | Claire     | Reed      | claire@example.com | Milan  |
| 3           | David      | Hunt      | david@example.com  | Naples |
| 4           | Zach       | Stone      | zach@example.com   | Turin  |
| 5           | Andrew     | Park      | andrew@example.com | Rome   |
---------------------------------------------------------------------------

## Tabela: payments:
---------------------------------------------------------------------------
| payment_id | customer_id | payment_date        | amount | method   |
---------------------------------------------------------------------------
| 1          | 1           | 2025-09-07 08:15:00 | 10.00  | card     |
| 2          | 2           | 2025-02-05 14:45:00 | 20.00  | cash     |
| 3          | 1           | 2025-09-07 21:40:00 | 30.00  | card     |
| 4          | 3           | 2025-07-23 09:30:00 | 15.00  | card     |
| 5          | 3           | 2025-07-23 22:05:00 | 25.00  | transfer |
| 6          | 1           | 2025-06-01 10:15:00 | 18.00  | cash     |
---------------------------------------------------------------------------

## Comando SQL:
SELECT
    c.first_name,
    c.city,
    p.payment_date,
    p.amount
FROM customers AS c
INNER JOIN payments AS p
    ON p.customer_id = c.customer_id
WHERE c.city = 'Rome'
ORDER BY p.payment_date;


## Resultado Esperado:
---------------------------------------------------------------
| first_name | city | payment_date        | amount |
---------------------------------------------------------------
| Steven     | Rome | 2025-06-01 10:15:00 | 18.00  |
| Steven     | Rome | 2025-09-07 08:15:00 | 10.00  |
| Steven     | Rome | 2025-09-07 21:40:00 | 30.00  |
---------------------------------------------------------------

---

## Explicacao:
O `INNER JOIN` combina os dados das tabelas `customers` e `payments` usando a coluna `customer_id` q esta
presente nas 2 tabelas.

A clausula:
    - p.customer_id = c.customer_id
faz a conexao entre as tabelas.

Depois disso, o `WHERE c.city = 'Rome'` filtra para mostras so os clientes que sao de ROME

Resultado:
- Apenas Steven aparece
- Todos os pagamentos de Steven sao exibidos
- Clientes q nao sejam de ROME sao removidos, e por tanto nao serao mostrados.

## Observacoes:
- `INNER JOIN` retorna so registros que existem nas 2 tabelas
- `WHERE` filtra os dados depois do `JOIN`.
- Andrew esta em Rome, mas nao aparece porque nao possui pagamentos na tabela `payments`.
- `ORDER BY p.payment_date` organiza os pagamentos por data.