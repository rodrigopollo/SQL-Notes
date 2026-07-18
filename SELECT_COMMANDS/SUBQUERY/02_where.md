## SUBQUERY — Quais clientes nunca fizeram nenhum pagamento?

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
|           5 | Elisa      | Cunha     |
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


### Query

```sql
SELECT
    first_name,
    last_name
FROM customer AS c
WHERE c.customer_id NOT IN (
    SELECT p.customer_id
    FROM payment AS p
)
ORDER BY
    first_name ASC;
```


### Resultado
```
+------------+-----------+
| first_name | last_name |
+------------+-----------+
| Elisa      | Cunha     |
+------------+-----------+
```

---


Dos 5 clientes cadastrados, apenas Elisa (customer_id 5) não tem nenhum registro na tabela `payment`. 
Os outros 4 aparecem ao menos uma vez em `payment` e por isso foram
excluídos pelo `NOT IN`. Esse tipo de consulta é útil na prática para identificar clientes inativos, 
leads que nunca converteram, ou registros órfãos entre tabelas.


### O que cada parte faz

- `SELECT first_name, last_name FROM customer AS c` —
  a query principal seleciona nome e sobrenome de cada
  cliente da tabela `customer`.

- `WHERE c.customer_id NOT IN (...)` — **novo:** `NOT IN`
  é o oposto de `IN`. Em vez de filtrar os clientes que
  estão na lista retornada pela subquery, ele filtra os
  que **não estão**. Se o `customer_id` aparecer em
  `payment`, o cliente é excluído do resultado.

- **Subquery (query interna):**
  - `SELECT p.customer_id FROM payment AS p` — retorna
    todos os `customer_id` que têm ao menos 1 registro
    em `payment`.
  - O resultado é a lista `[1, 2, 3, 4]` — todos os
    clientes que já pagaram ao menos uma vez.

- `ORDER BY first_name ASC` — ordena o resultado final
  em ordem alfabética pelo nome.



### Ordem de execução
```
1º → a subquery roda e retorna os customer_id
     que existem em payment:
     lista retornada: [1, 2, 3, 4]

2º → a query principal aplica NOT IN:
     customer_id 1 → está na lista → excluído
     customer_id 2 → está na lista → excluído
     customer_id 3 → está na lista → excluído
     customer_id 4 → está na lista → excluído
     customer_id 5 → NÃO está na lista → incluído ✓

3º → resultado ordenado por first_name ASC
```