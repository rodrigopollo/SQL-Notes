# LENGTH — Contando caracteres de uma coluna

## Tabela utilizada
```
customer
+------------+------------+-----------+
| customer_id | first_name | last_name |
+------------+------------+-----------+
| 1           | Ana        | Souza     |
| 2           | Bruno      | Lima      |
| 3           | Carla      | Mendes    |
| 4           | Daniel     | Rocha     |
| 5           | Elisa      | Cunha     |
| 6           | Fernando   | Alves     |
| 7           | Gabriela   | Nunes     |
| 8           | Henrique   | Pinto     |
+------------+------------+-----------+
```

---

## Query
```sql
SELECT
    first_name          AS nome,
    LENGTH(first_name)  AS tamanho_nome
FROM customer;
```


## Resultado
```
+----------+--------------+
| nome     | tamanho_nome |
+----------+--------------+
| Ana      | 3            |
| Bruno    | 5            |
| Carla    | 5            |
| Daniel   | 6            |
| Elisa    | 5            |
| Fernando | 8            |
| Gabriela | 8            |
| Henrique | 8            |
+----------+--------------+
```

---

## O que cada parte faz

- `LENGTH(first_name)` — conta quantos caracteres existem no valor da coluna `first_name` para cada linha.
- `AS nome` — renomeia a coluna `first_name` para `nome` no resultado.
- `AS tamanho_nome` — renomeia a coluna retornada por `LENGTH()` para `tamanho_nome`.



