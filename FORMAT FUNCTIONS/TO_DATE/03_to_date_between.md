## TO_DATE() — Como filtrar pagamentos a partir de uma data digitada pelo usuário?

**Tabela utilizada:** `payment`
```
payment
+------------+-------------+--------+---------------------+
| payment_id | customer_id | amount | payment_date        |
+------------+-------------+--------+---------------------+
|          1 |           1 |  10.00 | 2025-01-15 10:30:00 |
|          2 |           2 |  20.00 | 2025-03-22 18:45:00 |
|          3 |           3 |  30.00 | 2025-07-05 09:00:00 |
|          4 |           4 |  40.00 | 2025-09-10 14:20:00 |
|          5 |           5 |  50.00 | 2026-02-01 12:10:00 |
+------------+-------------+--------+---------------------+
```


### Query
```sql
SELECT
    payment_id,
    customer_id,
    amount,
    payment_date
FROM payment
WHERE payment_date BETWEEN
    TO_DATE('01/07/2025', 'DD/MM/YYYY')
    AND
    TO_DATE('31/12/2025', 'DD/MM/YYYY');
```


### Resultado
```
+------------+-------------+--------+---------------------+
| payment_id | customer_id | amount | payment_date        |
+------------+-------------+--------+---------------------+
|          3 |           3 |  30.00 | 2025-07-05 09:00:00 |
|          4 |           4 |  40.00 | 2025-09-10 14:20:00 |
+------------+-------------+--------+---------------------+
```

---

A query filtra os pagamentos realizados no segundo
semestre de 2025 — entre 01/07/2025 e 31/12/2025.
Os dois textos de data são convertidos por
`TO_DATE()` antes de serem comparados com
`payment_date`. Sem a conversão, o banco estaria
comparando uma data com texto, o que geraria
erro ou resultado incorreto. Apenas os
`payment_id` 3 e 4 estão dentro do intervalo.



### O que cada parte faz

- `payment_id, customer_id, amount, payment_date`
  — colunas trazidas diretamente da tabela,
  sem nenhuma transformação.

- `FROM payment` — define a tabela de origem
  dos dados.

- `WHERE payment_date BETWEEN
  TO_DATE('01/07/2025', 'DD/MM/YYYY')
  AND
  TO_DATE('31/12/2025', 'DD/MM/YYYY')` —
  combina `BETWEEN` com `TO_DATE()`:
  - `TO_DATE('01/07/2025', 'DD/MM/YYYY')` →
    converte o texto `'01/07/2025'` em data
    real `2025-07-01`.
  - `TO_DATE('31/12/2025', 'DD/MM/YYYY')` →
    converte o texto `'31/12/2025'` em data
    real `2025-12-31`.
  - `BETWEEN` filtra os registros cujo
    `payment_date` esteja dentro do intervalo,
    incluindo os extremos.

---

### Por que TO_DATE() é necessário aqui
```
Sem TO_DATE():
  WHERE payment_date BETWEEN
      '01/07/2025' AND '31/12/2025'

  → o banco recebe dois textos, não datas
  → comparar TIMESTAMP com string pode
    gerar erro ou resultado incorreto

Com TO_DATE():
  WHERE payment_date BETWEEN
      TO_DATE('01/07/2025', 'DD/MM/YYYY')
      AND
      TO_DATE('31/12/2025', 'DD/MM/YYYY')

  → os dois textos viram datas reais
  → comparação TIMESTAMP vs DATE funciona
    corretamente
```


### Máscara pode variar conforme o formato recebido

```sql
-- Data no formato brasileiro:
TO_DATE('01/07/2025', 'DD/MM/YYYY')
→ 2025-07-01

-- Data no formato americano:
TO_DATE('07-01-2025', 'MM-DD-YYYY')
→ 2025-07-01

-- Data no formato ISO:
TO_DATE('2025.07.01', 'YYYY.MM.DD')
→ 2025-07-01

-- Todos retornam a mesma data —
-- a máscara precisa bater com o
-- formato do texto recebido.
```