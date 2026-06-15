## DAY — Em quais dias do mês o faturamento total passou de R$ 25,00?

## Tabela utilizada
```
payments
+------------+---------------------+--------+
| payment_id | payment_date        | amount |
+------------+---------------------+--------+
| 1          | 2024-01-15 10:30:00 |  10.00 |
| 2          | 2025-03-22 18:45:00 |  20.00 |
| 3          | 2025-07-05 09:00:00 |  30.00 |
| 4          | 2026-09-10 14:20:00 |  40.00 |
| 5          | 2026-02-01 12:10:00 |  50.00 |
+------------+---------------------+--------+
```

### Query
```sql
SELECT
    EXTRACT(DAY FROM payment_date) AS dia_do_mes,
    COUNT(payment_id)              AS qnt_pagamentos,
    SUM(amount)                    AS tot_vendido,
    ROUND(AVG(amount), 2)          AS ticket_medio
FROM payments
GROUP BY
    EXTRACT(DAY FROM payment_date)
HAVING SUM(amount) > 25
ORDER BY
    tot_vendido DESC;
```

### Resultado
```
+------------+----------------+-------------+--------------+
| dia_do_mes | qnt_pagamentos | tot_vendido | ticket_medio |
+------------+----------------+-------------+--------------+
|          1 |              1 |       50.00 |        50.00 |
|         10 |              1 |       40.00 |        40.00 |
|          5 |              1 |       30.00 |        30.00 |
+------------+----------------+-------------+--------------+
```

Dos 5 dias com pagamentos registrados, apenas **3 superaram R$ 25,00**: dia 1 (R$ 50,00), dia 10 (R$ 40,00)
e dia 5 (R$ 30,00). Os dias 15 (R$ 10,00) e 22 (R$ 20,00) foram excluídos por ficarem abaixo do limite
definido no `HAVING`. Em uma base real, esse tipo de consulta é útil para identificar quais datas do mês
concentram os pagamentos de maior valor — informação relevante para planejamento de caixa e definição de
datas de vencimento.

---

### O que cada parte faz

- `EXTRACT(DAY FROM payment_date) AS dia_do_mes` — extrai apenas o número do dia dentro do mês da coluna
`payment_date`.
- `COUNT(payment_id) AS qnt_pagamentos` — conta quantos pagamentos ocorreram em cada dia do mês.
- `SUM(amount) AS tot_vendido` — soma o faturamento total de cada dia do mês.
- `ROUND(AVG(amount), 2) AS ticket_medio` — calcula a média dos valores de `amount` dentro de cada grupo
e arredonda para 2 casas decimais.
- `FROM payments` — define a tabela de origem dos dados.
- `GROUP BY EXTRACT(DAY FROM payment_date)` — agrupa os registros pelo dia do mês para que todas as 
funções de agregação operem por grupo.
- `HAVING SUM(amount) > 25` — filtra os grupos após o agrupamento, mantendo apenas os dias cujo faturamento
total seja maior que R$ 25,00. O `WHERE` não poderia ser usado aqui pois a condição depende de `SUM`,
que só existe depois do agrupamento.
- `ORDER BY tot_vendido DESC` — ordena pelo maior faturamento primeiro, facilitando a leitura dos dias
mais relevantes.


