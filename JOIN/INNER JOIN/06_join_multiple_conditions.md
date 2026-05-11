# INNER JOIN + WHERE (Multiplas Condicoes)

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
    p.amount,
    p.method
FROM customers AS c
INNER JOIN payments AS p
    ON p.customer_id = c.customer_id
WHERE
    p.method = 'card'
    AND p.amount > 20
ORDER BY p.amount DESC;


## Resultado Esperado:
----------------------------------------------------------
| first_name | payment_date        | amount | method |
----------------------------------------------------------
| Steven     | 2025-09-07 21:40:00 | 30.00  | card   |
----------------------------------------------------------

---

## Explicacao:
O `INNER JOIN` conecta as tabelas `customers` e `payments` usando o `customer_id`.

Depois disso, o `WHERE` aplica duas condicoes:
- `p.method = 'card'`
- `p.amount > 20`

O  `AND` exige que as duas condicoes sejam verdadeiras ao mesmo tempo.

Resultado:
- So pagamentos feitos com `card`
- So pagamentos maiores que `20`
- So Steven atende as duas condicoes

## Observacoes:
- `AND` combina multiplas condicoes.
- `ORDER BY p.amount DESC` organiza do maior para o menor valor.
- `INNER JOIN` retorna so os registros que estao nas dois tabelas.
