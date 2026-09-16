## CREATE TABLE — Como criar uma tabela de funcionários com salário e cargo?

**Tabela criada:** `employee`
```
employee (estrutura após o CREATE TABLE)
+------------+--------------+---------------------------+
| coluna     | tipo         | restrições                |
+------------+--------------+---------------------------+
| emp_id     | SERIAL       | PRIMARY KEY               |
| full_name  | VARCHAR(100) | NOT NULL                  |
| email      | VARCHAR(250) | UNIQUE, NOT NULL          |
| salary     | NUMERIC(10,2)| NOT NULL, CHECK (> 0)     |
| department | VARCHAR(50)  | NOT NULL                  |
| hire_date  | DATE         | NOT NULL                  |
| is_active  | BOOLEAN      | NOT NULL, DEFAULT TRUE    |
| manager_id | INTEGER      | REFERENCES employee(emp_id)|
+------------+--------------+---------------------------+
```


### Query

```sql
CREATE TABLE employee (
    emp_id      SERIAL          PRIMARY KEY,
    full_name   VARCHAR(100)    NOT NULL,
    email       VARCHAR(250)    UNIQUE NOT NULL,
    salary      NUMERIC(10, 2)  NOT NULL
                CHECK (salary > 0),
    department  VARCHAR(50)     NOT NULL,
    hire_date   DATE            NOT NULL,
    is_active   BOOLEAN         NOT NULL DEFAULT TRUE,
    manager_id  INTEGER         REFERENCES employee(emp_id)
);
```



### Resultado
```
employee (pronta para receber dados)
+--------+-----------+-------+--------+------------+-----------+-----------+------------+
| emp_id | full_name | email | salary | department | hire_date | is_active | manager_id |
+--------+-----------+-------+--------+------------+-----------+-----------+------------+
| (vazia)|           |       |        |            |           |           |            |
+--------+-----------+-------+--------+------------+-----------+-----------+------------+
```

---

A query cria a tabela `employee` com 8 colunas.
O ponto mais interessante é `manager_id` — uma
chave estrangeira que referencia a **própria tabela**
`employee`. Isso significa que um funcionário pode
ter um gerente que também é funcionário da mesma
tabela. Esse padrão é chamado de **self-referencing
foreign key** e é muito comum em estruturas
hierárquicas como organogramas.



### O que cada parte faz

- `emp_id SERIAL PRIMARY KEY` — identificador
  gerado automaticamente a cada novo funcionário.
  Único e nunca nulo.

- `full_name VARCHAR(100) NOT NULL` — nome completo
  do funcionário, obrigatório, com até 100
  caracteres.

- `email VARCHAR(250) UNIQUE NOT NULL` — e-mail
  obrigatório e único — dois funcionários não
  podem ter o mesmo e-mail.

- `salary NUMERIC(10, 2) NOT NULL CHECK (salary > 0)`
  — salário em formato monetário com até 10 dígitos
  no total e 2 decimais. `CHECK (salary > 0)` impede
  que salários zero ou negativos sejam cadastrados.

- `department VARCHAR(50) NOT NULL` — departamento
  do funcionário (ex: `'TI'`, `'RH'`, `'Financeiro'`).
  Obrigatório.

- `hire_date DATE NOT NULL` — **novo neste contexto:**
  `DATE` armazena apenas a data sem horário
  (ex: `2025-01-10`), diferente de `TIMESTAMP`
  que armazena data e hora. Para data de contratação,
  o horário não é relevante — `DATE` é suficiente.

- `is_active BOOLEAN NOT NULL DEFAULT TRUE` —
  indica se o funcionário está ativo. `DEFAULT TRUE`
  faz todo funcionário nascer ativo sem precisar
  informar esse campo no `INSERT`.

- `manager_id INTEGER REFERENCES employee(emp_id)`
  — **novo:** chave estrangeira que aponta para
  a **própria tabela** `employee`. Permite registrar
  quem é o gerente de cada funcionário. Sem `NOT NULL`
  pois o CEO ou dono da empresa não tem gerente —
  seu `manager_id` seria `NULL`.



### Como um INSERT nessa tabela ficaria
```sql
-- Inserindo o gerente primeiro (sem manager_id):
INSERT INTO employee (
    full_name, email, salary,
    department, hire_date
)
VALUES (
    'Carlos Silva',
    'carlos@empresa.com',
    8000.00,
    'TI',
    '2020-03-10'
);

-- Inserindo funcionário com gerente (emp_id 1):
INSERT INTO employee (
    full_name, email, salary,
    department, hire_date, manager_id
)
VALUES (
    'Jose Lima',
    'jose@empresa.com',
    4500.00,
    'TI',
    '2023-06-15',
    1
);
```

```
+--------+--------------+--------------------+---------+------------+------------+-----------+------------+
| emp_id | full_name    | email              | salary  | department | hire_date  | is_active | manager_id |
+--------+--------------+--------------------+---------+------------+------------+-----------+------------+
|      1 | Carlos Silva | carlos@empresa.com | 8000.00 | TI         | 2020-03-10 | TRUE      | NULL       |
|      2 | Jose Lima    | jose@empresa.com   | 4500.00 | TI         | 2023-06-15 | TRUE      | 1          |
+--------+--------------+--------------------+---------+------------+------------+-----------+------------+
```

---

### Self-referencing foreign key
```
employee
+--------+--------------+------------+
| emp_id | full_name    | manager_id |
+--------+--------------+------------+
|      1 | Carlos Silva | NULL       | ← sem gerente (é o chefe)
|      2 | Jose Lima    | 1          | ← gerenciado por Carlos
|      3 | Maria Rocha  | 1          | ← gerenciada por Carlos
|      4 | Pedro Costa  | 2          | ← gerenciado por Jose
+--------+--------------+------------+

Carlos → gerencia Jose e Maria
Jose   → gerencia Pedro
Pedro  → não gerencia ninguém
```