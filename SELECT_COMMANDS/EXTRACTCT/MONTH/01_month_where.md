# MONTH — Total vendido por mês em 2025

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

## Query
```sql
SELECT
    EXTRACT(MONTH FROM payment_date) AS mes,
    COUNT(payment_id)                AS qnt_pagamentos,
    SUM(amount)                      AS total_vendido
FROM payments
WHERE EXTRACT(YEAR FROM payment_date) = 2025
GROUP BY EXTRACT(MONTH FROM payment_date)
ORDER BY mes ASC;
```

## Resultado
```
+-----+----------------+---------------+
| mes | qnt_pagamentos | total_vendido |
+-----+----------------+---------------+
| 3   | 1              | 20.00         |
| 7   | 1              | 30.00         |
+-----+----------------+---------------+
```
Em 2025 tivemos:
- Março (mês 3): 1 pagamento de R$ 20,00.
- Julho (mês 7): 1 pagamento de R$ 30,00.

---

## O que cada parte faz
- `EXTRACT(MONTH FROM payment_date) AS mes` — extrai o número do mês de cada pagamento.
- `COUNT(payment_id) AS qnt_pagamentos` — conta quantos pagamentos ocorreram em cada mês.
- `SUM(amount) AS total_vendido` — soma o valor de todos os pagamentos de cada mês.
- `WHERE EXTRACT(YEAR FROM payment_date) = 2025` — filtra apenas os registros do ano de 2025,
antes de qualquer agrupamento.
- `GROUP BY EXTRACT(MONTH FROM payment_date)` — agrupa os registros por mês para que `COUNT` e `SUM` 
operem separadamente em cada um.
- `ORDER BY mes ASC` — ordena o resultado do mês mais antigo para o mais recente. `ASC` significa ordem 
crescente e é o comportamento padrão do `ORDER BY`, mas deixá-lo explícito torna a intenção mais clara.





