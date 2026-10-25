## CASE EXPRESSION + SUM — Contagem de filmes por categoria em colunas separadas?

**Tabela utilizada:** `film`
```
film (amostra)
+---------+------------------+-------------+
| film_id | title            | rental_rate |
+---------+------------------+-------------+
|       1 | Academy Dinosaur |        0.99 |
|       2 | Ace Goldfinger   |        4.99 |
|       3 | Adaptation Holes |        2.99 |
|       4 | Affair Prejudice |        4.99 |
|       5 | African Egg      |        2.99 |
|       6 | Agent Truman     |        0.99 |
|       7 | Airplane Sierra  |        0.99 |
+---------+------------------+-------------+
```


### Query
```sql
SELECT
    SUM(CASE rental_rate
            WHEN 0.99 THEN 1
            ELSE 0
        END) AS oferta,

    SUM(CASE rental_rate
            WHEN 2.99 THEN 1
            ELSE 0
        END) AS normal,

    SUM(CASE rental_rate
            WHEN 4.99 THEN 1
            ELSE 0
        END) AS lancamento
FROM film;
```


### Resultado
```
+--------+--------+------------+
| oferta | normal | lancamento |
+--------+--------+------------+
|      3 |      2 |          2 |
+--------+--------+------------+
```

---

A query conta quantos filmes existem em cada
categoria de preço, mas exibe o resultado em
colunas separadas em vez de linhas separadas.
Isso é chamado de **pivot** — girar os dados
de linhas para colunas. O resultado inteiro
cabe em 1 única linha, o que facilita leitura
em dashboards e relatórios executivos. A lógica
é simples: para cada filme, o `CASE` retorna
`1` se ele pertence àquela categoria ou `0`
se não pertence — o `SUM` soma esses valores
e entrega o total.



### O que cada parte faz

- `SUM(CASE rental_rate WHEN 0.99 THEN 1
  ELSE 0 END) AS oferta` — para cada linha
  da tabela, o `CASE` retorna `1` se
  `rental_rate` for `0.99` ou `0` caso
  contrário. O `SUM` soma todos esses `1`s
  e `0`s, entregando o total de filmes
  em oferta.

- `SUM(CASE rental_rate WHEN 2.99 THEN 1
  ELSE 0 END) AS normal` — mesma lógica
  para `rental_rate = 2.99`.

- `SUM(CASE rental_rate WHEN 4.99 THEN 1
  ELSE 0 END) AS lancamento` — mesma lógica
  para `rental_rate = 4.99`.

- `FROM film` — define a tabela de origem.
  Sem `GROUP BY` — o `SUM` agrega todos os
  registros da tabela de uma vez, retornando
  sempre 1 linha no resultado.

---

### Como o SUM conta cada filme
```
film_id 1 → rental_rate 0.99:
  oferta     → CASE retorna 1 ✓
  normal     → CASE retorna 0
  lancamento → CASE retorna 0

film_id 2 → rental_rate 4.99:
  oferta     → CASE retorna 0
  normal     → CASE retorna 0
  lancamento → CASE retorna 1 ✓

SUM acumula os 1s de cada coluna:
  oferta     → 1+0+0+0+0+1+1 = 3
  normal     → 0+0+1+0+1+0+0 = 2
  lancamento → 0+1+0+1+0+0+0 = 2
```



### Exercício anterior vs este — duas formas de organizar
```
Exercício anterior → resultado VERTICAL:
  1 linha por categoria, sem limite de categorias

  +------------+------------+
  | categoria  | quantidade |
  +------------+------------+
  | Oferta     |          3 |
  | Normal     |          2 |
  | Lançamento |          2 |
  +------------+------------+

Este exercício → resultado HORIZONTAL (pivot):
  1 linha só, 1 coluna por categoria

  +--------+--------+------------+
  | oferta | normal | lancamento |
  +--------+--------+------------+
  |      3 |      2 |          2 |
  +--------+--------+------------+

Quando usar cada um:
  Vertical  → muitas categorias, relatórios
              detalhados, fácil de filtrar
  Horizontal→ poucas categorias fixas,
              dashboards, comparação rápida
```