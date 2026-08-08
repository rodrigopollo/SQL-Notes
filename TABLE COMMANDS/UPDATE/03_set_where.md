## UPDATE + WHERE + RETURNING — Como atualizar o dado de um usuário específico?

**Tabela utilizada:** `account`
```
account (antes do UPDATE)
+---------+----------+----------+---------------------+
| user_id | username | password | last_login          |
+---------+----------+----------+---------------------+
|       1 | Jose     | 12345    | 2025-09-29 14:37:52 |
|       2 | Maria    | abcde    | 2025-09-29 14:37:52 |
|       3 | Carlos   | qwerty   | 2025-09-29 14:37:52 |
+---------+----------+----------+---------------------+
```


### Query
```sql
UPDATE account
SET
    password = 'nova_senha_456'
WHERE
    user_id = 2
RETURNING
    user_id,
    username,
    password;
```


### Resultado
```
+---------+----------+----------------+
| user_id | username | password       |
+---------+----------+----------------+
|       2 | Maria    | nova_senha_456 |
+---------+----------+----------------+
```

---

A query atualizou apenas a senha de Maria (user_id 2),
sem afetar os demais usuários. O `RETURNING` confirmou
imediatamente o novo valor da senha após a alteração,
sem precisar de um `SELECT` separado. Apenas 1 linha
foi afetada — exatamente o esperado quando se usa
`WHERE` com chave primária, pois `user_id` é único
por definição.


### O que cada parte faz

- `UPDATE account` — seleciona a tabela `account`
  como destino da modificação.

- `SET password = 'nova_senha_456'` — define a coluna
  que será alterada e o novo valor. String entre
  aspas simples, como sempre.

- `WHERE user_id = 2` — limita a atualização à linha
  cujo `user_id` seja 2. Sem esse `WHERE`, a senha
  de todos os usuários seria alterada para o mesmo
  valor — um erro crítico em produção.

- `RETURNING user_id, username, password` — retorna
  as colunas escolhidas já com o novo valor aplicado,
  confirmando que a alteração foi feita corretamente
  na linha certa.



### Comparação — com e sem WHERE
```
SEM WHERE:
  UPDATE account
  SET password = 'nova_senha_456'
  → afeta TODOS os usuários (3 linhas)
  → Jose, Maria e Carlos teriam
    a mesma senha

COM WHERE:
  UPDATE account
  SET password = 'nova_senha_456'
  WHERE user_id = 2
  → afeta APENAS Maria (1 linha)
```

---

### Boas práticas no UPDATE
```
1. Sempre use WHERE no UPDATE — a menos que
   realmente queira alterar todas as linhas.

2. Prefira filtrar pela PRIMARY KEY (user_id)
   quando quiser afetar apenas 1 linha —
   ela garante unicidade.

3. Use RETURNING para confirmar a alteração
   sem precisar de um SELECT separado.

4. Em caso de dúvida, teste o filtro com um
   SELECT antes de rodar o UPDATE:

   SELECT * FROM account WHERE user_id = 2;
   → confirma qual linha será afetada
   → só então rode o UPDATE
```