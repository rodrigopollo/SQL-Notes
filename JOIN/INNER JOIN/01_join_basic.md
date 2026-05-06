# INNER JOIN (Basico)

## Tabela: customers:
----------------------------------------------------------------------
| customer_id | first_name | last_name | email              | city   |
----------------------------------------------------------------------
| 1           | Steven     | Cole      | steven@example.com | Rome   |
| 2           | Claire     | Reed      | claire@example.com | Milan  |
| 3           | David      | Hunt      | david@example.com  | Naples |
| 4           | Zach       | Stone     | zach@example.com   | Turin  |
| 5           | Andrew     | Park      | andrew@example.com | Rome   |
----------------------------------------------------------------------

## Tabela: payments:
----------------------------------------------------------------------
| payment_id | customer_id | payment_date        | amount | method   |
----------------------------------------------------------------------
| 1          | 1           | 2025-09-07 08:15:00 | 10.00  | card     |
| 2          | 2           | 2025-02-05 14:45:00 | 20.00  | cash     |
| 3          | 1           | 2025-09-07 21:40:00 | 30.00  | card     |
| 4          | 3           | 2025-07-23 09:30:00 | 15.00  | card     |
| 5          | 3           | 2025-07-23 22:05:00 | 25.00  | transfer |
| 6          | 1           | 2025-06-01 10:15:00 | 18.00  | cash     |
----------------------------------------------------------------------

## Comando SQL:
SELECT
    c.first_name,
    p.payment_date,
    p.amount
FROM customers AS c
INNER JOIN payments AS p
    ON p.customer_id = c.customer_id
ORDER BY p.payment_date;

## Resultado Esperado:

---------------------------------------------
| first_name | payment_date        | amount |
---------------------------------------------
| Claire     | 2025-02-05 14:45:00 | 20.00  |
| Steven     | 2025-06-01 10:15:00 | 18.00  |
| David      | 2025-07-23 09:30:00 | 15.00  |
| David      | 2025-07-23 22:05:00 | 25.00  |
| Steven     | 2025-09-07 08:15:00 | 10.00  |
| Steven     | 2025-09-07 21:40:00 | 30.00  |
---------------------------------------------

---

## Explicacao:
O `INNER JOIN` eh utilizado para combinar dados de duas tabelas com base em uma coluna em comum.

Neste exemplo:
- A tabela `customers` contem informacoes dos clientes
- A tabela `payments` contem os pagamentos realizados

A condicao:
    - p.customer_id = c.customer_id
faz a ligacao entre as tabelas, retornando apenas os registros que existem em ambas.

Ou seja:
- Cada pagamento eh associado ao seu respectivo cliente
- Registros que nao estao nas 2 tabelas nao aparecem no resultado

## Observacoes:
- `INNER JOIN` retorna apenas a informaçao que esta disponivel nas 2 tabelas
- O  `AS` cria apelidos (alias) ara facilitar a leitura (`c` e `p`)
- `ORDER BY` organiza os resultados pela data do pagamento