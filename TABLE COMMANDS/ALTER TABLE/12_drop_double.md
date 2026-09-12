## ALTER TABLE — Como remover múltiplas colunas em um único comando?

**Tabela utilizada:** `account`
```
account (antes do DROP COLUMN)
+---------+----------+--------+------------+---------------------+
| user_id | username | active | last_login | created_on          |
+---------+----------+--------+------------+---------------------+
|       1 | Jose     | TRUE   | 2025-09-29 | 2025-01-10 09:00:00 |
|       2 | Maria    | TRUE   | 2025-09-29 | 2025-03-22 14:00:00 |
|       3 | Carlos   | TRUE   | NULL       | 2025-07-05 11:00:00 |
+---------+----------+--------+------------+---------------------+
```



### Query
```sql
ALTER TABLE account
DROP COLUMN active,
DROP COLUMN last_login;
```



### Resultado
```
account (depois do DROP COLUMN)
+---------+----------+---------------------+
| user_id | username | created_on          |
+---------+----------+---------------------+
|       1 | Jose     | 2025-01-10 09:00:00 |
|       2 | Maria    | 2025-03-22 14:00:00 |
|       3 | Carlos   | 2025-07-05 11:00:00 |
+---------+----------+---------------------+
```

---

A query removeu permanentemente as colunas `active`
e `last_login` da tabela `account` em uma única
operação. Todos os dados dessas colunas foram
perdidos. As colunas restantes e seus dados
permanecem intactos.



### O que cada parte faz

- `ALTER TABLE account` — seleciona a tabela
  cuja estrutura será modificada.

- `DROP COLUMN active` — remove permanentemente
  a coluna `active` e todos os seus dados.

- `DROP COLUMN last_login` — remove permanentemente
  a coluna `last_login` e todos os seus dados.
  Cada `DROP COLUMN` adicional é separado por
  vírgula no mesmo `ALTER TABLE`.



### Um DROP por vez vs múltiplos em um comando
```sql
-- Um DROP por vez (menos eficiente):
ALTER TABLE account DROP COLUMN active;
ALTER TABLE account DROP COLUMN last_login;

-- Múltiplos DROPs em um único comando
-- (recomendado):
ALTER TABLE account
DROP COLUMN active,
DROP COLUMN last_login;
```


### Combinando IF EXISTS com múltiplos DROPs
```sql
-- Versão segura — não gera erro se alguma
-- das colunas não existir:
ALTER TABLE account
DROP COLUMN IF EXISTS active,
DROP COLUMN IF EXISTS last_login;
```

---

### Atenção antes de executar
```
Sempre confirme os dados antes de remover:

SELECT active, last_login
FROM account;

→ só execute o DROP COLUMN após ter certeza
  de que os dados podem ser apagados.
```