## SUBQUERY — Quais filmes foram devolvidos entre os dias 29/05 e 30/05 de 2005?

**Tabelas utilizadas:** `film`, `inventory`, `rental`

```
film
+---------+-----------------+
| film_id | title           |
+---------+-----------------+
|       1 | Jurassic Park   |
|       2 | Titanic         |
|       3 | Matrix          |
|       4 | Gladiador       |
+---------+-----------------+

inventory
+--------------+---------+
| inventory_id | film_id |
+--------------+---------+
|            1 |       1 |
|            2 |       2 |
|            3 |       3 |
|            4 |       4 |
+--------------+---------+

rental
+-----------+--------------+---------------------+
| rental_id | inventory_id | return_date         |
+-----------+--------------+---------------------+
|         1 |            1 | 2005-05-29 10:00:00 |
|         2 |            2 | 2005-05-30 14:00:00 |
|         3 |            3 | 2005-06-01 09:00:00 |
|         4 |            4 | 2005-05-29 16:00:00 |
+-----------+--------------+---------------------+
```


### Query
```sql
SELECT
    f.title,
    f.film_id
FROM film AS f
WHERE f.film_id IN (
    SELECT
        i.film_id
    FROM inventory AS i
    INNER JOIN rental AS r
        ON r.inventory_id = i.inventory_id
    WHERE
        r.return_date >= '2005-05-29'
        AND r.return_date < '2005-05-31'
)
ORDER BY
    f.title ASC;
```

### Resultado
```
+-----------------+---------+
| title           | film_id |
+-----------------+---------+
| Gladiador       |       4 |
| Jurassic Park   |       1 |
| Titanic         |       2 |
+-----------------+---------+
```
---

A query encontrou 3 filmes devolvidos entre 29 e 30 de maio de 2005. A subquery foi necessária porque a 
informação de devolução (`return_date`) está na tabela `rental`, enquanto o título do filme está na tabela
`film` — e as duas não têm nenhuma coluna em comum para um JOIN direto. A tabela `inventory` serve como ponte
entre as duas: liga o `film_id` ao `inventory_id`, que por sua vez liga ao `rental`. A subquery resolve o
caminho intermediário e entrega à query principal apenas a lista de `film_id` relevantes, mantendo a query
externa simples e focada no resultado final


### O que cada parte faz

- `SELECT f.title, f.film_id FROM film AS f` — a query principal (outer query) seleciona o título e o id de
cada filme da tabela `film`.
- `WHERE f.film_id IN (...)` — **novo:** filtra os filmes da query principal usando o resultado de outra 
query, chamada de **subquery** (ou subconsulta). O operador `IN` verifica se o `film_id` de cada linha da 
`film` está presente na lista de ids retornada pela subquery. Pensa assim: a subquery roda primeiro, monta
uma lista de `film_id`, e a query principal usa essa lista como critério de filtro.
- **Subquery (query interna):**
  - `SELECT i.film_id FROM inventory AS i` — seleciona o `film_id` da tabela `inventory`, que faz a ligação 
  entre o filme e o registro de aluguel.
  - `INNER JOIN rental AS r ON r.inventory_id = i.inventory_id` — liga `inventory` com `rental` pelo 
  `inventory_id`, permitindo acessar a data de devolução de cada item.
  - `WHERE r.return_date >= '2005-05-29' AND r.return_date < '2005-05-31'` — filtra apenas os aluguéis 
  devolvidos a partir do dia 29/05 e antes do dia 31/05 — o que cobre exatamente os dias 29 e 30 de maio.
  Usar `< '2005-05-31'` em vez de `<= '2005-05-30'` é mais seguro quando a coluna armazena data e hora
  juntas: `<= '2005-05-30'` excluiria devoluções das 00:01h em diante do dia 30, enquanto `< '2005-05-31'`
  captura qualquer horário do dia 30.
- `ORDER BY f.title ASC` — ordena o resultado final em ordem alfabética pelo título do filme.



### Ordem de execução da query
```
1º → a subquery roda e retorna a lista de film_id devolvidos no período:
     film_id: [1, 2, 4]

2º → a query principal filtra a tabela film:
     WHERE film_id IN (1, 2, 4)

3º → o resultado é ordenado por título (ASC)
```
