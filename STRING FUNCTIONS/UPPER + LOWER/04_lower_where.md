## LOWER() — Quais clientes têm a sequência de letras 'an' no primeiro nome?

**Tabela utilizada:** `customer`
```
+-------------+------------+-----------+
| customer_id | first_name | last_name |
+-------------+------------+-----------+
|           1 | Ana        | Souza     |
|           2 | Bruno      | Lima      |
|           3 | Carla      | Mendes    |
|           4 | Daniel     | Rocha     |
|           5 | Elisa      | Cunha     |
|           6 | Fernando   | Alves     |
|           7 | Gabriela   | Nunes     |
|           8 | Henrique   | Pinto     |
+-------------+------------+-----------+
```



### Query
```sql
SELECT
    customer_id,
    first_name,
    last_name
FROM customer
WHERE LOWER(first_name) LIKE '%an%';
```


### Resultado
```
+-------------+------------+-----------+
| customer_id | first_name | last_name |
+-------------+------------+-----------+
|           1 | Ana        | Souza     |
|           4 | Daniel     | Rocha     |
|           6 | Fernando   | Alves     |
+-------------+------------+-----------+
```

---

A query encontrou 3 clientes cujo primeiro nome contém a sequência `'an'` em qualquer posição,
independentemente de maiúsculas ou minúsculas. `LOWER()` garante que a busca funcione mesmo que os nomes 
estejam cadastrados de formas inconsistentes no banco. Esse padrão — `LOWER()` combinado com `LIKE` — 
é muito usado em sistemas de busca onde o usuário digita parte de um nome e o sistema precisa encontrar 
todos os registros que contenham aquele trecho, sem se preocupar com capitalização.


### O que cada parte faz

- `customer_id, first_name, last_name` — colunas trazidas diretamente da tabela, sem nenhuma transformação.
- `FROM customer` — define a tabela de origem dos dados.
- `WHERE LOWER(first_name) LIKE '%an%'` — combina dois recursos:
  - `LOWER(first_name)` — converte o valor de `first_name` de cada linha para minúsculas antes da comparação. Sem isso, `LIKE '%an%'` não encontraria `'Ana'` (com A maiúsculo) nem `'Fernando'` dependendo da capitalização armazenada.
  - `LIKE '%an%'` — o operador `LIKE` busca um padrão dentro do texto. O `%` é um curinga que representa qualquer sequência de caracteres (inclusive nenhum). `'%an%'` significa: qualquer texto que contenha a sequência `'an'` em qualquer posição — no início, no meio ou no fim.


### Como o filtro avalia cada nome
```
'Ana'      → lower → 'ana'      → contém 'an'? ✓ (posição 1)
'Bruno'    → lower → 'bruno'    → contém 'an'? ✗
'Carla'    → lower → 'carla'    → contém 'an'? ✗
'Daniel'   → lower → 'daniel'   → contém 'an'? ✓ (posição 2)
'Elisa'    → lower → 'elisa'    → contém 'an'? ✗
'Fernando' → lower → 'fernando' → contém 'an'? ✓ (posição 5)
'Gabriela' → lower → 'gabriela' → contém 'an'? ✗
'Henrique' → lower → 'henrique' → contém 'an'? ✗
```
