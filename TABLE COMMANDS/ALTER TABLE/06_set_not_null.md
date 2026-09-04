## ALTER TABLE — Como adicionar a restrição NOT NULL em uma coluna existente?

**Tabela utilizada:** `new_info`
```
new_info (antes do SET NOT NULL)
+----+--------+-------------------+
| id | people | title             |
+----+--------+-------------------+
|  1 | Jose   | dados gerais      |
|  2 | Maria  | dados adicionais  |
|  3 | NULL   | some new title    |
+----+--------+-------------------+
```


### Query
```sql
ALTER TABLE new_info
ALTER COLUMN people SET NOT NULL;
```


### Resultado
```
-- Antes:
INSERT INTO new_info(title)
VALUES ('outro titulo');
→ funciona ✓ (people fica NULL)

-- Depois:
INSERT INTO new_info(title)
VALUES ('outro titulo');
→ erro ✗
ERROR: null value in column "people"
violates not-null constraint
```

---

A query adicionou a restrição `NOT NULL` à coluna
`people`. A partir desse momento, todo `INSERT` ou
`UPDATE` que deixar `people` sem valor será rejeitado
pelo banco. É o oposto do `DROP NOT NULL` visto no
exercício anterior.



### O que cada parte faz

- `ALTER TABLE new_info` — seleciona a tabela
  cuja estrutura será modificada.

- `ALTER COLUMN people` — seleciona a coluna
  específica que terá sua restrição alterada.

- `SET NOT NULL` — adiciona a restrição `NOT NULL`
  à coluna `people`. A partir desse momento,
  a coluna não aceita mais `NULL`.



### Atenção antes de usar SET NOT NULL

```
Se a tabela já tiver registros com NULL
na coluna, o banco rejeita o comando:

ERROR: column "people" of relation "new_info"
contains null values

→ É necessário atualizar os NULLs antes:

UPDATE new_info
SET people = 'desconhecido'
WHERE people IS NULL;

→ Só então rodar o SET NOT NULL.
```

---

### SET NOT NULL vs DROP NOT NULL

```sql
-- Adiciona a restrição (coluna passa a ser
-- obrigatória):
ALTER TABLE new_info
ALTER COLUMN people SET NOT NULL;

-- Remove a restrição (coluna passa a ser
-- opcional):
ALTER TABLE new_info
ALTER COLUMN people DROP NOT NULL;
```