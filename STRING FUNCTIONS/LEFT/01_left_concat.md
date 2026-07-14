## LEFT() — Como criar uma sigla com as iniciais do nome e sobrenome?

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
    CONCAT(first_name, ' ', last_name)          AS nome_completo,
    CONCAT(LEFT(first_name, 1), '.', LEFT(last_name, 1)) AS sigla
FROM customer;
```


### Resultado
```
+------------------+-------+
| nome_completo    | sigla |
+------------------+-------+
| Ana Souza        | A.S   |
| Bruno Lima       | B.L   |
| Carla Mendes     | C.M   |
| Daniel Rocha     | D.R   |
| Elisa Cunha      | E.C   |
| Fernando Alves   | F.A   |
| Gabriela Nunes   | G.N   |
| Henrique Pinto   | H.P   |
+------------------+-------+
```

---

A query extrai a inicial de cada nome e sobrenome usando `LEFT(..., 1)` e as une com um ponto no meio,
formando uma sigla de 3 caracteres por cliente. `LEFT()` é útil sempre que apenas o início de um texto 
importa — outras aplicações comuns incluem extrair o primeiro dígito de um código, pegar o prefixo de um
identificador, ou truncar um texto longo para exibição resumida. Para obter o ponto final também (`A.S.`),
bastaria adicionar `'.'` como quarto argumento: `CONCAT(LEFT(first_name, 1), '.', LEFT(last_name, 1), '.')`.


### O que cada parte faz
- `CONCAT(first_name, ' ', last_name) AS nome_completo` — une o primeiro nome, um espaço e o sobrenome exatamente como estão armazenados na tabela.
- `CONCAT(LEFT(first_name, 1), '.', LEFT(last_name, 1)) AS sigla` — monta a sigla unindo três partes:
  - `LEFT(first_name, 1)` — **novo:** `LEFT()` extrai os primeiros N caracteres de um texto, contando da esquerda. Recebe dois argumentos: a coluna ou texto de origem, e o número de caracteres a extrair. `LEFT(first_name, 1)` retorna apenas a primeira letra do nome — `'Ana'` vira `'A'`, `'Bruno'` vira `'B'`, e assim por diante.
  - `'.'` — ponto fixo que separa as duas iniciais.
  - `LEFT(last_name, 1)` — extrai a primeira letra do sobrenome pelo mesmo mecanismo.
- `FROM customer` — define a tabela de origem dos dados.
