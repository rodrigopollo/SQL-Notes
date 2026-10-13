## CASE EXPRESSION — Como converter códigos de sexo em texto legível?

**Tabela utilizada:** `customer`
```
customer
+-------------+------------+-----------+-----+
| customer_id | first_name | last_name | sex |
+-------------+------------+-----------+-----+
|           1 | Ana        | Souza     | F   |
|           2 | Bruno      | Lima      | M   |
|           3 | Carla      | Mendes    | F   |
|           4 | Daniel     | Rocha     | M   |
|           5 | Elisa      | Cunha     | F   |
+-------------+------------+-----------+-----+
```


### Query
```sql
SELECT
    customer_id,
    first_name,
    last_name,
    sex,
    CASE sex
        WHEN 'M' THEN 'Masculino'
        WHEN 'F' THEN 'Feminino'
    END AS sexo
FROM customer;
```


### Resultado
```
+-------------+------------+-----------+-----+-----------+
| customer_id | first_name | last_name | sex | sexo      |
+-------------+------------+-----------+-----+-----------+
|           1 | Ana        | Souza     | F   | Feminino  |
|           2 | Bruno      | Lima      | M   | Masculino |
|           3 | Carla      | Mendes    | F   | Feminino  |
|           4 | Daniel     | Rocha     | M   | Masculino |
|           5 | Elisa      | Cunha     | F   | Feminino  |
+-------------+------------+-----------+-----+-----------+
```

---

A query converte os códigos `'M'` e `'F'` da coluna
`sex` em textos legíveis. O banco armazena códigos
curtos por serem mais compactos — uma letra ocupa
menos espaço do que a palavra inteira, especialmente
em tabelas com milhões de registros. O `CASE`
traduz esses códigos apenas na exibição, sem
alterar nada na tabela. Como não há `ELSE`, qualquer
valor fora de `'M'` e `'F'` retornaria `NULL`.



### O que cada parte faz

- `CASE sex` — passa o valor de `sex` de cada
  linha para ser comparado com os `WHEN`s abaixo,
  testando igualdade em ordem.

- `WHEN 'M' THEN 'Masculino'` — se `sex` for
  igual a `'M'`, retorna `'Masculino'`. String
  entre aspas simples, como sempre.

- `WHEN 'F' THEN 'Feminino'` — se `sex` for
  igual a `'F'`, retorna `'Feminino'`.

- `END AS sexo` — encerra o bloco `CASE` e
  nomeia a coluna de resultado como `sexo`.

---

### Versão com ELSE para valores inesperados
```sql
CASE sex
    WHEN 'M' THEN 'Masculino'
    WHEN 'F' THEN 'Feminino'
    ELSE 'Não informado'
END AS sexo
```

```
+-----+----------------+
| sex | sexo           |
+-----+----------------+
| M   | Masculino      |
| F   | Feminino       |
| NULL| Não informado  |
| ?   | Não informado  |
+-----+----------------+
```

