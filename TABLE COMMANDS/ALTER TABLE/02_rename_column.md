## ALTER TABLE — Como renomear uma coluna?

**Tabela utilizada:** `new_info`
```
new_info (antes do RENAME COLUMN)
+----+--------+-------------------+
| id | person | description       |
+----+--------+-------------------+
|  1 | Jose   | dados gerais      |
|  2 | Maria  | dados adicionais  |
+----+--------+-------------------+
```


### Query
```sql
ALTER TABLE new_info
RENAME COLUMN person TO people;
```


### Resultado
```
-- Antes:
SELECT person FROM new_info;  → funciona ✓

-- Depois:
SELECT person FROM new_info;  → erro ✗
SELECT people FROM new_info;  → funciona ✓
```

---

A query renomeou a coluna `person` para `people`
dentro da tabela `new_info`. Os dados da coluna
e toda a estrutura restante da tabela permanecem
intactos — apenas o nome da coluna muda.
A partir deste momento, qualquer query que
referencie o nome antigo (`person`) retornará
erro.



### O que cada parte faz

- `ALTER TABLE new_info` — seleciona a tabela
  que será modificada.

- `RENAME COLUMN person TO people` — define o
  nome antigo da coluna (`person`) e o novo
  nome que ela receberá (`people`).



### RENAME TO vs RENAME COLUMN
```sql
-- Renomeia a tabela inteira:
ALTER TABLE information
RENAME TO new_info;

-- Renomeia uma coluna específica:
ALTER TABLE new_info
RENAME COLUMN person TO people;
```

---

### Devo ter atenção quando renomear colunas
```
Após o RENAME COLUMN, tudo que referencia
o nome antigo precisa ser atualizado:

  ✗ SELECT person FROM new_info
  ✗ WHERE person = 'Jose'
  ✗ ORDER BY person
  ✗ views que usam a coluna person
  ✗ código da aplicação que usa person

→ Todos precisam ser atualizados para people
```