## SEARCHED CASE — Como categorizar filmes usando operadores de comparação?

**Tabela utilizada:** `film`
```
film
+---------+------------------+-------------+
| film_id | title            | rental_rate |
+---------+------------------+-------------+
|       1 | Academy Dinosaur |        0.99 |
|       2 | Ace Goldfinger   |        4.99 |
|       3 | Adaptation Holes |        2.99 |
|       4 | Affair Prejudice |        4.99 |
|       5 | African Egg      |        2.99 |
+---------+------------------+-------------+
```

> `SEARCHED CASE`
>  variação do `CASE` que aceita qualquer operador de comparação, não so igualdade.


### Query
```sql
SELECT
    title,
    rental_rate,
    CASE
        WHEN rental_rate = 0.99 THEN 'Barato'
        WHEN rental_rate BETWEEN 1.00 AND 3.00 THEN 'Médio'
        WHEN rental_rate > 3.00 THEN 'Caro'
        ELSE 'Desconhecido'
    END AS categoria
FROM film;
```


### Resultado
```
+------------------+-------------+-----------+
| title            | rental_rate | categoria |
+------------------+-------------+-----------+
| Academy Dinosaur |        0.99 | Barato    |
| Ace Goldfinger   |        4.99 | Caro      |
| Adaptation Holes |        2.99 | Médio     |
| Affair Prejudice |        4.99 | Caro      |
| African Egg      |        2.99 | Médio     |
+------------------+-------------+-----------+
```

---

A query categoriza cada filme usando comparações
mais flexíveis do que o `CASE EXPRESSION` permitia.
`BETWEEN` cobre uma faixa de valores, `>` cobre
tudo acima de um limite — nenhum desses operadores
é possível no `CASE EXPRESSION`. O banco testa
cada `WHEN` em ordem e para na primeira condição
verdadeira. O `ELSE` cobre qualquer valor que não
se encaixe em nenhuma das condições anteriores.



### O que cada parte faz

- `CASE` sem coluna — **novo:** diferente do
  `CASE EXPRESSION` que recebia uma coluna logo
  após (`CASE rental_rate`), o `SEARCHED CASE`
  não tem coluna após `CASE`. Cada `WHEN` escreve
  a condição completa por conta própria.

- `WHEN rental_rate = 0.99 THEN 'Barato'` —
  testa igualdade exata. Mesmo operador do
  `CASE EXPRESSION`, mas aqui a coluna é
  escrita dentro do `WHEN`.

- `WHEN rental_rate BETWEEN 1.00 AND 3.00
  THEN 'Médio'` — **novo no CASE:** `BETWEEN`
  não é possível no `CASE EXPRESSION`. Aqui
  cobre qualquer valor entre 1.00 e 3.00,
  inclusive os extremos.

- `WHEN rental_rate > 3.00 THEN 'Caro'` —
  operador `>` também impossível no
  `CASE EXPRESSION`. Cobre qualquer valor
  acima de 3.00.

- `ELSE 'Desconhecido'` — cobre qualquer valor
  que não satisfaça nenhum `WHEN` anterior.

- `END AS categoria` — encerra o bloco `CASE`
  e nomeia a coluna de resultado.

---

### CASE EXPRESSION vs SEARCHED CASE
```
CASE EXPRESSION          SEARCHED CASE
→ coluna após CASE       → sem coluna após CASE
→ só igualdade (=)       → qualquer operador
→ valores fixos          → faixas e condições

CASE rental_rate         CASE
    WHEN 0.99 THEN ...       WHEN rental_rate = 0.99
    WHEN 2.99 THEN ...       WHEN rental_rate > 3.00
END                          WHEN rental_rate BETWEEN
                         END

Operadores disponíveis no SEARCHED CASE:
  =, <>, !=, >, <, >=, <=
  BETWEEN, IN, NOT IN
  IS NULL, IS NOT NULL
  LIKE, ILIKE
  AND, OR
```