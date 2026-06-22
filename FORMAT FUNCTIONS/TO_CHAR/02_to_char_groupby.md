## TO_CHAR() — Durante quais meses ocorreram pagamentos? O mês deve estar escrito por extenso.

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
    COUNT(payment_id)                    AS qnt_pagamentos,
    TO_CHAR(payment_date, 'FMMonth')     AS mes,
    EXTRACT(YEAR FROM payment_date)      AS ano
FROM payments
GROUP BY
    TO_CHAR(payment_date, 'FMMonth'),
    EXTRACT(YEAR FROM payment_date)
ORDER BY
    ano ASC,
    EXTRACT(MONTH FROM payment_date) ASC;
```


### Resultado
```
+----------------+-----------+------+
| qnt_pagamentos | mes       | ano  |
+----------------+-----------+------+
|              1 | January   | 2025 |
|              1 | March     | 2025 |
|              1 | July      | 2025 |
|              1 | September | 2025 |
|              1 | February  | 2026 |
+----------------+-----------+------+
```

---

A query lista todos os meses em que houve pelo menos um pagamento, exibindo o nome por extenso em vez 
do número — o que torna o resultado mais legível em relatórios. Em 2025 houve pagamentos em 4 meses 
distintos (janeiro, março, julho e setembro); em 2026 apenas em fevereiro. O truque de ordenar por 
`EXTRACT(MONTH ...)` em vez do nome do mês é essencial aqui: sem ele, "February" viria antes de "January"
por ordem alfabética, quebrando a leitura cronológica.


### O que cada parte faz

- `COUNT(payment_id) AS qnt_pagamentos` — conta quantos pagamentos ocorreram em cada combinação de mês e ano.
- `TO_CHAR(payment_date, 'FMMonth') AS mes` — converte a data para o nome do mês por extenso em texto. 
A máscara `'Month'` funciona, mas o PostgreSQL preenche o resultado com espaços em branco à direita até 
atingir o comprimento do mês mais longo ("September" = 9 caracteres) — então "July" viria como 
"July     ". O prefixo `FM` (fill mode) remove esses espaços, retornando o nome limpo.
- `EXTRACT(YEAR FROM payment_date) AS ano` — extrai o ano para separar pagamentos do mesmo mês em anos 
diferentes.
- `FROM payments` — define a tabela de origem dos dados.
- `GROUP BY TO_CHAR(...), EXTRACT(YEAR ...)` — agrupa os registros pela combinação de nome do mês e ano. 
É necessário repetir as expressões completas no `GROUP BY`, pois o PostgreSQL não permite usar aliases 
(`mes`, `ano`) nessa cláusula.
- `ORDER BY ano ASC, EXTRACT(MONTH FROM payment_date) ASC` — **importante:** ordenar pelo alias `mes` (texto) colocaria os meses em ordem alfabética (February, January, July...), não cronológica. Por isso usamos `EXTRACT(MONTH FROM payment_date)` no `ORDER BY` — ele retorna o número do mês (1 a 12), garantindo a ordem cronológica correta dentro de cada ano.
