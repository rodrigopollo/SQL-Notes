# YEAR — Contando quantos anos têm pagamentos

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
    COUNT(DISTINCT EXTRACT(YEAR FROM payment_date)) AS total_anos
FROM
    payments;
```

## Resultado
```
+------------+
| total_anos |
+------------+
| 3          |
+------------+
```

---

## O que cada parte faz
- `EXTRACT(YEAR FROM payment_date)` — extrai o ano de cada linha da tabela.
- `DISTINCT` — garante que anos repetidos (como 2025 e 2026, que aparecem duas vezes) sejam contados
apenas uma vez.
- `COUNT(...)` — conta quantos anos únicos existem no resultado.
- `AS total_anos` — renomeia a coluna do resultado para `total_anos`.

A tabela tem pagamentos em 3 anos distintos: 2024, 2025 e 2026.