## ALTER TABLE — Como resolver erro de NOT NULL em uma coluna?

**Tabela utilizada:** `new_info`
```
new_info
+----+--------+-------------------+
| id | people | title             |
+----+--------+-------------------+
|  1 | Jose   | dados gerais      |
|  2 | Maria  | dados adicionais  |
+----+--------+-------------------+
```

> A coluna `people` foi criada com `NOT NULL` —
> ou seja, não aceita registros sem valor nessa coluna.

---

### O problema
```sql
INSERT INTO new_info(title)
VALUES ('some new title');
```

```
Erro copiado nao criado.

ERROR: null value in column "people" violates
not-null constraint
DETAIL: Failing row contains
(3, null, some new title)
```


### Interpretação do erro 

O `INSERT` tentou criar um registro informando
apenas `title`, deixando `people` sem valor.
Como `people` tem `NOT NULL`, o banco rejeitou
a operação — ele não pode armazenar `NULL`
nessa coluna. Existem duas formas de resolver.

---

### Solução 1 — Informar o valor no INSERT
```sql
INSERT INTO new_info(
    title,
    people
)
VALUES
    ('some new title', 'Jose');
```


### Resultado — Solução 1
```
+----+--------+----------------+
| id | people | title          |
+----+--------+----------------+
|  1 | Jose   | dados gerais   |
|  2 | Maria  | dados adicionais|
|  3 | Jose   | some new title |
+----+--------+----------------+
```

---

### Solução 2 — Remover a restrição NOT NULL

```sql
ALTER TABLE new_info
ALTER COLUMN people DROP NOT NULL;
```

Depois disso, o `INSERT` original passa a funcionar:

```sql
INSERT INTO new_info(title)
VALUES ('some new title');
```


### Resultado — Solução 2
```
+----+--------+----------------+
| id | people | title          |
+----+--------+----------------+
|  1 | Jose   | dados gerais   |
|  2 | Maria  | dados adicionais|
|  3 | NULL   | some new title |
+----+--------+----------------+
```

---

### O que cada parte faz

- `ALTER TABLE new_info` — seleciona a tabela
  cuja estrutura será modificada.

- `ALTER COLUMN people` — seleciona a coluna
  específica que terá sua restrição alterada.

- `DROP NOT NULL` — remove a restrição `NOT NULL`
  da coluna `people`. A partir desse momento,
  a coluna passa a aceitar `NULL`.



### Quando usar cada solução
```
Solução 1 — Informar o valor no INSERT:
  → quando a coluna DEVE ter um valor sempre
  → mantém a integridade dos dados
  → recomendada na maioria dos casos

Solução 2 — DROP NOT NULL:
  → quando a coluna pode ser opcional
  → altera a regra da tabela permanentemente
  → use com cautela — remove uma proteção
    que foi definida por algum motivo
```