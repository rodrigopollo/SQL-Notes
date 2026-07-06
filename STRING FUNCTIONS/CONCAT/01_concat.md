## CONCAT() — Como juntar o primeiro nome e o sobrenome em uma só coluna?

**Tabela utilizada:** `customer`

```
+------------+-----------+
| first_name | last_name |
+------------+-----------+
| Ana        | Souza     |
| Bruno      | Lima      |
| Carla      | Mendes    |
| Daniel     | Rocha     |
| Elisa      | Cunha     |
| Fernando   | Alves     |
| Gabriela   | Nunes     |
| Henrique   | Pinto     |
+------------+-----------+
```

### Query
```sql
SELECT
    CONCAT(first_name, ' ', last_name) AS nome_completo
FROM customer;
```

### Resultado
```
+-----------------+
| nome_completo   |
+-----------------+
| Ana Souza       |
| Bruno Lima      |
| Carla Mendes    |
| Daniel Rocha    |
| Elisa Cunha     |
| Fernando Alves  |
| Gabriela Nunes  |
| Henrique Pinto  |
+-----------------+
```

---

A query une `first_name` e `last_name` em uma única coluna de exibição, sem alterar nada na tabela. Manter 
nome e sobrenome em colunas separadas é uma boa prática de banco de dados — permite filtrar, ordenar e buscar
por cada parte individualmente. `CONCAT()` entra em cena apenas na camada de exibição, quando o resultado
precisa ser apresentado de forma legível para o usuário final, exportado para um relatório, ou enviado para
outro sistema.


### O que cada parte faz

- `CONCAT(first_name, ' ', last_name) AS nome_completo` — **novo:** `CONCAT()` é uma função de string que une
dois ou mais valores de texto em um só, na ordem em que são passados. Aceita qualquer quantidade de argumentos
separados por vírgula. Neste caso recebe três argumentos:
  - `first_name` — o valor da coluna de primeiro nome.
  - `' '` — um espaço em branco fixo, definido diretamente na query, para separar os dois nomes. Sem ele, 
  o resultado seria `AnaSouza` em vez de `Ana Souza`.
  - `last_name` — o valor da coluna de sobrenome.
- `AS nome_completo` — apelido para nomear a coluna resultante. Sem ele, o PostgreSQL exibiria `concat` 
como nome da coluna — pouco legível e pouco profissional.
- `FROM customer` — define a tabela de origem dos dados.