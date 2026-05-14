# INNER JOIN + WHERE + GROUP BY + SUM()

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
    c.city,
    SUM(p.amount) AS total_amount
FROM customers AS c
INNER JOIN payments AS p
    ON p.customer_id = c.customer_id
WHERE
    p.payment_date >= '2025-07-01'
    AND p.payment_date < '2025-10-01'
    AND p.method <> 'transfer'
    AND p.amount >= 15
GROUP BY
    c.first_name,
    c.city
ORDER BY
    total_amount DESC,
    c.first_name ASC;


## Resultado Esperado
----------------------------------------
| first_name | city   | total_amount |
----------------------------------------
| Steven     | Rome   | 30.00        |
| David      | Naples | 15.00        |
----------------------------------------

---

## Explicacao

O `INNER JOIN` conecta as tabelas `customers` e `payments` usando o campo `customer_id`.
Depois disso, o `WHERE` aplica varios filtros usando AND:

Filtros do `WHERE`
- So pagamentos entre julho e setembro de 2025
- Remove pagamentos com metodo `transfer`
- Mantem apenas valores maiores ou iguais a `15`

Depois:
- `GROUP BY` agrupa os resultados por cliente e cidade
- `SUM(p.amount)` calcula o total gasto
- `ORDER BY total_amount DESC` organiza do maior para o menor total
- `c.first_name ASC` organiza alfabeticamente em caso de empate

Calculo final:
- Steven: 30.00
- David: 15.00


## Observacoes
- `<>` significa diferente de.
- `GROUP BY` pode usar mais de uma coluna.
- `SUM()` calcula o total dos valores filtrados.
- `ORDER BY` pode usar varias regras de ordenacao ao mesmo tempo.
- Pagamentos fora da faixa de datas sao ignorados.