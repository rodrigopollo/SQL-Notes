## CREATE TABLE — Como criar uma tabela com chave primária e restrições?


### Query
```sql
CREATE TABLE account (
    user_id     SERIAL          PRIMARY KEY,
    username    VARCHAR(50)     NOT NULL,
    birthdate   DATE            CHECK (birthdate > '1900-01-01'),
    password    VARCHAR(50)     NOT NULL,
    email       VARCHAR(250)    UNIQUE NOT NULL,
    created_on  TIMESTAMP       NOT NULL,
    last_login  TIMESTAMP
);
```

### Resultado — estrutura da tabela criada

```
+-----------+--------------+-----------------------------+
| coluna    | tipo         | restrições                  |
+-----------+--------------+-----------------------------+
| user_id   | SERIAL       | PRIMARY KEY                 |
| username  | VARCHAR(50)  | NOT NULL                    |
| birthdate | DATE         | CHECK (> '1900-01-01')      |
| password  | VARCHAR(50)  | NOT NULL                    |
| email     | VARCHAR(250) | UNIQUE, NOT NULL            |
| created_on| TIMESTAMP    | NOT NULL                    |
| last_login| TIMESTAMP    | (nenhuma)                   |
+-----------+--------------+-----------------------------+
```

---

A query cria a tabela `account` com 7 colunas, cada uma
com seu tipo de dado e restrições específicas. `user_id`
é gerado automaticamente pelo banco a cada novo registro.
`email` é obrigatório e único — dois usuários não podem
compartilhar o mesmo. `last_login` é a única coluna sem
restrições, pois um usuário recém-criado ainda não fez
login. As restrições garantem qualidade dos dados desde
a criação da tabela, sem depender da aplicação.

---

### O que cada parte faz

- `CREATE TABLE account (...)` — cria uma nova tabela
  chamada `account` no banco de dados. Se a tabela já
  existir, o comando retorna erro.

- `user_id SERIAL PRIMARY KEY` — duas coisas juntas:
  - `SERIAL` — tipo que gera um número inteiro
    automaticamente e incrementa a cada novo registro
    inserido (1, 2, 3...). Não é necessário informar
    esse valor no `INSERT`.
  - `PRIMARY KEY` — define esta coluna como chave
    primária: valor único por linha e nunca nulo.
    Cada tabela pode ter apenas 1 chave primária.

- `username VARCHAR(50) NOT NULL` — texto de até 50
  caracteres. `NOT NULL` impede que o campo seja
  deixado em branco no momento do `INSERT`.

- `birthdate DATE CHECK (birthdate > '1900-01-01')`
  — coluna do tipo data. `CHECK` é uma restrição que
  valida o valor antes de aceitar o registro: só aceita
  datas posteriores a 01/01/1900. Valores que não
  passarem na verificação são rejeitados com erro.
  Esta coluna não tem `NOT NULL` — data de nascimento
  é opcional.

- `password VARCHAR(50) NOT NULL` — texto de até 50
  caracteres, obrigatório. Na prática real, senhas
  nunca são armazenadas como texto puro — passam por
  uma função de hash antes de serem salvas.

- `email VARCHAR(250) UNIQUE NOT NULL` — texto de até
  250 caracteres, obrigatório e único. `UNIQUE` garante
  que nenhum outro registro na tabela tenha o mesmo
  valor nessa coluna — o banco retorna erro se alguém
  tentar cadastrar um e-mail já existente.

- `created_on TIMESTAMP NOT NULL` — armazena data e
  hora da criação do registro. Obrigatório — todo
  usuário deve ter uma data de cadastro.

- `last_login TIMESTAMP` — armazena data e hora do
  último acesso. Sem `NOT NULL` — um usuário recém
  cadastrado ainda não fez login, então o valor
  inicial é `NULL` (vazio).