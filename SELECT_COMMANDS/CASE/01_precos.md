## CASE EXPRESSION — Como categorizar filmes pelo valor do aluguel?

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


### Query
```sql
SELECT
    title,
    rental_rate,
    CASE rental_rate
        WHEN 0.99 THEN 'Barato'
        WHEN 2.99 THEN 'Médio'
        WHEN 4.99 THEN 'Caro'
        ELSE 'Outro'
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

A query categoriza cada filme como `Barato`, `Médio`
ou `Caro` com base no valor exato de `rental_rate`.
Nenhum filme caiu no `ELSE 'Outro'` pois todos os
valores existentes na tabela têm uma condição
correspondente. O resultado é apenas uma coluna de
exibição — nada é alterado na tabela.



### O que cada parte faz

- `CASE rental_rate` — **novo:** inicia um bloco
  `CASE EXPRESSION`. O valor da coluna `rental_rate`
  de cada linha é passado para ser comparado com
  os `WHEN`s abaixo. Funciona de forma parecida
  com o `if/elif/else` do Python:



```
Python:                     SQL:
if rate == 0.99:            CASE rental_rate
    return 'Barato'             WHEN 0.99 THEN 'Barato'
elif rate == 2.99:              WHEN 2.99 THEN 'Médio'
    return 'Médio'              WHEN 4.99 THEN 'Caro'
elif rate == 4.99:              ELSE 'Outro'
    return 'Caro'           END
else:
    return 'Outro'
```



- `WHEN 0.99 THEN 'Barato'` — se `rental_rate`
  for igual a `0.99`, retorna o texto `'Barato'`.
  O banco testa cada `WHEN` em ordem, do primeiro
  para o último, e para na primeira correspondência.

- `WHEN 2.99 THEN 'Médio'` — se `rental_rate`
  for igual a `2.99`, retorna `'Médio'`.

- `WHEN 4.99 THEN 'Caro'` — se `rental_rate`
  for igual a `4.99`, retorna `'Caro'`.

- `ELSE 'Outro'` — valor padrão retornado quando
  nenhum `WHEN` for satisfeito. Sem `ELSE`, o banco
  retornaria `NULL` para as linhas não cobertas.

- `END AS categoria` — encerra o bloco `CASE` e
  define o apelido da coluna de resultado.

---

### Limitação do CASE EXPRESSION
```
CASE EXPRESSION só testa igualdade (=).
Não é possível usar >, <, BETWEEN, IS NULL etc.

Para condições mais complexas, usa-se
CASE sem coluna — chamado de CASE SEARCHED,
que veremos no próximo exercício.
```