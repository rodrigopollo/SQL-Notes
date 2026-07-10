## UPPER() — Como padronizar nomes e sobrenomes para letras maiúsculas?

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
    UPPER(first_name) AS nome_maiusculo,
    UPPER(last_name)  AS sobrenome_maiusculo
FROM customer;
```


### Resultado
```
+-------------+----------------+---------------------+
| customer_id | nome_maiusculo | sobrenome_maiusculo |
+-------------+----------------+---------------------+
|           1 | ANA            | SOUZA               |
|           2 | BRUNO          | LIMA                |
|           3 | CARLA          | MENDES              |
|           4 | DANIEL         | ROCHA               |
|           5 | ELISA          | CUNHA               |
|           6 | FERNANDO       | ALVES               |
|           7 | GABRIELA       | NUNES               |
|           8 | HENRIQUE       | PINTO               |
+-------------+----------------+---------------------+
```

---

A query exibe todos os nomes e sobrenomes padronizados em maiúsculas, sem alterar nada na tabela original.
Essa padronização é importante em situações onde os dados foram cadastrados de formas inconsistentes,
por exemplo, `'ana'`, `'ANA'` e `'Ana'` são textos diferentes para o banco, e uma busca por `'ANA'` não 
encontraria `'ana'`. Converter tudo para o mesmo padrão (`UPPER` ou `LOWER`) antes de comparar ou exibir 
garante consistência. Na prática, `LOWER()` é mais usado para comparações em filtros 
(`WHERE LOWER(first_name) = 'ana'`), enquanto `UPPER()` aparece mais em relatórios e etiquetas onde a 
apresentação visual em caixa alta é desejada.


### O que cada parte faz

- `customer_id` — coluna trazida diretamente da tabela, sem nenhuma transformação.
- `UPPER(first_name) AS nome_maiusculo` — converte todos os caracteres de `first_name` para letras maiúsculas
e exibe o resultado com o apelido `nome_maiusculo`. O valor original na tabela não é alterado — a conversão 
existe apenas na exibição.
- `UPPER(last_name) AS sobrenome_maiusculo` — aplica a mesma conversão sobre `last_name`, exibindo o sobrenome 
inteiramente em maiúsculas.
- `FROM customer` — define a tabela de origem dos dados.

> **Referência rápida — `UPPER` vs `LOWER`:**
>
> | Função         | O que faz                | Exemplo                  |
> |----------------|--------------------------|--------------------------|
> | `UPPER(texto)` | converte para MAIÚSCULAS | `UPPER('Ana')` → `'ANA'` |
> | `LOWER(texto)` | converte para minúsculas | `LOWER('Ana')` → `'ana'` |
