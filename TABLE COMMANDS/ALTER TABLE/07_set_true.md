## ALTER TABLE — Como adicionar um valor padrão em uma coluna existente?

**Tabela utilizada:** `account`
```
account (antes do SET DEFAULT)
+---------+----------+--------+
| user_id | username | active |
+---------+----------+--------+
|       1 | Jose     | NULL   |
|       2 | Maria    | NULL   |
|       3 | Carlos   | NULL   |
+---------+----------+--------+
```


### Query
```sql
ALTER TABLE account
ALTER COLUMN active SET DEFAULT TRUE;
```


### Resultado
```
-- Antes do SET DEFAULT:
INSERT INTO account (username)
VALUES ('Pedro');
→ active fica NULL

-- Depois do SET DEFAULT:
INSERT INTO account (username)
VALUES ('Pedro');
→ active recebe TRUE automaticamente
```


```
account (depois do INSERT com SET DEFAULT ativo)
+---------+----------+--------+
| user_id | username | active |
+---------+----------+--------+
|       1 | Jose     | NULL   |
|       2 | Maria    | NULL   |
|       3 | Carlos   | NULL   |
|       4 | Pedro    | TRUE   |
+---------+----------+--------+
```

---

A query adicionou `DEFAULT TRUE` à coluna `active`.
Os registros já existentes (Jose, Maria, Carlos) não
foram afetados — continuam com `NULL` pois o `DEFAULT`
só age em novos `INSERT`. Pedro foi o primeiro inserido
após o `SET DEFAULT`, por isso recebeu `TRUE`
automaticamente sem precisar ser informado.



### O que cada parte faz

- `ALTER TABLE account` — seleciona a tabela
  cuja estrutura será modificada.

- `ALTER COLUMN active` — seleciona a coluna
  que receberá a nova regra.

- `SET DEFAULT TRUE` — define `TRUE` como valor
  padrão da coluna `active`. A partir desse
  momento, qualquer `INSERT` que não informar
  `active` receberá `TRUE` automaticamente.
  Booleano sem aspas.



### Corrigindo os registros antigos com NULL

```sql
-- SET DEFAULT não atualiza registros existentes.
-- Para corrigir os NULLs antigos, usar UPDATE:

UPDATE account
SET active = TRUE
WHERE active IS NULL;
```

```
account (depois do UPDATE)
+---------+----------+--------+
| user_id | username | active |
+---------+----------+--------+
|       1 | Jose     | TRUE   |
|       2 | Maria    | TRUE   |
|       3 | Carlos   | TRUE   |
|       4 | Pedro    | TRUE   |
+---------+----------+--------+
```

---

### SET DEFAULT vs DROP DEFAULT

```sql
-- Adiciona valor padrão à coluna:
ALTER TABLE account
ALTER COLUMN active SET DEFAULT TRUE;

-- Remove o valor padrão da coluna:
ALTER TABLE account
ALTER COLUMN active DROP DEFAULT;
```