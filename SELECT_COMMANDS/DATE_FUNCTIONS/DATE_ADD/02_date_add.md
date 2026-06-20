## DATE_SUB() — Qual seria a data de cada pagamento subtraindo 1 mês?

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
    DATE_SUB(payment_date, INTERVAL 1 MONTH) AS menos_1_month
FROM payments;
```


### Resultado
```
+------------+---------------------+---------------------+
| payment_id | payment_date        | menos_1_month        |
+------------+---------------------+---------------------+
|          1 | 2025-01-15 10:30:00 | 2024-12-15 10:30:00 |
|          2 | 2025-03-22 18:45:00 | 2025-02-22 18:45:00 |
|          3 | 2025-07-05 09:00:00 | 2025-06-05 09:00:00 |
|          4 | 2025-09-10 14:20:00 | 2025-08-10 14:20:00 |
|          5 | 2026-02-01 12:10:00 | 2026-01-01 12:10:00 |
+------------+---------------------+---------------------+
```

---

A query projeta uma nova data para cada pagamento, subtraindo 1 mês da `payment_date` original. O horário
é preservado em todos os registros, e o ano é ajustado automaticamente quando necessário — como no 
`payment_id 1`, onde janeiro/2025 menos 1 mês resulta em dezembro/2024. Esse tipo de operação é comum
em situações reais como calcular o início de um ciclo de cobrança anterior, verificar se um pagamento 
foi feito dentro do mês de competência, ou gerar comparativos "mês anterior vs. mês atual".

### O que cada parte faz

- `payment_id, payment_date` — colunas trazidas diretamente da tabela, sem nenhuma transformação.
- `DATE_SUB(payment_date, INTERVAL 1 MONTH) AS menos_1_month` — **novo:** `DATE_SUB()` é o oposto de
`DATE_ADD()` — subtrai um intervalo de tempo de uma data em vez de somar. Recebe dois argumentos: a coluna
de data (`payment_date`) e o intervalo a ser subtraído (`INTERVAL 1 MONTH`). O resultado é exibido com o
apelido `menos_1_month`.
- `INTERVAL 1 MONTH` — define o intervalo a ser subtraído. Assim como em `DATE_ADD()`, a unidade pode
variar: `DAY`, `MONTH`, `YEAR`, `HOUR`, `MINUTE`, entre outras.
- `FROM payments` — define a tabela de origem dos dados.



