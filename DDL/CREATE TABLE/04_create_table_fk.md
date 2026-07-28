## CREATE TABLE FK — Como criar uma tabela com chaves estrangeiras?


### Query
```sql
CREATE TABLE account_job (
    user_id   INTEGER   REFERENCES account(user_id),
    job_id    INTEGER   REFERENCES job(job_id),
    hire_date TIMESTAMP
);
```



### Resultado — estrutura da tabela criada
```
+-----------+-----------+------------------------------+
| coluna    | tipo      | restrições                   |
+-----------+-----------+------------------------------+
| user_id   | INTEGER   | FOREIGN KEY → account.user_id|
| job_id    | INTEGER   | FOREIGN KEY → job.job_id     |
| hire_date | TIMESTAMP | (nenhuma)                    |
+-----------+-----------+------------------------------+
```

---


A tabela `account_job` liga um usuário a um cargo,
armazenando também a data de contratação. É um exemplo
clássico de **tabela de junção** — ela não representa
uma entidade por si só, mas a relação entre duas:
`account` e `job`. As duas chaves estrangeiras garantem
que só é possível vincular usuários e cargos que já
existam em suas respectivas tabelas.

---

### O que cada parte faz

- `user_id INTEGER REFERENCES account(user_id)` —
  coluna do tipo inteiro que referencia a coluna
  `user_id` da tabela `account`. `REFERENCES` é a
  forma inline de declarar uma chave estrangeira —
  mais curta que o `CONSTRAINT ... FOREIGN KEY`
  visto no exercício anterior, mas com o mesmo
  efeito: o banco rejeita qualquer `user_id` que
  não exista em `account`.

- `job_id INTEGER REFERENCES job(job_id)` — mesma
  lógica aplicada ao cargo: só aceita valores que
  existam na coluna `job_id` da tabela `job`.

- `hire_date TIMESTAMP` — data e hora de contratação.
  Sem `NOT NULL` — pode ser preenchida depois.

---

### REFERENCES inline vs CONSTRAINT explícito

```sql
-- Forma inline (este exercício) — mais curta:
user_id INTEGER REFERENCES account(user_id)

-- Forma explícita (exercício anterior) — com nome:
CONSTRAINT fk_user
    FOREIGN KEY (user_id)
    REFERENCES account(user_id)
```

A forma inline é mais rápida de escrever. A forma
com `CONSTRAINT` e nome explícito é preferida em
ambientes profissionais pois facilita identificar
e remover a restrição no futuro com:

```sql
ALTER TABLE account_job
DROP CONSTRAINT fk_user;
```

Sem nome definido, o banco gera um nome automático
difícil de identificar.

---

### Observação sobre boas práticas
Esta tabela não tem `PRIMARY KEY` definida. Em um
ambiente de produção, o recomendado seria adicionar
uma chave primária composta pelos dois ids, evitando
duplicatas no vínculo usuário-cargo:

```sql
PRIMARY KEY (user_id, job_id)
```