## QUARTER — Qual foi o desempenho por trimestre em cada ano?

**Tabela utilizada:** `payments`

> **Conceitos novos neste exercício:** `EXTRACT(QUARTER ...)` e `HAVING`.

---

### Query
```sql
SELECT
    EXTRACT(YEAR FROM payment_date)    AS ano,
    EXTRACT(QUARTER FROM payment_date) AS trimestre,
    COUNT(payment_id)                  AS qnt_vendas,
    SUM(amount)                        AS tot_vendas
FROM payments
GROUP BY
    EXTRACT(YEAR FROM payment_date),
    EXTRACT(QUARTER FROM payment_date)
HAVING COUNT(payment_id) > 0
ORDER BY
    ano ASC,
    trimestre ASC;
```

### Resultado
```
+------+-----------+------------+------------+
| ano  | trimestre | qnt_vendas | tot_vendas |
+------+-----------+------------+------------+
| 2024 |         1 |          1 |      10.00 |
| 2025 |         1 |          1 |      20.00 |
| 2025 |         3 |          1 |      30.00 |
| 2026 |         1 |          1 |      50.00 |
| 2026 |         3 |          1 |      40.00 |
+------+-----------+------------+------------+
```

Os pagamentos estão concentrados nos trimestres **Q1 e Q3**, sem nenhuma ocorrência em Q2 ou Q4 em nenhum
dos anos. Em 2024, houve apenas 1 trimestre ativo (Q1). Em 2025, os dois trimestres ativos somam **R$ 50,00**.
Em 2026, o melhor trimestre foi o **Q1 com R$ 50,00**, seguido do Q3 com R$ 40,00.

---

### O que cada parte faz

- `EXTRACT(YEAR FROM payment_date) AS ano` — extrai o ano da coluna `payment_date` e exibe com o apelido `ano`.
- `EXTRACT(QUARTER FROM payment_date) AS trimestre` — **novo:** extrai o trimestre da data. Um trimestre 
é um bloco de 3 meses; o ano é dividido em quatro: Q1 = jan–mar, Q2 = abr–jun, Q3 = jul–set, Q4 = out–dez.
O resultado é um número de 1 a 4.
- `COUNT(payment_id) AS qnt_vendas` — conta quantos pagamentos ocorreram em cada combinação de ano e trimestre.
- `SUM(amount) AS tot_vendas` — soma os valores de `amount` para cada combinação de ano e trimestre.
- `FROM payments` — define a tabela de origem dos dados.
- `GROUP BY EXTRACT(YEAR FROM ...), EXTRACT(QUARTER FROM ...)` — agrupa os registros por ano e por trimestre
para que o `COUNT` e o `SUM` operem em cada grupo separadamente.

- `HAVING COUNT(payment_id) > 0` — **novo:** `HAVING` filtra os grupos **depois** do agrupamento, ao contrário
do `WHERE`, que filtra os registros **antes**. É usado quando a condição depende de uma função de agregação
como `COUNT` ou `SUM`. Neste caso específico, a condição é redundante: o `GROUP BY` nunca gera grupos vazios,
então `COUNT` sempre será ≥ 1. Um uso mais prático seria, por exemplo, `HAVING SUM(amount) > 100` para exibir
só os trimestres com faturamento acima de um valor.
- `ORDER BY ano ASC, trimestre ASC` — ordena o resultado do mais antigo para o mais recente.



