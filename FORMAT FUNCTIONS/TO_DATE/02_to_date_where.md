## TO_DATE() — Quais pagamentos foram realizados a partir de 01/06/2025?

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
    payment_id,
    payment_date,
    amount
FROM payments
WHERE payment_date >= TO_DATE('01/06/2025', 'DD/MM/YYYY');
```


### Resultado
```
+------------+---------------------+--------+
| payment_id | payment_date        | amount |
+------------+---------------------+--------+
|          3 | 2025-07-05 09:00:00 |  30.00 |
|          4 | 2025-09-10 14:20:00 |  40.00 |
|          5 | 2026-02-01 12:10:00 |  50.00 |
+------------+---------------------+--------+
```

---

Dos 5 pagamentos da tabela, 3 foram realizados a partir de 01/06/2025: julho/2025, setembro/2025 e
fevereiro/2026. Os `payment_id` 1 e 2 (janeiro e março/2025) ficaram de fora por serem anteriores à data
de corte. Este é o uso mais comum de `TO_DATE()` no dia a dia: quando a data de filtro vem de fora do
banco — digitada pelo usuário, recebida de um formulário ou lida de um arquivo — sempre como texto,
e precisa ser convertida antes de ser comparada com colunas do tipo `date` ou `timestamp`.


### O que cada parte faz

- `payment_id, payment_date, amount` — colunas trazidas diretamente da tabela, sem nenhuma transformação.
- `FROM payments` — define a tabela de origem dos dados.
- `WHERE payment_date >= TO_DATE('01/06/2025', 'DD/MM/YYYY')` — aqui está o uso prático de `TO_DATE()`:
o texto `'01/06/2025'` é convertido em uma data real antes de ser comparado com `payment_date`. 
Sem `TO_DATE()`, o banco estaria comparando uma data com um texto — o que geraria erro ou resultados incorretos. A máscara `'DD/MM/YYYY'` instrui o banco a interpretar o texto como dia, mês e ano nessa ordem. O operador `>=` filtra apenas os pagamentos cuja data seja igual ou posterior a 01/06/2025.
