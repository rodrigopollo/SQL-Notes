## NOT EXISTS — Quais clientes não têm nenhum pagamento acima de R$ 11,00?

**Tabelas utilizadas:** `customer`, `payment`
```
customer
+-------------+------------+-----------+
| customer_id | first_name | last_name |
+-------------+------------+-----------+
|           1 | Ana        | Souza     |
|           2 | Bruno      | Lima      |
|           3 | Carla      | Mendes    |
+-------------+------------+-----------+

payment
+------------+-------------+--------+
| payment_id | customer_id | amount |
+------------+-------------+--------+
|        101 |           1 |  10.00 |
|        102 |           1 |  12.00 |
|        103 |           2 |   5.00 |
|        104 |           2 |  15.00 |
|        105 |           3 |   8.00 |
+------------+-------------+--------+
```


### Query

```sql
SELECT
    c.first_name,
    c.last_name
FROM customer AS c
WHERE NOT EXISTS (
    SELECT customer_id
    FROM payment AS p
    WHERE
        p.amount > 11
        AND p.customer_id = c.customer_id
)
ORDER BY
    c.first_name ASC,
    c.last_name ASC;
```



### Resultado

```
+------------+-----------+
| first_name | last_name |
+------------+-----------+
| Carla      | Mendes    |
+------------+-----------+
```

---

Dos 3 clientes, apenas Carla não tem nenhum pagamento
acima de R$ 11,00 — seu único registro é de R$ 8,00.
Ana e Bruno foram excluídos pois têm ao menos 1
pagamento acima do limite (R$ 12,00 e R$ 15,00
respectivamente). `NOT EXISTS` é o oposto direto de
`EXISTS`: inclui o cliente no resultado quando a
subquery não encontra nenhuma linha.



### O que cada parte faz

- `SELECT c.first_name, c.last_name FROM customer AS c`
  — a query principal seleciona nome e sobrenome de
  cada cliente da tabela `customer`.

- `WHERE NOT EXISTS (...)` — **novo:** `NOT EXISTS` é
  o oposto de `EXISTS`. Para cada linha da query
  principal, verifica se a subquery retorna ao menos
  1 resultado. Se **não** retornar nenhuma linha,
  o resultado é `TRUE` e o cliente é incluído. Se
  retornar ao menos 1 linha, o resultado é `FALSE`
  e o cliente é excluído.

- **Subquery (query interna):**
  - `SELECT customer_id FROM payment AS p` — busca
    registros na tabela `payment`.
  - `WHERE p.amount > 11` — filtra pagamentos acima
    de R$ 11,00.
  - `AND p.customer_id = c.customer_id` — liga a
    subquery à query principal, verificando apenas
    os pagamentos do cliente sendo avaliado naquele
    momento.

- `ORDER BY c.first_name ASC, c.last_name ASC` —
  ordena por nome e, em caso de empate, pelo sobrenome.

---

### EXISTS vs NOT EXISTS — resumo rápido

```
EXISTS     → inclui a linha se a subquery
             retornar AO MENOS 1 resultado.

NOT EXISTS → inclui a linha se a subquery
             retornar ZERO resultados.
```

---

### Ordem de execução
```
Para cada cliente da query principal:

  Ana (customer_id 1):
    subquery busca pagamentos de customer_id 1
    com amount > 11
    → encontrou payment_id 102 (12.00) ✓
    → NOT EXISTS = FALSE → Ana excluída

  Bruno (customer_id 2):
    subquery busca pagamentos de customer_id 2
    com amount > 11
    → encontrou payment_id 104 (15.00) ✓
    → NOT EXISTS = FALSE → Bruno excluído

  Carla (customer_id 3):
    subquery busca pagamentos de customer_id 3
    com amount > 11
    → nenhum encontrado ✗
    → NOT EXISTS = TRUE → Carla incluída ✓
```