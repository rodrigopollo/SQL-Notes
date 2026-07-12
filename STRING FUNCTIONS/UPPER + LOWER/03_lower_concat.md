## LOWER() — Como gerar e-mails corporativos no formato padrão da empresa?

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
        LOWER(first_name),
        '.',
        LOWER(last_name),
        '@empresa.com'
    ) AS email
FROM customer;
```


### Resultado

```
+------------+-----------+----------------------------+
| first_name | last_name | email                      |
+------------+-----------+----------------------------+
| Ana        | Souza     | ana.souza@empresa.com      |
| Bruno      | Lima      | bruno.lima@empresa.com     |
| Carla      | Mendes    | carla.mendes@empresa.com   |
| Daniel     | Rocha     | daniel.rocha@empresa.com   |
| Elisa      | Cunha     | elisa.cunha@empresa.com    |
| Fernando   | Alves     | fernando.alves@empresa.com |
| Gabriela   | Nunes     | gabriela.nunes@empresa.com |
| Henrique   | Pinto     | henrique.pinto@empresa.com |
+------------+-----------+----------------------------+
```

---

A query combina `LOWER()` e `CONCAT()` para gerar automaticamente o e-mail corporativo de cada cliente no
formato `nome.sobrenome@empresa.com`. Exibir `first_name` e `last_name` ao lado do e-mail gerado é uma boa 
prática: permite conferir visualmente se a montagem está correta antes de usar o resultado em produção. 
A diferença em relação ao exercício anterior com `@gmail.com` está apenas no domínio — a lógica é idêntica,
o que mostra como a mesma estrutura de query pode ser reutilizada para diferentes contextos apenas alterando
o texto fixo do domínio.


### O que cada parte faz

- `first_name, last_name` — colunas trazidas diretamente da tabela, sem nenhuma transformação. Exibidas ao lado do e-mail gerado para facilitar a conferência do resultado.
- `CONCAT(...) AS email` — une quatro partes em um único texto para montar o e-mail de cada cliente:
  - `LOWER(first_name)` — converte o primeiro nome para minúsculas, garantindo que o e-mail siga o padrão independentemente de como o nome está cadastrado na tabela.
  - `'.'` — ponto fixo que separa o primeiro nome do sobrenome no formato de e-mail.
  - `LOWER(last_name)` — converte o sobrenome para minúsculas pelo mesmo motivo.
  - `'@empresa.com'` — domínio corporativo fixo adicionado ao final de todos os e-mails.
- `FROM customer` — define a tabela de origem dos dados.


### Como o CONCAT monta cada e-mail
```
LOWER('Ana')  +  '.'  +  LOWER('Souza')  +  '@empresa.com'
→  'ana'      +  '.'  +  'souza'         +  '@empresa.com'
→  'ana.souza@empresa.com'
```
