## UPPER() — Como buscar um cliente ignorando maiúsculas e minúsculas?

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
WHERE UPPER(first_name) = UPPER('BRUNO');
```

### Resultado
```
+-------------+------------+-----------+
| customer_id | first_name | last_name |
+-------------+------------+-----------+
|           2 | Bruno      | Lima      |
+-------------+------------+-----------+
```

---

A query encontra o cliente "Bruno" independentemente de como o nome foi digitado — `'bruno'`, `'BRUNO'`,
`'Bruno'` ou `'bRuNo'` retornariam exatamente o mesmo resultado. Esse padrão é essencial em sistemas reais
onde os dados foram cadastrados por pessoas diferentes, em momentos diferentes, sem uma regra de capitalização
definida. Sem essa técnica, uma busca por `'bruno'` não encontraria `'Bruno'` — e o sistema pareceria com um
bug para o usuário final, quando na verdade seria apenas uma comparação sensível a maiúsculas e minúsculas.


### O que cada parte faz

- `customer_id, first_name, last_name` — colunas trazidas diretamente da tabela, sem nenhuma transformação.
- `FROM customer` — define a tabela de origem dos dados.
- `WHERE UPPER(first_name) = UPPER('BRUNO')` — antes de comparar, ambos os lados são convertidos para 
maiúsculas: `first_name` de cada linha e o texto `'BRUNO'` passado na busca. Com isso, independentemente de
como o nome foi digitado no banco (`'bruno'`, `'Bruno'`, `'bRuNo'`) ou de como foi digitado na busca, os dois
lados da comparação sempre serão `'BRUNO'` — e a igualdade funciona. Usar `UPPER()` dos dois lados é a chave:
converter apenas um lado poderia falhar se o valor armazenado na tabela tivesse uma capitalização inesperada.

> **Alternativa com `LOWER()`:** o mesmo resultado pode ser obtido com `WHERE LOWER(first_name) = LOWER('BRUNO')`.
O importante não é qual dos dois usar — é garantir que **ambos os lados** da comparação estejam no mesmo padrão.

> **Alternativa com `ILIKE`:** no PostgreSQL existe o operador `ILIKE`, que já faz a comparação ignorando 
maiúsculas e minúsculas sem precisar de `UPPER()` ou `LOWER()`: `WHERE first_name ILIKE 'bruno'`. O resultado
seria o mesmo, com uma sintaxe mais curta.

