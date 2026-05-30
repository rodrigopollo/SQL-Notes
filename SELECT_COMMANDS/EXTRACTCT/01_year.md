# YEAR — Extraindo o Ano de uma Data

## Objetivo
Ver quais anos têm pagamentos registrados, sem repetições e em ordem crescente.

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
SELECT DISTINCT
    EXTRACT(YEAR FROM payment_date) AS ano
FROM payments
ORDER BY ano;


## Resultado
+------+
| ano  |
+------+
| 2024 |
| 2025 |
| 2026 |
+------+

---

## O que cada parte faz

- `EXTRACT(YEAR FROM payment_date)` — extrai apenas o ano do campo `payment_date`.
- `AS ano` — renomeia a coluna do resultado para `ano`.
- `DISTINCT` — remove anos duplicados. Como 2025 e 2026 aparecem mais de uma vez na tabela, sem o
`DISTINCT` eles apareceriam repetidos no resultado.
- `ORDER BY ano` — ordena o resultado do menor para o maior ano.


## Observações
- `EXTRACT` funciona com outras partes da data alem de `YEAR`, como `MONTH`, `DAY`, `HOUR`, entre outros.
- `DISTINCT` atua **depois** do `EXTRACT`, ou seja, elimina anos repetidos já no valor extraído, nao nas 
datas originais.