# YEAR — Lucro bruto recebido por ano

## Tabela
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
    EXTRACT(YEAR FROM payment_date) AS ano,
    COUNT(payment_id)               AS qnt_pagamentos,
    SUM(amount)                     AS tot_lucro_bruto
FROM payments
GROUP BY EXTRACT(YEAR FROM payment_date)
ORDER BY ano;
```


## Resultado
```
+------+----------------+-----------------+
| ano  | qnt_pagamentos | tot_lucro_bruto |
+------+----------------+-----------------+
| 2024 | 1              | 10.00           |
| 2025 | 2              | 50.00           |
| 2026 | 2              | 90.00           |
+------+----------------+-----------------+
```

---

## O que cada parte faz
- `EXTRACT(YEAR FROM payment_date) AS ano` — extrai o ano de cada pagamento e nomeia a coluna como `ano`.
- `COUNT(payment_id) AS qnt_pagamentos` — conta quantos pagamentos ocorreram em cada ano.
- `SUM(amount) AS tot_lucro_bruto` — soma os valores de todos os pagamentos de cada ano.
- `GROUP BY EXTRACT(YEAR FROM payment_date)` — agrupa as linhas por ano, para que o `COUNT` e o `SUM` operem
separadamente em cada um.
- `ORDER BY ano` — ordena o resultado do ano mais antigo para o mais recente.



