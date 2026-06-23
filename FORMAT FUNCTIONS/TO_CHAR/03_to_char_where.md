## TO_CHAR() — Quantos pagamentos foram feitos nas segundas-feiras?

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
    COUNT(payment_id)                  AS qnt_pagamentos,
    TO_CHAR(payment_date, 'FMDay')     AS dia_da_semana
FROM payments
WHERE
    EXTRACT(DOW FROM payment_date) = 1
GROUP BY
    TO_CHAR(payment_date, 'FMDay');
```


### Resultado
```
+----------------+---------------+
| qnt_pagamentos | dia_da_semana |
+----------------+---------------+
(0 linhas)
+----------------+---------------+
```

---

A query combina três recursos: `EXTRACT(DOW ...)` para filtrar pelo dia da semana antes do agrupamento,
`TO_CHAR()` para exibir o nome do dia por extenso, e `COUNT()` para contar os pagamentos agrupados. 
Em uma base real com muitos registros, esse tipo de consulta é útil para identificar padrões de comportamento
por dia da semana — por exemplo, verificar se pagamentos se concentram no início ou no fim da semana.


### O que cada parte faz

- `COUNT(payment_id) AS qnt_pagamentos` — conta quantos pagamentos ocorreram no dia da semana filtrado.
- `TO_CHAR(payment_date, 'FMDay') AS dia_da_semana` — converte a data para o nome do dia da semana por 
extenso em inglês. A máscara `'Day'` retorna o nome capitalizado; o prefixo `FM` (fill mode) remove os 
espaços em branco que o PostgreSQL adiciona à direita para alinhar os nomes (sem FM, "Monday" viria como
"Monday   ").
- `FROM payments` — define a tabela de origem dos dados.
- `WHERE EXTRACT(DOW FROM payment_date) = 1` — **novo:** `DOW` significa *Day of Week* (dia da semana).
`EXTRACT(DOW ...)` retorna um número de 0 a 6, onde: 0 = domingo, 1 = segunda, 2 = terça, 3 = quarta,
4 = quinta, 5 = sexta, 6 = sábado. O filtro `= 1` mantém apenas os registros cujo `payment_date` caia
numa segunda-feira.
- `GROUP BY TO_CHAR(payment_date, 'FMDay')` — agrupa os registros que passaram pelo `WHERE` pelo nome do
dia da semana, permitindo o uso de `COUNT()` no `SELECT`.
