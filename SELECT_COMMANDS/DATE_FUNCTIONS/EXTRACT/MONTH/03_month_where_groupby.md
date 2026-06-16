## MONTH — Quanto faturamos mês a mês apenas em 2025?

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
    EXTRACT(MONTH FROM payment_date) AS mes,
    COUNT(payment_id) AS qnt_pagamentos,
    SUM(amount) AS total_vendido
FROM payments
WHERE EXTRACT(YEAR FROM payment_date) = 2025
GROUP BY
    EXTRACT(MONTH FROM payment_date)
ORDER BY
    mes ASC;
```

### Resultado
```
+-----+----------------+--------------+
| mes | qnt_pagamentos | total_vendido|
+-----+----------------+--------------+
|   3 |              1 |        20.00 |
|   7 |              1 |        30.00 |
+-----+----------------+--------------+
```

Em 2025, a empresa registrou pagamentos em apenas **2 meses**: março (R$ 20,00) e julho (R$ 30,00).
O melhor mês do ano foi **julho**, com o maior faturamento entre os dois. Os demais meses do ano não
aparecem no resultado pois não houve nenhum pagamento registrado nesses períodos.

---

### O que cada parte faz

- `EXTRACT(MONTH FROM payment_date) AS mes` — extrai apenas o número do mês da coluna `payment_date` e exibe
o resultado com o apelido `mes`. Desta vez não extraímos o ano, pois já estamos filtrando por ele no `WHERE`.
- `COUNT(payment_id) AS qnt_pagamentos` — conta quantos pagamentos ocorreram em cada mês dentro do ano filtrado.
- `SUM(amount) AS total_vendido` — soma os valores de `amount` para cada mês, retornando o total faturado no período.
- `FROM payments` — define a tabela de origem dos dados.
- `WHERE EXTRACT(YEAR FROM payment_date) = 2025` — filtra os registros antes do agrupamento, mantendo apenas os pagamentos cujo ano seja 2025. Tudo fora desse ano é ignorado.
- `GROUP BY EXTRACT(MONTH FROM payment_date)` — agrupa os registros que passaram pelo filtro, separando-os por mês.
- `ORDER BY mes ASC` — ordena o resultado do mês mais antigo para o mais recente dentro do ano.



