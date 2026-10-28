## TO_NUMBER() — Como aplicar uma porcentagem de imposto armazenada como texto?

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
    amount                                          AS valor_original,
    ROUND(
        amount * TO_NUMBER('1.15', '9.99'),
        2
    )                                               AS valor_com_imposto
FROM payment;
```


### Resultado
```
+------------+----------------+-------------------+
| payment_id | valor_original | valor_com_imposto |
+------------+----------------+-------------------+
|          1 |          10.00 |             11.50 |
|          2 |          20.00 |             23.00 |
|          3 |          30.00 |             34.50 |
|          4 |          40.00 |             46.00 |
|          5 |          50.00 |             57.50 |
+------------+----------------+-------------------+
```

---

A query calcula o valor de cada pagamento com
15% de imposto adicionado. O multiplicador
`'1.15'` chega como texto — simulando um valor
vindo de fora do banco, como um arquivo de
configuração ou uma planilha — e é convertido
por `TO_NUMBER()` antes de participar do
cálculo. `ROUND(..., 2)` garante que o resultado
tenha sempre 2 casas decimais, evitando números
como `11.4999...`.


### O que cada parte faz

- `amount AS valor_original` — exibe o valor
  original de cada pagamento para facilitar
  a comparação com o valor calculado.

- `TO_NUMBER('1.15', '9.99')` — converte o
  texto `'1.15'` em número real. A máscara
  `'9.99'` define: 1 dígito inteiro e 2
  decimais. Sem a conversão, o banco não
  conseguiria multiplicar `amount` por um
  texto.

- `amount * TO_NUMBER('1.15', '9.99')` —
  multiplica o valor original pelo fator
  `1.15`, que equivale a adicionar 15%:
  `10.00 * 1.15 = 11.50`.

- `ROUND(..., 2)` — arredonda o resultado
  para 2 casas decimais, evitando imprecisões
  de ponto flutuante em cálculos monetários.

- `AS valor_com_imposto` — apelido para
  nomear a coluna de resultado.

---

### Como o cálculo funciona
```
amount * 1.15 = valor com 15% de imposto

10.00 * 1.15 = 11.50   (+R$  1.50)
20.00 * 1.15 = 23.00   (+R$  3.00)
30.00 * 1.15 = 34.50   (+R$  4.50)
40.00 * 1.15 = 46.00   (+R$  6.00)
50.00 * 1.15 = 57.50   (+R$  7.50)
```


### Outros multiplicadores comuns
```sql
-- 10% de desconto (multiplica por 0.90):
amount * TO_NUMBER('0.90', '9.99')

-- 20% de aumento (multiplica por 1.20):
amount * TO_NUMBER('1.20', '9.99')

-- 7.5% de imposto (multiplica por 1.075):
amount * TO_NUMBER('1.075', '9.999')
--                          ↑
--               máscara com 3 decimais
--               para bater com o texto
```