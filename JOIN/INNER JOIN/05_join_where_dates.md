# INNER JOIN + WHERE (Faixa de Datas)

## Tabela: customers:
---------------------------------------------------------------------------
| customer_id | first_name | last_name | email              | city   |
---------------------------------------------------------------------------
| 1           | Steven     | Cole      | steven@example.com | Rome   |
| 2           | Claire     | Reed      | claire@example.com | Milan  |
| 3           | David      | Hunt      | david@example.com  | Naples |
| 4           | Zach       | Stone     | zach@example.com   | Turin  |
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
    p.payment_date,
    p.amount
FROM customers AS c
INNER JOIN payments AS p
    ON p.customer_id = c.customer_id
WHERE
    p.payment_date >= '2025-07-01'
    AND p.payment_date < '2025-08-01'
ORDER BY p.payment_date;

## Resultado Esperado:
---------------------------------------------------------
| first_name | payment_date        | amount |
---------------------------------------------------------
| David      | 2025-07-23 09:30:00 | 15.00  |
| David      | 2025-07-23 22:05:00 | 25.00  |
---------------------------------------------------------

---

## Explicacao:
O `INNER JOIN` conecta as tabelas `customers` e `payments` usando o campo `customer_id`.
Depois o `WHERE` filtra os pagamentos dentro dentro das datas selecionadas:

- Maior ou igual a `2025-07-01`
- Menor que `2025-08-01`
- Isso retorna apenas so realizados em julho de 2025.

Resultado:
- So o David aparece
- Os dois pagamentos feitos em julho vao ser mostrados

## Observacoes:
- Esse tipo de filtro eh chamado de `date range`.
- Usar `< '2025-08-01'` eh mais seguro do que usar `<= '2025-07-31 23:59:59'`.
- `ORDER BY` organiza os pagamentos pela data.
