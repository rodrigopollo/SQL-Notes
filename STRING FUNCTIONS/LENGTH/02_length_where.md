## LENGTH() — Quais clientes têm primeiro nome com mais de 5 caracteres?

**Tabela utilizada:** `customer`

```
+-------------+
| first_name  |
+-------------+
| Ana         |
| Daniel      |
| Fernando    |
| Gabriela    |
| Henrique    |
| Leo         |
+-------------+
```


### Query

```sql
SELECT first_name
FROM customer
WHERE LENGTH(first_name) > 5;
```

### Resultado

```
+------------+
| first_name |
+------------+
| Daniel     |
| Fernando   |
| Gabriela   |
| Henrique   |
+------------+
```

---

### Quantos caracteres tem cada nome?
```
Ana      → 3 caracteres → False (3 não é > 5)
Leo      → 3 caracteres → False (3 não é > 5)
Daniel   → 6 caracteres → True  (6 > 5) ✓
Fernando → 8 caracteres → True  (8 > 5) ✓
Gabriela → 8 caracteres → True  (8 > 5) ✓
Henrique → 8 caracteres → True  (8 > 5) ✓
```

A query filtra os clientes cujo primeiro nome tenha mais de 5 caracteres, usando `LENGTH()` diretamente
no `WHERE` como critério de seleção. Nomes curtos como "Ana" e "Leo" foram descartados. Na prática, 
`LENGTH()` é útil para validar dados — por exemplo, garantir que campos obrigatórios não foram preenchidos
com valores muito curtos, identificar registros com dados incompletos, ou filtrar entradas que não 
respeitam um tamanho mínimo esperado.

### O que cada parte faz

- `SELECT first_name` — traz apenas a coluna `first_name` da tabela, sem nenhuma transformação.
- `FROM customer` — define a tabela de origem dos dados.
- `WHERE LENGTH(first_name) > 5` — **novo:** `LENGTH()` é uma função de string que conta o número de 
caracteres de um texto e retorna um número inteiro. Aqui ela é aplicada sobre cada valor de `first_name`
antes de compará-lo com `5`. Apenas os nomes com mais de 5 caracteres passam pelo filtro e aparecem no 
resultado. Nomes com exatamente 5 caracteres **não** entram — o operador `>` é estrito (maior que), não `>=`




---



---

### Interpretação

