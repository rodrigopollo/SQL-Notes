## DATE_ADD() — Qual seria a data de cada pagamento somando 7 dias?

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
    DATE_ADD(payment_date, INTERVAL 7 DAY) AS plus_7_days
FROM payments;
```

### Resultado
```
+------------+---------------------+---------------------+
| payment_id | payment_date        | plus_7_days         |
+------------+---------------------+---------------------+
|          1 | 2025-01-15 10:30:00 | 2025-01-22 10:30:00 |
|          2 | 2025-03-22 18:45:00 | 2025-03-29 18:45:00 |
|          3 | 2025-07-05 09:00:00 | 2025-07-12 09:00:00 |
|          4 | 2025-09-10 14:20:00 | 2025-09-17 14:20:00 |
|          5 | 2026-02-01 12:10:00 | 2026-02-08 12:10:00 |
+------------+---------------------+---------------------+
```

---

### Interpretação

A query projeta uma nova data para cada pagamento, somando 7 dias à `payment_date` original. 
O horário é preservado em todos os registros. Esse tipo de operação é comum em situações reais como
calcular datas de vencimento, prazos de entrega, períodos de garantia ou janelas de reembolso — por exemplo,
uma política de devolução de 7 dias após o pagamento.


### O que cada parte faz

- `payment_id, payment_date` — colunas trazidas diretamente da tabela, sem nenhuma transformação.
- `DATE_ADD(payment_date, INTERVAL 7 DAY) AS plus_7_days` — **novo:** `DATE_ADD()` soma um intervalo
de tempo a uma data. Recebe dois argumentos: a coluna de data (`payment_date`) e o intervalo a ser somado
(`INTERVAL 7 DAY`). O resultado é a data original acrescida de 7 dias, mantendo o horário intacto. 
O resultado é exibido com o apelido `plus_7_days`.
- `INTERVAL 7 DAY` — define o intervalo de tempo a ser somado. A unidade pode variar: `DAY`, `MONTH`,
`YEAR`, `HOUR`, `MINUTE`, entre outras.
- `FROM payments` — define a tabela de origem dos dados.

> **Nota PostgreSQL:** `DATE_ADD()` é nativo do MySQL. No PostgreSQL, o equivalente é 
`payment_date + INTERVAL '7 days'`. A lógica é a mesma — apenas a sintaxe muda conforme o banco de dados.


