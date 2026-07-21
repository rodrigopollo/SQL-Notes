## EXISTS — Quais clientes têm pelo menos 1 pagamento acima de R$ 11,00?

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

---

### Query

```sql
SELECT
    c.first_name,
    c.last_name
FROM customer AS c
WHERE EXISTS (
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

---

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

Dos 3 clientes, Ana e Bruno têm ao menos 1 pagamento
acima de R$ 11,00 (R$ 12,00 e R$ 15,00 respectivamente).
Carla ficou de fora pois seu único pagamento foi de
R$ 8,00. `EXISTS` não se preocupa com quantos registros
a subquery retorna — basta encontrar 1 para considerar
a condição verdadeira e incluir o cliente no resultado.


### O que cada parte faz

- `SELECT c.first_name, c.last_name FROM customer AS c`
  — a query principal seleciona nome e sobrenome de
  cada cliente da tabela `customer`.

- `WHERE EXISTS (...)` — **novo:** `EXISTS` verifica,
  para cada linha da query principal, se a subquery
  retorna ao menos 1 linha. Se retornar, o resultado
  é `TRUE` e o cliente é incluído. Se não retornar
  nenhuma linha, o resultado é `FALSE` e o cliente
  é excluído. `EXISTS` não usa a lista de valores
  retornados — só se importa se existe ou não existe.

- **Subquery (query interna):**
  - `SELECT customer_id FROM payment AS p` — seleciona
    registros da tabela `payment`.
  - `WHERE p.amount > 11` — filtra pagamentos acima
    de R$ 11,00.
  - `AND p.customer_id = c.customer_id` — **ponto
    chave:** liga a subquery à query principal pelo
    `customer_id`. Isso faz com que a subquery rode
    uma vez para cada cliente da query externa,
    verificando apenas os pagamentos daquele cliente
    específico. Esse tipo de subquery que referencia
    a query externa é chamada de **subquery
    correlacionada**.

- `ORDER BY c.first_name ASC, c.last_name ASC` —
  ordena o resultado por nome e, em caso de empate,
  pelo sobrenome.


### EXISTS vs IN — qual a diferença?

```
IN      → roda a subquery uma vez, monta uma lista
          e verifica se o valor está nela.

EXISTS  → roda a subquery uma vez POR LINHA da query
          principal, verificando apenas se existe
          ao menos 1 resultado para aquela linha.
```


O resultado desta query seria idêntico usando `IN`:
```sql
WHERE c.customer_id IN (
    SELECT p.customer_id
    FROM payment AS p
    WHERE p.amount > 11
)
```


A diferença é de comportamento interno: `EXISTS` para
de procurar assim que encontra o primeiro registro
válido, o que pode ser mais eficiente em tabelas
grandes com muitos registros por cliente.

---


### Ordem de execução
```
Para cada cliente da query principal:

  Ana (customer_id 1):
    subquery busca pagamentos de customer_id 1
    com amount > 11
    → encontrou payment_id 102 (12.00) ✓
    → EXISTS = TRUE → Ana incluída

  Bruno (customer_id 2):
    subquery busca pagamentos de customer_id 2
    com amount > 11
    → encontrou payment_id 104 (15.00) ✓
    → EXISTS = TRUE → Bruno incluído

  Carla (customer_id 3):
    subquery busca pagamentos de customer_id 3
    com amount > 11
    → nenhum encontrado ✗
    → EXISTS = FALSE → Carla excluída
```