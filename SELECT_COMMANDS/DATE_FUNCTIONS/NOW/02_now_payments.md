## NOW() — Há quantos dias cada pagamento foi realizado?

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

> **Conceito novo neste exercício:** subtração entre datas com `NOW()` e uso de `EXTRACT` sobre o resultado.


### Query
```sql
SELECT
    payment_id,
    payment_date,
    amount,
    EXTRACT(DAY FROM NOW() - payment_date) AS dias_desde_pagamento
FROM payments
ORDER BY
    dias_desde_pagamento DESC;
```


### Resultado
```
+------------+---------------------+--------+----------------------+
| payment_id | payment_date        | amount | dias_desde_pagamento |
+------------+---------------------+--------+----------------------+
|          1 | 2025-01-15 10:30:00 |  10.00 |                  519 |
|          2 | 2025-03-22 18:45:00 |  20.00 |                  452 |
|          3 | 2025-07-05 09:00:00 |  30.00 |                  348 |
|          4 | 2025-09-10 14:20:00 |  40.00 |                  281 |
|          5 | 2026-02-01 12:10:00 |  50.00 |                  137 |
+------------+---------------------+--------+----------------------+
```
---

A query calcula, em tempo real, há quantos dias cada pagamento foi registrado. O pagamento mais antigo
foi o de `payment_id 1` (15/01/2025), e o mais recente o de `payment_id 5` (01/02/2026). Esse tipo de
consulta é útil em situações reais como identificar cobranças em atraso, calcular tempo médio entre pedido
e pagamento, ou verificar há quanto tempo um cliente não realiza uma compra.

### O que cada parte faz
- `payment_id, payment_date, amount` — colunas trazidas diretamente da tabela, sem nenhuma transformação.
- `NOW() - payment_date` — **novo:** subtrai a data de cada pagamento da data e hora atuais do sistema.
O resultado é um **intervalo de tempo** (no PostgreSQL chamado de `interval`) — por exemplo,
`200 days 03:30:00`. Quando se subtrai dois valores de data/hora no PostgreSQL, o banco automaticamente
calcula a diferença entre eles.
- `EXTRACT(DAY FROM NOW() - payment_date)` — aplica `EXTRACT` sobre o intervalo gerado pela subtração,
extraindo apenas a parte dos dias. Aqui o `EXTRACT` não está agindo sobre uma coluna de data, mas sim 
sobre o resultado de uma conta — o que é perfeitamente válido no PostgreSQL.
- `AS dias_desde_pagamento` — apelido para tornar o nome da coluna legível no resultado.
- `FROM payments` — define a tabela de origem dos dados.
- `ORDER BY dias_desde_pagamento DESC` — ordena do pagamento mais antigo (mais dias) para o mais recente
(menos dias).


> **Atenção:** Como `NOW()` retorna a data e hora do momento da execução, a coluna `dias_desde_pagamento`
vai ter valores diferentes cada vez que a query for rodada.


