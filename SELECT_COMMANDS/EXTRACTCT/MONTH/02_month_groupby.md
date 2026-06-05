## MONTH — Quanto vendemos em cada mês desde que abrimos a empresa?

**Tabela utilizada:** `payments`

---

### Query

```sql
SELECT 
    EXTRACT(YEAR FROM payment_date) AS ano,
    EXTRACT(MONTH FROM payment_date) AS mes,
    COUNT(payment_id) AS qnt_pagamentos,
    SUM(amount) AS total_vendido
FROM payments
GROUP BY
    EXTRACT(YEAR FROM payment_date),
    EXTRACT(MONTH FROM payment_date)
ORDER BY
    ano ASC,
    mes ASC;
```


### Resultado

```
+------+-----+----------------+--------------+
| ano  | mes | qnt_pagamentos | total_vendido|
+------+-----+----------------+--------------+
| 2024 |   1 |              1 |        10.00 |
| 2025 |   3 |              1 |        20.00 |
| 2025 |   7 |              1 |        30.00 |
| 2026 |   2 |              1 |        50.00 |
| 2026 |   9 |              1 |        40.00 |
+------+-----+----------------+--------------+
```

---

### O que cada parte faz

- `EXTRACT(YEAR FROM payment_date) AS ano` — extrai apenas o ano da coluna `payment_date` e exibe
o resultado com o apelido `ano`.
- `EXTRACT(MONTH FROM payment_date) AS mes` — extrai apenas o número do mês da coluna `payment_date` 
e exibe o resultado com o apelido `mes`.
- `COUNT(payment_id) AS qnt_pagamentos` — conta quantos pagamentos ocorreram em cada combinação de ano e mês.
- `SUM(amount) AS total_vendido` — soma os valores de `amount` para cada combinação de ano e mês, retornando
o total faturado no período.
- `FROM payments` — define a tabela de origem dos dados.
- `GROUP BY EXTRACT(YEAR FROM payment_date), EXTRACT(MONTH FROM payment_date)` — agrupa os registros por 
ano e por mês; sem esse agrupamento, o `COUNT` e o `SUM` somariam tudo junto, sem separar por período.
- `ORDER BY ano ASC, mes ASC` — ordena o resultado do mais antigo para o mais recente, primeiro pelo ano e,
dentro do mesmo ano, pelo mês.


### Interpretação

A empresa iniciou suas operações em janeiro de 2024. Desde então, foram registrados pagamentos em **5
meses distintos**, sem nenhuma concentração — cada mês ativo teve exatamente 1 pagamento. O maior valor
faturado em um único mês foi em **fevereiro/2026 (R$ 50,00)**, e o menor em **janeiro/2024 (R$ 10,00)**. 
Os meses sem registro simplesmente não aparecem no resultado, pois a query retorna apenas os períodos 
onde há dados na tabela.