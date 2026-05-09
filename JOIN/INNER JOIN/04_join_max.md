# INNER JOIN + MAX()

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
    MAX(p.payment_date) AS last_payment
FROM customers AS c
INNER JOIN payments AS p
    ON p.customer_id = c.customer_id
GROUP BY c.first_name
ORDER BY last_payment DESC;


## Resultado Esperado:
------------------------------------------------
| first_name | last_payment        |
------------------------------------------------
| Steven     | 2025-09-07 21:40:00 |
| David      | 2025-07-23 22:05:00 |
| Claire     | 2025-02-05 14:45:00 |
------------------------------------------------

---

## Explicacao:
O `INNER JOIN` conecta as tabelas `customers` e `payments` usando o campo `customer_id`.

Depois disso:
- `GROUP BY c.first_name` agrupa os pagamentos por cliente
- `MAX(p.payment_date)` pega a data mais recente de pagamento de cada cliente
- `ORDER BY last_payment DESC` organiza do pagamento mais recente para o mais antigo

Resultado:
- Steven teve o ultimo pagamento em `2025-09-07 21:40:00`
- David teve o ultimo pagamento em `2025-07-23 22:05:00`
- Claire teve o ultimo pagamento em `2025-02-05 14:45:00`

Clientes sem pagamentos nao aparecem porque o `INNER JOIN` retorna so os registros com que estao nas 
dois tabelas.

## Observacoes:
- `MAX()` retorna o maior valor de uma coluna.
- Em colunas de data, `MAX()` retorna a data mais recente.
- `GROUP BY` eh necessario para agrupar o resultado por cliente.
- Zach e Andrew nao aparecem porque nao possuem pagamentos.