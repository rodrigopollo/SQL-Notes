## CREATE TABLE — Como criar uma tabela de produtos com estoque?


### Query
```sql
CREATE TABLE product (
    product_id   SERIAL          PRIMARY KEY,
    name         VARCHAR(100)    NOT NULL,
    description  TEXT,
    price        NUMERIC(10, 2)  NOT NULL CHECK (price >= 0),
    stock        INT             NOT NULL DEFAULT 0
                                 CHECK (stock >= 0),
    category     VARCHAR(50)     NOT NULL,
    active       BOOLEAN         NOT NULL DEFAULT TRUE,
    created_at   TIMESTAMP       NOT NULL DEFAULT NOW()
);
```



### Resultado — estrutura da tabela criada
```
+------------+--------------+------------------------------+
| coluna     | tipo         | restrições                   |
+------------+--------------+------------------------------+
| product_id | SERIAL       | PRIMARY KEY                  |
| name       | VARCHAR(100) | NOT NULL                     |
| description| TEXT         | (nenhuma)                    |
| price      | NUMERIC(10,2)| NOT NULL, CHECK (>= 0)       |
| stock      | INT          | NOT NULL, DEFAULT 0,         |
|            |              | CHECK (>= 0)                 |
| category   | VARCHAR(50)  | NOT NULL                     |
| active     | BOOLEAN      | NOT NULL, DEFAULT TRUE       |
| created_at | TIMESTAMP    | NOT NULL, DEFAULT NOW()      |
+------------+--------------+------------------------------+
```

---

A query cria a tabela `product` com 8 colunas. Todo
produto nasce com estoque zero e status ativo por
padrão — dois `DEFAULT` que refletem o comportamento
real de um cadastro de produto novo. `description` é
a única coluna opcional, pois nem todo produto precisa
de descrição. Os dois `CHECK` garantem que preço e
estoque nunca sejam negativos, protegendo a integridade
dos dados independentemente da aplicação que inserir
os registros.



### O que cada parte faz

- `product_id SERIAL PRIMARY KEY` — identificador
  gerado automaticamente a cada produto inserido.
  Valor único e nunca nulo.

- `name VARCHAR(100) NOT NULL` — nome do produto,
  obrigatório, com até 100 caracteres.

- `description TEXT` — **novo:** `TEXT` é um tipo
  de texto sem limite de caracteres, diferente de
  `VARCHAR(n)` que tem tamanho máximo definido.
  Sem `NOT NULL` — descrição é opcional.

- `price NUMERIC(10, 2) NOT NULL CHECK (price >= 0)`
  — valor monetário do produto. `CHECK (price >= 0)`
  usa `>=` em vez de `>` para permitir produtos
  gratuitos (preço zero), diferente do exercício
  anterior onde `amount > 0` bloqueava o zero.

- `stock INT NOT NULL DEFAULT 0 CHECK (stock >= 0)`
  — quantidade em estoque. `DEFAULT 0` faz o banco
  iniciar o estoque em zero automaticamente quando
  não informado. `CHECK (stock >= 0)` impede que
  o estoque fique negativo — uma restrição importante
  em sistemas de controle de inventário.

- `category VARCHAR(50) NOT NULL` — categoria do
  produto (ex: `'eletronico'`, `'roupa'`),
  obrigatória.

- `active BOOLEAN NOT NULL DEFAULT TRUE` — **novo:**
  `BOOLEAN` armazena apenas dois valores possíveis:
  `TRUE` ou `FALSE`. Aqui representa se o produto
  está ativo ou foi desativado. `DEFAULT TRUE` faz
  todo produto nascer ativo sem precisar informar
  esse campo no `INSERT`. Desativar em vez de deletar
  é uma prática comum em sistemas reais — preserva
  o histórico de pedidos e relatórios.

- `created_at TIMESTAMP NOT NULL DEFAULT NOW()`
  — data e hora do cadastro do produto, preenchida
  automaticamente pelo banco no momento do `INSERT`.

---

### Como um INSERT nessa tabela ficaria

```sql
-- Informando só o necessário:
INSERT INTO product (name, price, category)
VALUES ('Camiseta Básica', 49.90, 'roupa');

-- O banco preenche automaticamente:
-- stock      → 0
-- active     → TRUE
-- created_at → data e hora atual
-- product_id → próximo número da sequência
```