# SQL — RIGHT JOIN com Filtro no ON

## O que é RIGHT JOIN?

O `RIGHT JOIN` retorna **todas as linhas da tabela da direita** (`Logins`),
e apenas as linhas da tabela da esquerda (`Registrations`) que cumprirem as condições do `ON`.

Quando não há correspondência, os campos da esquerda aparecem como `NULL`.


## Tabelas utilizadas

```
Registrations                  Logins
+--------+---------+           +--------+---------+
| reg_id | name    |           | log_id | name    |
+--------+---------+           +--------+---------+
| 1      | Andrew  |           | 1      | Xavier  |
| 2      | Bob     |           | 2      | Andrew  |
| 3      | Charlie |           | 3      | Yolanda |
| 4      | David   |           | 4      | Bob     |
+--------+---------+           +--------+---------+
```


## Querry:

```sql
SELECT
    r.reg_id,
    r.name,
    l.log_id,
    l.name
FROM Registrations AS r
RIGHT JOIN Logins AS l
    ON r.name = l.name
    AND r.reg_id >= 2;
```



## Resultado

```
+--------+---------+--------+---------+
| reg_id | r.name  | log_id | l.name  |
+--------+---------+--------+---------+
| null   | null    | 1      | Xavier  |
| null   | null    | 2      | Andrew  |
| null   | null    | 3      | Yolanda |
| 2      | Bob     | 4      | Bob     |
+--------+---------+--------+---------+
```

---

## Passo a passo
| Nome    | Existe em Registrations? | Filtro `reg_id >= 2`? | Resultado              |
|---------|--------------------------|------------------------|------------------------|
| Xavier  | Não                      | —                      | NULL no lado esquerdo  |
| Andrew  | Sim (`reg_id = 1`)       | Falhou (`1 >= 2` ❌)   | NULL no lado esquerdo  |
| Yolanda | Não                      | —                      | NULL no lado esquerdo  |
| Bob     | Sim (`reg_id = 2`)       | Passou (`2 >= 2` ✅)   | Juntou as duas tabelas |



## Ponto de atenção
> O filtro `r.reg_id >= 2` está dentro do `ON`, **não** no `WHERE`.
>
> Isso faz diferença:
> - **Filtro no `ON`**: a linha de Andrew falha no filtro, mas **ainda aparece no resultado** 
  com `NULL` no lado esquerdo, pois o `RIGHT JOIN` garante todas as linhas da direita.
> - **Filtro no `WHERE`**: Andrew seria **eliminado completamente** do resultado.