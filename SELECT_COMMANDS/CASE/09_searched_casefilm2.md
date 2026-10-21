## CASE EXPRESSION + GROUP BY — Quantos filmes existem em cada categoria de preço?

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
    CASE rental_rate
        WHEN 0.99 THEN 'Oferta'
        WHEN 2.99 THEN 'Normal'
        WHEN 4.99 THEN 'Lançamento'
        ELSE 'outros valores'
    END AS categoria,
    COUNT(*) AS quantidade
FROM film
GROUP BY
    CASE rental_rate
        WHEN 0.99 THEN 'Oferta'
        WHEN 2.99 THEN 'Normal'
        WHEN 4.99 THEN 'Lançamento'
        ELSE 'outros valores'
    END
ORDER BY
    categoria DESC;
```


### Resultado
```
+------------+------------+
| categoria  | quantidade |
+------------+------------+
| Oferta     |          3 |
| Normal     |          2 |
| Lançamento |          2 |
+------------+------------+
```

---

A query conta quantos filmes existem em cada
categoria de preço. Diferente dos exercícios
anteriores onde o `CASE` exibia uma categoria
por linha, aqui ele é combinado com `COUNT(*)`
e `GROUP BY` para agregar os dados — entregando
um resumo do catálogo inteiro em apenas 3 linhas.
O `ORDER BY categoria DESC` ordena as categorias
em ordem alfabética decrescente (O > N > L).



### O que cada parte faz

- `CASE rental_rate ... END AS categoria` —
  classifica cada filme em uma categoria com
  base no valor de `rental_rate`. Funciona
  igual aos exercícios anteriores.

- `COUNT(*) AS quantidade` — conta quantos
  filmes existem em cada grupo formado pelo
  `GROUP BY`. `COUNT(*)` conta todas as linhas
  do grupo, incluindo as com valores nulos.

- `GROUP BY CASE rental_rate ... END` —
  **ponto chave:** o `GROUP BY` precisa repetir
  a expressão `CASE` completa porque o
  PostgreSQL não permite usar o alias
  (`categoria`) no `GROUP BY` — ele processa
  o `GROUP BY` antes de calcular os aliases
  do `SELECT`.

- `ORDER BY categoria DESC` — aqui sim é
  possível usar o alias, pois o `ORDER BY`
  é processado depois do `SELECT`. Ordena
  alfabeticamente de forma decrescente:
  Oferta (O) → Normal (N) → Lançamento (L).

---

### Duas formas de usar CASE — comparação
```
Forma 1 — linha a linha (exercícios anteriores):
  Mostra a categoria de cada filme individualmente.
  Resultado: 1 linha por filme.

  +------------------+-------------+-----------+
  | title            | rental_rate | categoria |
  +------------------+-------------+-----------+
  | Academy Dinosaur |        0.99 | Oferta    |
  | Ace Goldfinger   |        4.99 | Lançamento|
  | Adaptation Holes |        2.99 | Normal    |
  +------------------+-------------+-----------+

Forma 2 — agrupado com COUNT (este exercício):
  Mostra quantos filmes existem por categoria.
  Resultado: 1 linha por categoria.

  +------------+------------+
  | categoria  | quantidade |
  +------------+------------+
  | Oferta     |          3 |
  | Normal     |          2 |
  | Lançamento |          2 |
  +------------+------------+
```



### Por que o GROUP BY repete o CASE inteiro
```sql
-- ERRADO → PostgreSQL não aceita alias no GROUP BY:
GROUP BY categoria

-- CORRETO → repetir a expressão completa:
GROUP BY
    CASE rental_rate
        WHEN 0.99 THEN 'Oferta'
        WHEN 2.99 THEN 'Normal'
        WHEN 4.99 THEN 'Lançamento'
        ELSE 'outros valores'
    END
```