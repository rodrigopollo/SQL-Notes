## ERROR — Como resolver erro de UNIQUE em uma coluna?

**Tabela utilizada:** `account`
```
account
+---------+----------+---------------------------+
| user_id | username | email                     |
+---------+----------+---------------------------+
|       1 | Jose     | jose@mail.com             |
|       2 | Maria    | maria@mail.com            |
|       3 | Carlos   | carlos@mail.com           |
+---------+----------+---------------------------+
```

> A coluna `email` foi criada com `UNIQUE NOT NULL`
> — não aceita dois registros com o mesmo e-mail.


### O problema
```sql
INSERT INTO account (username, email)
VALUES ('Pedro', 'jose@mail.com');
```

```
ERROR: duplicate key value violates unique
constraint "account_email_key"
DETAIL: Key (email)=(jose@mail.com) already
exists.
```



### O erro

O `INSERT` tentou cadastrar Pedro com o e-mail
`jose@mail.com`, que já pertence a Jose. Como
`email` tem `UNIQUE`, o banco rejeitou a operação
— dois registros não podem ter o mesmo valor
nessa coluna. Existem duas formas de resolver.

---

### Solução 1 — Usar um e-mail diferente no INSERT
```sql
INSERT INTO account (username, email)
VALUES ('Pedro', 'pedro@mail.com');
```

### Resultado — Solução 1
```
+---------+----------+---------------------------+
| user_id | username | email                     |
+---------+----------+---------------------------+
|       1 | Jose     | jose@mail.com             |
|       2 | Maria    | maria@mail.com            |
|       3 | Carlos   | carlos@mail.com           |
|       4 | Pedro    | pedro@mail.com            |
+---------+----------+---------------------------+
```

---

### Solução 2 — Remover a restrição UNIQUE

```sql
ALTER TABLE account
DROP CONSTRAINT account_email_key;
```

Depois disso, o `INSERT` original passa a funcionar:

```sql
INSERT INTO account (username, email)
VALUES ('Pedro', 'jose@mail.com');
```

### Resultado — Solução 2
```
+---------+----------+---------------------------+
| user_id | username | email                     |
+---------+----------+---------------------------+
|       1 | Jose     | jose@mail.com             |
|       2 | Maria    | maria@mail.com            |
|       3 | Carlos   | carlos@mail.com           |
|       4 | Pedro    | jose@mail.com             |
+---------+----------+---------------------------+
```

---

### O que cada parte faz

- `ALTER TABLE account` — seleciona a tabela
  cuja estrutura será modificada.

- `DROP CONSTRAINT account_email_key` — remove
  a restrição `UNIQUE` da coluna `email`. O nome
  da constraint (`account_email_key`) é gerado
  automaticamente pelo PostgreSQL no padrão
  `tabela_coluna_key` quando não foi definido
  um nome explícito na criação da tabela.

> **Como descobrir o nome da constraint:**
> ```sql
> SELECT constraint_name
> FROM information_schema.table_constraints
> WHERE table_name = 'account';
> ```



### Quando usar cada solução

```
Solução 1 — Usar um valor diferente no INSERT:
  → quando a restrição UNIQUE faz sentido
    e deve ser mantida
  → o dado inserido estava simplesmente errado
  → recomendada na maioria dos casos

Solução 2 — DROP CONSTRAINT:
  → quando a regra de unicidade não faz
    mais sentido para o negócio
  → altera a estrutura da tabela permanentemente
  → use com cautela — permite duplicatas
    que antes eram bloqueadas
```