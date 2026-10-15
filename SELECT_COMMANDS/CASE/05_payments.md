## CASE EXPRESSION — Como traduzir códigos de método de pagamento?

**Tabela utilizada:** `payment`
```
payment
+------------+-------------+--------+----------------+
| payment_id | customer_id | amount | payment_method |
+------------+-------------+--------+----------------+
|          1 |           1 |  49.90 | CC             |
|          2 |           2 |  99.90 | PIX            |
|          3 |           3 |  29.90 | DC             |
|          4 |           1 | 149.90 | PIX            |
|          5 |           2 |  19.90 | BOL            |
|          6 |           3 |  79.90 | CC             |
+------------+-------------+--------+----------------+
```



### Query
```sql
SELECT
    payment_id,
    customer_id,
    amount,
    payment_method,
    CASE payment_method
        WHEN 'CC'  THEN 'Cartão de Crédito'
        WHEN 'DC'  THEN 'Cartão de Débito'
        WHEN 'PIX' THEN 'Pix'
        WHEN 'BOL' THEN 'Boleto Bancário'
        ELSE 'Método desconhecido'
    END AS metodo_completo
FROM payment;
```



### Resultado
```
+------------+-------------+--------+----------------+-------------------+
| payment_id | customer_id | amount | payment_method | metodo_completo   |
+------------+-------------+--------+----------------+-------------------+
|          1 |           1 |  49.90 | CC             | Cartão de Crédito |
|          2 |           2 |  99.90 | PIX            | Pix               |
|          3 |           3 |  29.90 | DC             | Cartão de Débito  |
|          4 |           1 | 149.90 | PIX            | Pix               |
|          5 |           2 |  19.90 | BOL            | Boleto Bancário   |
|          6 |           3 |  79.90 | CC             | Cartão de Crédito |
+------------+-------------+--------+----------------+-------------------+
```

---

A query traduz os códigos curtos de método de
pagamento (`CC`, `DC`, `PIX`, `BOL`) para seus
nomes completos. O banco armazena abreviações por
serem mais rápidas de comparar e ocuparem menos
espaço — especialmente em tabelas de pagamento
que podem ter milhões de registros. O `ELSE` cobre
qualquer código inesperado que possa entrar na
tabela por erro de integração com sistemas externos.



### O que cada parte faz

- `CASE payment_method` — passa o valor de
  `payment_method` de cada linha para ser
  comparado com os `WHEN`s abaixo.

- `WHEN 'CC' THEN 'Cartão de Crédito'` — se
  `payment_method` for igual a `'CC'`, retorna
  `'Cartão de Crédito'`.

- `WHEN 'DC' THEN 'Cartão de Débito'` — se
  `payment_method` for igual a `'DC'`, retorna
  `'Cartão de Débito'`.

- `WHEN 'PIX' THEN 'Pix'` — se `payment_method`
  for igual a `'PIX'`, retorna `'Pix'`.

- `WHEN 'BOL' THEN 'Boleto Bancário'` — se
  `payment_method` for igual a `'BOL'`, retorna
  `'Boleto Bancário'`.

- `ELSE 'Método desconhecido'` — cobre códigos
  fora dos quatro esperados, evitando `NULL`
  silencioso no resultado.

- `END AS metodo_completo` — encerra o bloco
  `CASE` e nomeia a coluna de resultado.

---

### Quando CASE EXPRESSION é a escolha certa
```
Use CASE EXPRESSION quando:
  ✓ os valores são fixos e conhecidos
  ✓ a comparação é sempre de igualdade (=)
  ✓ os valores são códigos curtos
    que precisam de tradução legível

Exemplos clássicos no mercado:
  CC, DC, PIX, BOL  → método de pagamento
  M, F              → sexo
  1, 2, 3           → status do pedido
  G, PG, R, NC-17   → classificação etária
  BR, US, PT        → país de origem
```