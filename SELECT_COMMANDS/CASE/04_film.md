## CASE EXPRESSION — Como traduzir classificações etárias de filmes?

**Tabela utilizada:** `film`
```
film
+---------+------------------+--------+
| film_id | title            | rating |
+---------+------------------+--------+
|       1 | Academy Dinosaur | PG     |
|       2 | Ace Goldfinger   | G      |
|       3 | Adaptation Holes | NC-17  |
|       4 | Affair Prejudice | G      |
|       5 | African Egg      | R      |
|       6 | Agent Truman     | PG-13  |
+---------+------------------+--------+
```



### Query
```sql
SELECT
    title,
    rating,
    CASE rating
        WHEN 'G'     THEN 'Livre'
        WHEN 'PG'    THEN 'Recomendado para maiores de 10'
        WHEN 'PG-13' THEN 'Recomendado para maiores de 13'
        WHEN 'R'     THEN 'Maiores de 17'
        WHEN 'NC-17' THEN 'Somente adultos'
        ELSE 'Classificação desconhecida'
    END AS classificacao
FROM film;
```



### Resultado
```
+------------------+--------+--------------------------------+
| title            | rating | classificacao                  |
+------------------+--------+--------------------------------+
| Academy Dinosaur | PG     | Recomendado para maiores de 10 |
| Ace Goldfinger   | G      | Livre                          |
| Adaptation Holes | NC-17  | Somente adultos                |
| Affair Prejudice | G      | Livre                          |
| African Egg      | R      | Maiores de 17                  |
| Agent Truman     | PG-13  | Recomendado para maiores de 13 |
+------------------+--------+--------------------------------+
```

### Interpretação

A query traduz os códigos de classificação etária
americanos (`G`, `PG`, `PG-13`, `R`, `NC-17`) para
descrições mais claras em português. O banco armazena
os códigos curtos por serem padronizados e compactos
— o `CASE` faz a tradução apenas na exibição. O
`ELSE` cobre qualquer código inesperado que possa
existir na tabela, evitando `NULL` silencioso.



### O que cada parte faz

- `CASE rating` — passa o valor de `rating` de
  cada linha para ser comparado com os `WHEN`s
  abaixo, testando igualdade em ordem.

- `WHEN 'G' THEN 'Livre'` — classificação livre,
  indicada para todos os públicos.

- `WHEN 'PG' THEN 'Recomendado para maiores de 10'`
  — presença dos pais sugerida para menores.

- `WHEN 'PG-13' THEN 'Recomendado para maiores
  de 13'` — conteúdo inapropriado para menores
  de 13 anos.

- `WHEN 'R' THEN 'Maiores de 17'` — menores de
  17 anos só com acompanhamento de adultos.

- `WHEN 'NC-17' THEN 'Somente adultos'` — proibido
  para menores de 17 anos.

- `ELSE 'Classificação desconhecida'` — cobre
  qualquer valor fora dos cinco códigos esperados.

- `END AS classificacao` — encerra o bloco `CASE`
  e nomeia a coluna de resultado.

---

### Comparação dos três exemplos de CASE EXPRESSION
```
rental_rate → número decimal  → 0.99, 2.99, 4.99
status_code → número inteiro  → 1, 2, 3
sex         → texto curto     → 'M', 'F'
rating      → texto curto     → 'G', 'PG', 'R'...

Em todos os casos, CASE EXPRESSION só funciona
com igualdade (=) e valores fixos conhecidos.
Para comparações com >, <, BETWEEN ou IS NULL
→ usar CASE SEARCHED (próximo exercício).
```