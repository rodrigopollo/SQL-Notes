# INNER JOIN + GROUP BY + SUM()

## Tabela: customers
---------------------------------------------------------------------------
| customer_id | first_name | last_name | email              | city   |
---------------------------------------------------------------------------
| 1           | Steven     | Cole      | steven@example.com | Rome   |
| 2           | Claire     | Reed      | claire@example.com | Milan  |
| 3           | David      | Hunt      | david@example.com  | Naples |
| 4           | Zach       | Stone     | zach@example.com   | Turin  |
| 5           | Andrew     | Park      | andrew@example.com | Rome   |
---------------------------------------------------------------------------

## Tabela: payments
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

## Comando SQL
SELECT
    c.first_name,
    SUM(p.amount) AS total_amount
FROM customers AS c
INNER JOIN payments AS p
    ON p.customer_id = c.customer_id
GROUP BY c.first_name
ORDER BY total_amount DESC;


## Resultado Esperado
--------------------------------
| first_name | total_amount |
--------------------------------
| Steven     | 58.00        |
| David      | 40.00        |
| Claire     | 20.00        |
--------------------------------

---

## Explicacao
O `INNER JOIN` conecta as tabelas `customers` e `payments` usando o `customer_id`.

- p.customer_id = c.customer_id   ->   faz a ligacao entre os clientes e seus pagamentos.

Depois disso:
- `GROUP BY c.first_name` agrupa os pagamentos por cliente
- `SUM(p.amount)` soma todos os pagamentos de cada cliente
- `ORDER BY total_amount DESC` organiza do maior para o menor valor gasto

Calculo por cliente:
- Steven: 10.00 + 30.00 + 18.00 = 58.00
- David: 15.00 + 25.00 = 40.00
- Claire: 20.00

Clientes sem pagamentos nao aparecem no resultado porque o `INNER JOIN` retorna apenas correspondencias
entre as tabelas.

## Observacoes
- Zach e Andrew nao aparecem porque nao possuem pagamentos.