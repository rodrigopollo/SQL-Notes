## CONCAT() — Como adicionar um texto fixo antes do nome completo de cada cliente?

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
    CONCAT('Cliente: ', first_name, ' ', last_name) AS saudacao
FROM customer;
```


### Resultado
```
+-------------------------+
| saudacao                |
+-------------------------+
| Cliente: Ana Souza      |
| Cliente: Bruno Lima     |
| Cliente: Carla Mendes   |
| Cliente: Daniel Rocha   |
| Cliente: Elisa Cunha    |
| Cliente: Fernando Alves |
| Cliente: Gabriela Nunes |
| Cliente: Henrique Pinto |
+-------------------------+
```

---

### O que cada parte faz

- `CONCAT('Cliente: ', first_name, ' ', last_name) AS saudacao` — une quatro argumentos em um único texto, na
ordem em que são passados:
  - `'Cliente: '` — texto fixo definido diretamente na query, que aparece igual em todas as linhas do resultado. Não vem de nenhuma coluna da tabela. O espaço após os dois pontos já está incluído dentro da string.
  - `first_name` — o valor da coluna de primeiro nome de cada linha.
  - `' '` — espaço em branco fixo para separar o primeiro nome do sobrenome.
  - `last_name` — o valor da coluna de sobrenome de cada linha.
- `AS saudacao` — apelido para nomear a coluna resultante de forma legível.
- `FROM customer` — define a tabela de origem dos dados.



### Como o CONCAT monta cada linha
```
'Cliente: '  +  'Ana'  +  ' '  +  'Souza'  →  'Cliente: Ana Souza'
'Cliente: '  +  'Bruno'  +  ' '  +  'Lima'  →  'Cliente: Bruno Lima'
```






A diferença em relação ao exercício anterior é a adição de um texto fixo (`'Cliente: '`) como primeiro
argumento do `CONCAT()`. Esse texto aparece idêntico em todas as linhas — não vem da tabela, é inserido
diretamente na query. Esse padrão é muito usado na prática para gerar mensagens personalizadas, etiquetas,
descrições ou qualquer saída onde um prefixo ou sufixo fixo precisa ser combinado com dados variáveis de
cada registro.