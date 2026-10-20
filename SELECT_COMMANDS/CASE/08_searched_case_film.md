## SEARCHED CASE — Como agrupar múltiplas classificações em uma única condição?

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
    CASE
        WHEN rating IN ('PG', 'PG-13') THEN 'Livre'
        WHEN rating = 'R'              THEN 'Adulto'
        ELSE 'Outro'
    END AS classificacao
FROM film;
```


### Resultado
```
+------------------+--------+---------------+
| title            | rating | classificacao |
+------------------+--------+---------------+
| Academy Dinosaur | PG     | Livre         |
| Ace Goldfinger   | G      | Outro         |
| Adaptation Holes | NC-17  | Outro         |
| Affair Prejudice | G      | Outro         |
| African Egg      | R      | Adulto        |
| Agent Truman     | PG-13  | Livre         |
+------------------+--------+---------------+
```

---

A query agrupa `PG` e `PG-13` em uma única categoria
`'Livre'` usando `IN` dentro do `WHEN`. Isso seria
impossível no `CASE EXPRESSION` — ele só aceita um
valor por `WHEN`, forçando a migração para o
`SEARCHED CASE`. `G` e `NC-17` caíram no `ELSE
'Outro'` por não terem condição correspondente.



### O que cada parte faz

- `CASE` sem coluna — inicia um `SEARCHED CASE`,
  permitindo qualquer operador dentro dos `WHEN`s.

- `WHEN rating IN ('PG', 'PG-13') THEN 'Livre'`
  — **ponto chave:** `IN` verifica se `rating`
  é igual a qualquer um dos valores da lista.
  Isso agrupa dois ratings em uma única condição
  — impossível no `CASE EXPRESSION`, que só
  aceita um valor por `WHEN`.

- `WHEN rating = 'R' THEN 'Adulto'` — testa
  igualdade simples para o rating `'R'`.

- `ELSE 'Outro'` — cobre `'G'` e `'NC-17'`,
  que não têm condição explícita.

- `END AS classificacao` — encerra o bloco
  `CASE` e nomeia a coluna de resultado.



### Por que CASE EXPRESSION não resolve aqui

```sql
-- CASE EXPRESSION → só aceita um valor por WHEN:
CASE rating
    WHEN 'PG'    THEN 'Livre'  -- linha separada
    WHEN 'PG-13' THEN 'Livre'  -- linha separada
    WHEN 'R'     THEN 'Adulto'
END

-- SEARCHED CASE → agrupa os dois em um WHEN só:
CASE
    WHEN rating IN ('PG', 'PG-13') THEN 'Livre'
    WHEN rating = 'R'              THEN 'Adulto'
END

-- Mesmo resultado, mas o SEARCHED CASE é mais
-- limpo quando vários valores mapeiam para
-- a mesma categoria.
```

---

### Outros operadores que forçam o SEARCHED CASE

```
IN ('A', 'B', 'C')  → múltiplos valores
NOT IN (...)        → exclusão de valores
BETWEEN x AND y     → faixa de valores
IS NULL             → verificar vazio
IS NOT NULL         → verificar preenchido
>, <, >=, <=        → comparações numéricas
LIKE '%texto%'      → busca por padrão
AND / OR            → condições combinadas
```