## CONCAT() — Como montar um e-mail corporativo a partir do nome e sobrenome?

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
    CONCAT(first_name, ' ', last_name) AS nome_completo,
    CONCAT(LOWER(first_name), '.', LOWER(last_name), '@gmail.com') AS email
FROM customer;
```


### Resultado
```
+------------------+----------------------------+
| nome_completo    | email                      |
+------------------+----------------------------+
| Ana Souza        | ana.souza@gmail.com        |
| Bruno Lima       | bruno.lima@gmail.com       |
| Carla Mendes     | carla.mendes@gmail.com     |
| Daniel Rocha     | daniel.rocha@gmail.com     |
| Elisa Cunha      | elisa.cunha@gmail.com      |
| Fernando Alves   | fernando.alves@gmail.com   |
| Gabriela Nunes   | gabriela.nunes@gmail.com   |
| Henrique Pinto   | henrique.pinto@gmail.com   |
+------------------+----------------------------+
```

---

Este é um dos exemplos mais próximos de uso real do `CONCAT()`: gerar e-mails corporativos automaticamente 
a partir de dados já existentes na tabela. O padrão `nome.sobrenome@dominio.com` é amplamente adotado por
empresas, e `LOWER()` garante que o resultado siga a convenção de letras minúsculas independentemente de como
o nome está cadastrado no banco. Na prática, esse tipo de query é usado em migrações de dados, onboarding de
novos funcionários ou geração de relatórios onde o e-mail precisa ser reconstruído a partir de partes separadas.

### O que cada parte faz

- `CONCAT(first_name, ' ', last_name) AS nome_completo` — une o primeiro nome, um espaço e o sobrenome exatamente como estão armazenados na tabela, mantendo a capitalização original.
- `CONCAT(LOWER(first_name), '.', LOWER(last_name), '@gmail.com') AS email` — monta o e-mail unindo quatro partes:
  - `LOWER(first_name)` — **novo:** `LOWER()` é uma função de string que converte todos os caracteres de um texto para letras minúsculas. Necessário aqui pois endereços de e-mail são convencionalmente escritos em minúsculas — sem ele, o resultado seria `Ana.Souza@gmail.com` em vez de `ana.souza@gmail.com`.
  - `'.'` — ponto fixo que separa o primeiro nome do sobrenome no formato de e-mail.
  - `LOWER(last_name)` — sobrenome convertido para minúsculas pelo mesmo motivo.
  - `'@gmail.com'` — domínio fixo adicionado ao final de todos os e-mails.
- `FROM customer` — define a tabela de origem dos dados.



### Como o CONCAT monta cada e-mail
```
LOWER('Ana')  +  '.'  +  LOWER('Souza')  +  '@gmail.com'
→  'ana'      +  '.'  +  'souza'         +  '@gmail.com'
→  'ana.souza@gmail.com'
```
