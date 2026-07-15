## LEFT() — Como gerar um nome de usuário automático com as primeiras letras do nome e sobrenome?

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
    first_name,
    last_name,
    CONCAT(
        LOWER(LEFT(first_name, 3)),
        LOWER(LEFT(last_name, 3))
    ) AS usuario
FROM customer;
```


### Resultado
```
+------------+-----------+---------+
| first_name | last_name | usuario |
+------------+-----------+---------+
| Ana        | Souza     | anasou  |
| Bruno      | Lima      | brulim  |
| Carla      | Mendes    | carmen  |
| Daniel     | Rocha     | danroc  |
| Elisa      | Cunha     | elicun  |
| Fernando   | Alves     | feralv  |
| Gabriela   | Nunes     | gabnun  |
| Henrique   | Pinto     | henpin  |
+------------+-----------+---------+
```

---

A query gera automaticamente um nome de usuário padronizado para cada cliente, combinando os 3 primeiros 
caracteres do nome com os 3 primeiros do sobrenome, tudo em minúsculas. Esse padrão é muito comum em sistemas
corporativos para criação de logins, usuários de rede ou credenciais de acesso. `LEFT()` garante que o 
resultado tenha sempre o mesmo comprimento por parte, independentemente do tamanho do nome original 
"Fernando" e "Ana" ambos contribuem com exatamente 3 caracteres para o usuário final.


### O que cada parte faz

- `first_name, last_name` — colunas trazidas diretamente da tabela, exibidas ao lado do usuário gerado para
facilitar a conferência do resultado.
- `CONCAT(...) AS usuario` — une duas partes para montar o nome de usuário de cada cliente:
  - `LOWER(LEFT(first_name, 3))` — extrai os 3 primeiros caracteres do nome com `LEFT()` e converte para 
  minúsculas com `LOWER()`. As duas funções são combinadas: `LEFT()` age primeiro, retornando o trecho do 
  texto; `LOWER()` age em seguida, convertendo esse trecho.
  - `LOWER(LEFT(last_name, 3))` — aplica a mesma lógica sobre o sobrenome.
- `FROM customer` — define a tabela de origem dos dados.
