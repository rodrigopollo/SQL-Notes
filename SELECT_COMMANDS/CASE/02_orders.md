## CASE EXPRESSION — Como converter códigos numéricos em status legíveis?

**Tabela utilizada:** `orders`
```
orders
+----------+-------------+--------+
| order_id | customer_id | status_code |
+----------+-------------+-------------+
|        1 |           1 |           1 |
|        2 |           2 |           3 |
|        3 |           3 |           2 |
|        4 |           1 |           3 |
|        5 |           2 |           1 |
+----------+-------------+-------------+
```


### Query
```sql
SELECT
    order_id,
    customer_id,
    status_code,
    CASE status_code
        WHEN 1 THEN 'Aguardando'
        WHEN 2 THEN 'Processando'
        WHEN 3 THEN 'Concluído'
    END AS status
FROM orders;
```


### Resultado
```
+----------+-------------+-------------+-------------+
| order_id | customer_id | status_code | status      |
+----------+-------------+-------------+-------------+
|        1 |           1 |           1 | Aguardando  |
|        2 |           2 |           3 | Concluído   |
|        3 |           3 |           2 | Processando |
|        4 |           1 |           3 | Concluído   |
|        5 |           2 |           1 | Aguardando  |
+----------+-------------+-------------+-------------+
```

---

A query converte os códigos numéricos `1`, `2` e `3`
da coluna `status_code` em textos legíveis para
exibição. Bancos de dados frequentemente armazenam
status como números inteiros por serem mais leves
e rápidos de comparar — o `CASE EXPRESSION` entra
apenas na camada de exibição, traduzindo esses
códigos para o usuário final sem alterar nada na
tabela. Como todos os valores possíveis têm um
`WHEN`, o `ELSE` foi omitido — linhas com códigos
fora de 1, 2 ou 3 retornariam `NULL`.



### O que cada parte faz

- `CASE status_code` — passa o valor de
  `status_code` de cada linha para ser comparado
  com os `WHEN`s abaixo, testando igualdade
  em ordem.

- `WHEN 1 THEN 'Aguardando'` — se `status_code`
  for igual a `1`, retorna `'Aguardando'`.

- `WHEN 2 THEN 'Processando'` — se `status_code`
  for igual a `2`, retorna `'Processando'`.

- `WHEN 3 THEN 'Concluído'` — se `status_code`
  for igual a `3`, retorna `'Concluído'`.

- `END AS status` — encerra o bloco `CASE` e
  nomeia a coluna de resultado como `status`.

---

### Por que armazenar códigos numéricos?
```
Armazenar 1, 2, 3 em vez de texto:

  ✓ ocupa menos espaço em disco
  ✓ comparações numéricas são mais rápidas
  ✓ mais fácil de mudar o texto do status
    sem alterar os dados da tabela
    (basta ajustar o CASE na query)

  O CASE faz a tradução só na hora
  de exibir — os dados ficam compactos
  no banco.
```


### ELSE omitido vs ELSE explícito
```sql
-- Sem ELSE → código desconhecido retorna NULL:
CASE status_code
    WHEN 1 THEN 'Aguardando'
    WHEN 2 THEN 'Processando'
    WHEN 3 THEN 'Concluído'
END

-- Com ELSE → código desconhecido retorna texto:
CASE status_code
    WHEN 1 THEN 'Aguardando'
    WHEN 2 THEN 'Processando'
    WHEN 3 THEN 'Concluído'
    ELSE 'Status desconhecido'
END
```

Dica q ainda nao entendo.
Em produção, usar `ELSE` é mais seguro — evita
`NULL` silencioso quando um código inesperado
aparece na tabela.