## TO_CHAR() — Alternativa: quantos pagamentos foram feitos nas segundas-feiras?

**Tabela utilizada:** `payments`

```
+------------+---------------------+--------+
| payment_id | payment_date        | amount |
+------------+---------------------+--------+
|          1 | 2025-01-15 10:30:00 |  10.00 |
|          2 | 2025-03-22 18:45:00 |  20.00 |
|          3 | 2025-07-05 09:00:00 |  30.00 |
|          4 | 2025-09-10 14:20:00 |  40.00 |
|          5 | 2026-02-01 12:10:00 |  50.00 |
+------------+---------------------+--------+
```


### Query
```sql
SELECT
    COUNT(payment_id)  AS qnt_pagamentos,
    'Segunda-feira'    AS dia_da_semana
FROM payments
WHERE EXTRACT(DOW FROM payment_date) = 1;
```


### Resultado
```
+----------------+---------------+
| qnt_pagamentos | dia_da_semana |
+----------------+---------------+
|              0 | Segunda-feira |
+----------------+---------------+
```


---

Esta alternativa é mais simples e direta quando a pergunta tem uma resposta única: "quantos pagamentos 
houve na segunda-feira?" — sem necessidade de agrupar por vários dias. A coluna `'Segunda-feira'` como 
texto fixo torna o resultado autoexplicativo, útil em relatórios onde o leitor precisa entender o resultado
sem ver a query que o gerou. Para checar um dia com resultados reais nesta tabela, substituir `= 1` por `= 3`
retornaria `2` pagamentos para quarta-feira.


### O que cada parte faz

- `COUNT(payment_id) AS qnt_pagamentos` — conta quantas linhas possuem valor em `payment_id` após o filtro
do `WHERE`. Diferente de `COUNT(*)`, que conta todas as linhas incluindo aquelas com valores nulos, 
`COUNT(payment_id)` conta apenas as linhas onde `payment_id` não é nulo. Na prática, como `payment_id`
é chave primária e nunca é nulo, os dois retornariam o mesmo valor aqui. Uma diferença importante: sem
`GROUP BY`, o `COUNT()` sempre retorna exatamente **1 linha** — mesmo que nenhuma linha passe pelo filtro,
o resultado é `0`, não vazio.
- `'Segunda-feira' AS dia_da_semana` — **novo:** cria uma coluna de exibição com um valor de texto fixo 
definido diretamente na query, sem vir de nenhuma coluna da tabela. Não cria nem altera nada na tabela —
existe apenas no resultado da consulta. É útil para tornar o resultado mais legível, especialmente quando
o filtro já define qual dia está sendo consultado.
- `FROM payments` — define a tabela de origem dos dados.
- `WHERE EXTRACT(DOW FROM payment_date) = 1` — filtra apenas os registros cujo `payment_date` caia numa 
segunda-feira. `DOW` (Day of Week) retorna um número de 0 a 6: 0 = domingo, 1 = segunda, 2 = terça, 
3 = quarta, 4 = quinta, 5 = sexta, 6 = sábado.


### Diferença em relação ao exercício anterior

|                      | Query com `GROUP BY`                | Esta query (sem `GROUP BY`)       |
|----------------------|-------------------------------------|-----------------------------------|
| Resultado sem linhas | retorna **0 linhas**                | retorna **1 linha com COUNT = 0** |
| Quando usar          | quando quer ver cada grupo separado | quando quer apenas o total geral  |



> Nenhum pagamento da tabela foi feito numa segunda-feira, por isso `qnt_pagamentos` retorna `0`. Diferente
da query com `GROUP BY`, que retornou 0 linhas, aqui o `COUNT()` sem agrupamento sempre garante ao menos 
1 linha no resultado — com o valor `0` quando nada passa pelo filtro.
