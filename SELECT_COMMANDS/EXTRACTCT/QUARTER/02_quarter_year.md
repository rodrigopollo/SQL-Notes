## QUARTER — Quais trimestres tiveram faturamento total acima de R$ 25,00?

**Tabela utilizada:** `payments`

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
HAVING SUM(amount) > 25
ORDER BY
    ano ASC,
    trimestre ASC;
```

### Resultado
```
+------+-----------+------------+------------+
| ano  | trimestre | qnt_vendas | tot_vendas |
+------+-----------+------------+------------+
| 2025 |         3 |          1 |      30.00 |
| 2026 |         1 |          1 |      50.00 |
| 2026 |         3 |          1 |      40.00 |
+------+-----------+------------+------------+
```

Dos 5 trimestres com vendas registradas, apenas **3 superaram R$ 25,00**: Q3/2025 (R$ 30,00), 
Q1/2026 (R$ 50,00) e Q3/2026 (R$ 40,00). Os trimestres Q1/2024 (R$ 10,00) e Q1/2025 (R$ 20,00)
foram excluídos do resultado por ficarem abaixo do limite definido no `HAVING`. O trimestre de maior
faturamento foi **Q1/2026, com R$ 50,00**.

---

### O que cada parte faz

- `EXTRACT(YEAR FROM payment_date) AS ano` — extrai o ano da coluna `payment_date` e exibe com o apelido `ano`.
- `EXTRACT(QUARTER FROM payment_date) AS trimestre` — extrai o trimestre da data. 
Q1 = jan–mar, Q2 = abr–jun, Q3 = jul–set, Q4 = out–dez.
- `COUNT(payment_id) AS qnt_vendas` — conta quantos pagamentos ocorreram em cada combinação de ano e trimestre.
- `SUM(amount) AS tot_vendas` — soma os valores de `amount` para cada combinação de ano e trimestre.
- `FROM payments` — define a tabela de origem dos dados.
- `GROUP BY EXTRACT(YEAR FROM ...), EXTRACT(QUARTER FROM ...)` — agrupa os registros por ano e por trimestre
para que o `COUNT` e o `SUM` operem em cada grupo separadamente.
- `HAVING SUM(amount) > 25` — filtra os grupos **após** o agrupamento, mantendo apenas os trimestres cujo
faturamento total seja maior que R$ 25,00. Este é um uso prático do `HAVING`: a condição depende de `SUM`,
uma função de agregação, o que torna impossível usar `WHERE` aqui — o `WHERE` age antes do agrupamento,
quando os totais ainda não foram calculados.
- `ORDER BY ano ASC, trimestre ASC` — ordena o resultado do mais antigo para o mais recente.



