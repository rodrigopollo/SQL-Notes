## ALTER TABLE — Como remover uma coluna de uma tabela existente?

**Tabela utilizada:** `account`
```
account (antes do DROP COLUMN)
+---------+----------+--------+---------------------+
| user_id | username | active | created_on          |
+---------+----------+--------+---------------------+
|       1 | Jose     | TRUE   | 2025-01-10 09:00:00 |
|       2 | Maria    | TRUE   | 2025-03-22 14:00:00 |
|       3 | Carlos   | TRUE   | 2025-07-05 11:00:00 |
+---------+----------+--------+---------------------+
```


### Query
```sql
ALTER TABLE account
DROP COLUMN active CASCADE;
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

A query removeu permanentemente a coluna `active`
da tabela `account`, junto com tudo que dependia
dela. Os dados das demais colunas permanecem
intactos. `DROP COLUMN` é irreversível — não existe
desfazer após a execução.



### O que cada parte faz

- `ALTER TABLE account` — seleciona a tabela
  cuja estrutura será modificada.

- `DROP COLUMN active` — remove permanentemente
  a coluna `active` e todos os dados que ela
  continha. Diferente de `UPDATE`, que altera
  dados, `DROP COLUMN` altera a estrutura da
  tabela.

- `CASCADE` — remove a coluna **e tudo que
  depende dela** automaticamente, sem perguntar.
  Isso inclui:

```
  ✗ views que usam a coluna active
  ✗ índices criados sobre active
  ✗ constraints que referenciam active
  ✗ funções que dependem de active
```

---

### CASCADE vs RESTRICT

```sql
-- CASCADE → remove a coluna e tudo que
-- depende dela (sem aviso):
ALTER TABLE account
DROP COLUMN active CASCADE;

-- RESTRICT → comportamento padrão. Bloqueia
-- o DROP se existir qualquer dependência,
-- retornando erro com o nome do que depende:
ALTER TABLE account
DROP COLUMN active RESTRICT;

-- Erro gerado pelo RESTRICT:
ERROR: cannot drop column active of table
account because other objects depend on it
DETAIL: view active_users depends on
column active of table account
```

> `RESTRICT` é mais seguro pois força você a
> verificar e remover as dependências manualmente
> antes de apagar a coluna, evitando surpresas.

---

### Tem que ter atenção com CASCADE
```
CASCADE pode apagar muito mais do que você
espera. Antes de usar, verifique o que depende
da coluna:

SELECT *
FROM information_schema.columns
WHERE table_name = 'account'
AND column_name = 'active';

→ só use CASCADE quando tiver certeza de
  que tudo que será removido junto pode
  ser apagado com segurança.
```