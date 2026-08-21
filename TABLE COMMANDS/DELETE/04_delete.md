## DELETE + AND — Como remover pagamentos antigos de baixo valor?

**Tabela utilizada:** `payment`
```
payment (antes do DELETE)
+------------+-------------+--------+---------------------+
| payment_id | customer_id | amount | payment_date        |
+------------+-------------+--------+---------------------+
|        101 |           1 |  10.00 | 2023-01-15 09:00:00 |
|        102 |           1 |  12.00 | 2025-03-22 14:00:00 |
|        103 |           2 |   5.00 | 2023-05-10 11:00:00 |
|        104 |           2 |  15.00 | 2025-07-01 08:00:00 |
|        105 |           3 |   8.00 | 2023-11-20 16:00:00 |
+------------+-------------+--------+---------------------+
```



### Query
```sql
DELETE FROM payment
WHERE
    amount < 10
    AND payment_date < '2024-01-01'
RETURNING
    payment_id,
    customer_id,
    amount,
    payment_date;
```


### Resultado
```
+------------+-------------+--------+---------------------+
| payment_id | customer_id | amount | payment_date        |
+------------+-------------+--------+---------------------+
|        103 |           2 |   5.00 | 2023-05-10 11:00:00 |
|        105 |           3 |   8.00 | 2023-11-20 16:00:00 |
+------------+-------------+--------+---------------------+
```

---

A query removeu 2 pagamentos que atenderam às duas
condições ao mesmo tempo: valor abaixo de R$ 10,00
**e** data anterior a 2024. O payment_id 101 não
foi deletado pois seu valor é exatamente R$ 10,00
— o operador `<` é estrito e não inclui o limite.
Os pagamentos de 2025 também foram preservados
mesmo com valores baixos, pois não atenderam
à condição de data.



### O que cada parte faz

- `DELETE FROM payment` — seleciona a tabela
  `payment` como origem da remoção.

- `WHERE amount < 10` — primeira condição: apenas
  pagamentos com valor estritamente abaixo de
  R$ 10,00. O `payment_id 101` (R$ 10,00 exato)
  **não** é incluído pois `<` não engloba o limite.

- `AND payment_date < '2024-01-01'` — segunda
  condição: apenas pagamentos anteriores a
  01/01/2024. O `AND` exige que **ambas** as
  condições sejam verdadeiras para a linha ser
  deletada — uma condição verdadeira sozinha
  não é suficiente.

- `RETURNING payment_id, customer_id, amount,
  payment_date` — retorna as colunas escolhidas
  dos registros removidos para confirmar
  o que foi deletado.

---

### Tabela depois do DELETE
```
payment (depois do DELETE)
+------------+-------------+--------+---------------------+
| payment_id | customer_id | amount | payment_date        |
+------------+-------------+--------+---------------------+
|        101 |           1 |  10.00 | 2023-01-15 09:00:00 |
|        102 |           1 |  12.00 | 2025-03-22 14:00:00 |
|        104 |           2 |  15.00 | 2025-07-01 08:00:00 |
+------------+-------------+--------+---------------------+
```



### Por que cada linha foi mantida ou removida

```
payment_id 101 → amount 10.00, data 2023
  amount < 10?  NÃO (10 não é < 10) → mantido ✓

payment_id 102 → amount 12.00, data 2025
  amount < 10?  NÃO                  → mantido ✓

payment_id 103 → amount 5.00, data 2023
  amount < 10?  SIM
  data < 2024?  SIM                  → deletado ✗

payment_id 104 → amount 15.00, data 2025
  amount < 10?  NÃO                  → mantido ✓

payment_id 105 → amount 8.00, data 2023
  amount < 10?  SIM
  data < 2024?  SIM                  → deletado ✗
```



### AND vs OR no DELETE
```sql
-- AND → ambas as condições precisam ser TRUE:
WHERE amount < 10 AND payment_date < '2024-01-01'
→ remove só os antigos E de baixo valor

-- OR → basta uma condição ser TRUE:
WHERE amount < 10 OR payment_date < '2024-01-01'
→ remove os antigos OU os de baixo valor
  (afetaria mais linhas — use com cuidado)
```