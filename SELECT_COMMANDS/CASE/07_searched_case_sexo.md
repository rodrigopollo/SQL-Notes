## SEARCHED CASE — Como converter códigos de sexo usando condições completas?

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
    CASE
        WHEN sex = 'M' THEN 'Masculino'
        WHEN sex = 'F' THEN 'Feminino'
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

O resultado é idêntico ao exercício de `CASE
EXPRESSION` com `sex`. A diferença está apenas
na sintaxe: aqui cada `WHEN` escreve a condição
completa (`sex = 'M'`) em vez de receber só o
valor (`'M'`). Para comparações simples de
igualdade como essa, os dois funcionam igual
— a escolha fica por preferência ou consistência
com o resto do código.


### O que cada parte faz

- `CASE` sem coluna — inicia um `SEARCHED CASE`.
  Nenhuma coluna é declarada após `CASE` — cada
  `WHEN` escreve a condição inteira.

- `WHEN sex = 'M' THEN 'Masculino'` — testa
  se `sex` é igual a `'M'` e retorna
  `'Masculino'`. A coluna e o operador ficam
  dentro do `WHEN`.

- `WHEN sex = 'F' THEN 'Feminino'` — testa
  se `sex` é igual a `'F'` e retorna
  `'Feminino'`.

- `END AS sexo` — encerra o bloco `CASE` e
  nomeia a coluna de resultado.

---

### Comparação direta — mesma lógica, sintaxe diferente
```sql
-- CASE EXPRESSION (mais curto):
CASE sex
    WHEN 'M' THEN 'Masculino'
    WHEN 'F' THEN 'Feminino'
END AS sexo

-- SEARCHED CASE (mais verboso):
CASE
    WHEN sex = 'M' THEN 'Masculino'
    WHEN sex = 'F' THEN 'Feminino'
END AS sexo
```


### Quando cada um é mais vantajoso
```
Use CASE EXPRESSION quando:
  → todos os WHEN testam a MESMA coluna
  → a comparação é sempre igualdade (=)
  → quer um código mais curto e legível

Use SEARCHED CASE quando:
  → precisa de >, <, BETWEEN, IS NULL etc.
  → os WHEN testam colunas diferentes
  → precisa combinar condições com AND/OR
  → quer um único padrão para todo o código,
    mesmo nas comparações simples
```