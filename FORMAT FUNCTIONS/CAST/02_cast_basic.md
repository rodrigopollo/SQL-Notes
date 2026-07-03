## CAST() — Como exibir apenas a data de cada pagamento, sem o horário?

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
    payment_date                    AS data_completa,
    CAST(payment_date AS DATE)      AS somente_data,
    amount
FROM payments;
```

### Resultado
```
+------------+---------------------+--------------+--------+
| payment_id | data_completa       | somente_data | amount |
+------------+---------------------+--------------+--------+
|          1 | 2025-01-15 10:30:00 | 2025-01-15   |  10.00 |
|          2 | 2025-03-22 18:45:00 | 2025-03-22   |  20.00 |
|          3 | 2025-07-05 09:00:00 | 2025-07-05   |  30.00 |
|          4 | 2025-09-10 14:20:00 | 2025-09-10   |  40.00 |
|          5 | 2026-02-01 12:10:00 | 2026-02-01   |  50.00 |
+------------+---------------------+--------------+--------+
```

---

A coluna `payment_date` armazena data e hora juntas (tipo `TIMESTAMP`). Em muitas situações o horário não
é relevante — relatórios diários, agrupamentos por data, comparações com `CURRENT_DATE` — e carregar o 
horário no resultado polui a leitura desnecessariamente. `CAST(payment_date AS DATE)` resolve isso de forma
limpa, descartando o horário e mantendo apenas a data. Esse é um dos usos mais comuns de `CAST()` no dia a
dia, especialmente em pipelines de dados onde colunas de timestamp precisam ser normalizadas para data antes
de serem agrupadas ou comparadas.


### O que cada parte faz

- `payment_id, amount` — colunas trazidas diretamente da tabela, sem nenhuma transformação.
- `payment_date AS data_completa` — exibe a coluna original com o apelido `data_completa` para facilitar
a comparação com a coluna convertida ao lado.
- `CAST(payment_date AS DATE) AS somente_data` — converte o tipo `TIMESTAMP` (data + hora) para o tipo 
`DATE` (somente data). O horário é descartado completamente na conversão. Diferente do exercício anterior
com `CHAR`, o tipo `DATE` não tem armadilha de tamanho — ele sempre representa uma data completa no formato
`YYYY-MM-DD`.
- `FROM payments` — define a tabela de origem dos dados.


### Tipos envolvidos nesta conversão

| Tipo        | O que armazena | Exemplo               |
|-------------|----------------|-----------------------|
| `TIMESTAMP` | data + hora    | `2025-01-15 10:30:00` |
| `DATE`      | somente data   | `2025-01-15`          |