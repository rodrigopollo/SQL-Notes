# INNER JOIN + DISTINCT

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
SELECT DISTINCT
    c.first_name
FROM customers AS c
INNER JOIN payments AS p
    ON p.customer_id = c.customer_id
ORDER BY c.first_name;


## Resultado Esperado
----------------
| first_name |
----------------
| Claire     |
| David      |
| Steven     |
----------------

---

## Explicacao:
O `INNER JOIN` conecta as tabelas `customers` e `payments` usando o `customer_id`.

Como o `INNER JOIN` retorna so os registros que coincidem nas 2 tabelas, so clientes que
tem pagamentos aparecem no resultado.

O `DISTINCT` remove nomes repetidos.
Sem o `DISTINCT`, Steven e David apareceriam varias vezes porque tem mais de um pagamento.

Resultado:
- Claire tem pagamento
- David tem pagamento
- Steven tem pagamento
- Zach e Andrew nao aparecem porque eles nao possuem pagamentos

## Observacoes:
- `DISTINCT` remove valores duplicados.
- `INNER JOIN` naturalmente exclui registros que nao coincidem em ambas tabelas.
- Muito usado para descobrir clientes, usuarios ou produtos com movimentacao.
- `ORDER BY` organiza os nomes em ordem alfabetica.