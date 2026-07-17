## SUBQUERY — Quais clientes têm pelo menos 1 pagamento com valor acima de R$ 11,00?

**Tabelas utilizadas:** `customer`, `payment`

```
customer
+-------------+------------+-----------+
| customer_id | first_name | last_name |
+-------------+------------+-----------+
|           1 | Ana        | Souza     |
|           2 | Bruno      | Lima      |
|           3 | Carla      | Mendes    |
|           4 | Daniel     | Rocha     |
+-------------+------------+-----------+

payment
+------------+-------------+--------+
| payment_id | customer_id | amount |
+------------+-------------+--------+
|          1 |           1 |  15.00 |
|          2 |           1 |   5.00 |
|          3 |           2 |  12.00 |
|          4 |           3 |   8.00 |
|          5 |           4 |  10.00 |
+------------+-------------+--------+
```

---

### Query

```sql
SELECT
    first_name,
    last_name
FROM customer AS c
WHERE c.customer_id IN (
    SELECT p.customer_id
    FROM payment AS p
    WHERE p.amount > 11
)
ORDER BY
    first_name ASC,
    last_name ASC;
```


### Resultado
```
+------------+-----------+
| first_name | last_name |
+------------+-----------+
| Ana        | Souza     |
| Bruno      | Lima      |
+------------+-----------+
```

---

Dos 4 clientes da tabela, apenas Ana (customer_id 1) e Bruno (customer_id 2) têm pelo menos 1 pagamento acima
de R$ 11,00. Carla e Daniel ficaram de fora pois todos os seus pagamentos ficaram abaixo do limite. Vale notar
que Ana tem dois pagamentos (R$ 15,00 e R$ 5,00) — mesmo assim aparece apenas uma vez no resultado, pois o `IN`
verifica apenas se o `customer_id` está presente na lista, sem duplicar linhas. Esse é um padrão muito usado na
prática para cruzar informações entre tabelas quando um JOIN direto traria mais linhas do que o necessário.


### O que cada parte faz

- `SELECT first_name, last_name FROM customer AS c` — a query principal seleciona o nome e sobrenome de cada 
cliente da tabela `customer`.
- `WHERE c.customer_id IN (...)` — filtra os clientes cujo `customer_id` esteja presente na lista retornada
pela subquery. Apenas os clientes que aparecerem nessa lista passam para o resultado final.
- **Subquery (query interna):**
  - `SELECT p.customer_id FROM payment AS p` — seleciona o `customer_id` de cada pagamento da tabela `payment`.
  - `WHERE p.amount > 11` — filtra apenas os pagamentos com valor estritamente maior que R$ 11,00. Pagamentos 
  com valor exatamente igual a R$ 11,00 **não** entram — o operador `>` é estrito.
  - O resultado da subquery é uma lista de `customer_id` que fizeram ao menos 1 pagamento acima de R$ 11,00. 
  Se um cliente tiver 10 pagamentos mas apenas 1 deles for maior que R$ 11,00, ele ainda aparece na lista.
- `ORDER BY first_name ASC, last_name ASC` — ordena o resultado final em ordem alfabética pelo nome e, em caso
de empate, pelo sobrenome.



### Ordem de execução da query
```
1º → a subquery roda e analisa a tabela payment:
     amount 15.00 → customer_id 1 ✓ (15 > 11)
     amount  5.00 → customer_id 1 ✗ (5 não é > 11)
     amount 12.00 → customer_id 2 ✓ (12 > 11)
     amount  8.00 → customer_id 3 ✗ (8 não é > 11)
     amount 10.00 → customer_id 4 ✗ (10 não é > 11)

     lista retornada: [1, 2]

2º → a query principal filtra customer:
     WHERE customer_id IN (1, 2)

3º → resultado ordenado por first_name ASC, last_name ASC
```
