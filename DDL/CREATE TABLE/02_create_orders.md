## CREATE TABLE — Como criar uma tabela de pedidos com chave estrangeira?


### Query

```sql
CREATE TABLE orders (
    order_id    SERIAL          PRIMARY KEY,
    customer_id INT             NOT NULL,
    amount      NUMERIC(10, 2)  NOT NULL CHECK (amount > 0),
    status      VARCHAR(20)     NOT NULL DEFAULT 'pending',
    created_at  TIMESTAMP       NOT NULL DEFAULT NOW(),

    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES customer(customer_id)
);
```



### Resultado — estrutura da tabela criada

```
+-------------+--------------+----------------------------------+
| coluna      | tipo         | restrições                       |
+-------------+--------------+----------------------------------+
| order_id    | SERIAL       | PRIMARY KEY                      |
| customer_id | INT          | NOT NULL, FOREIGN KEY → customer |
| amount      | NUMERIC(10,2)| NOT NULL, CHECK (> 0)            |
| status      | VARCHAR(20)  | NOT NULL, DEFAULT 'pending'      |
| created_at  | TIMESTAMP    | NOT NULL, DEFAULT NOW()          |
+-------------+--------------+----------------------------------+
```

---


A query cria a tabela `orders` com 5 colunas. `order_id`
é gerado automaticamente. `customer_id` é uma chave
estrangeira — só aceita valores que existam na tabela
`customer`, impedindo pedidos vinculados a clientes
inexistentes. `amount` tem validação de valor positivo.
`status` e `created_at` têm valores padrão automáticos,
então um `INSERT` simples já preenche essas colunas
sem precisar informá-las.



### O que cada parte faz

- `order_id SERIAL PRIMARY KEY` — número gerado
  automaticamente pelo banco a cada novo pedido
  inserido. Valor único e nunca nulo.

- `customer_id INT NOT NULL` — número inteiro
  obrigatório que identifica qual cliente fez o
  pedido. O tipo `INT` é usado aqui porque o valor
  vem da coluna `user_id` de outra tabela, e não
  precisa ser gerado automaticamente.

- `amount NUMERIC(10, 2) NOT NULL CHECK (amount > 0)`
  — **novo:** `NUMERIC(10, 2)` é o tipo ideal para
  valores monetários. O primeiro número (10) define
  o total de dígitos permitidos; o segundo (2) define
  quantos dígitos são decimais — por exemplo:
  `99999999.99`. `CHECK (amount > 0)` garante que
  nenhum pedido seja inserido com valor zero ou
  negativo.

- `status VARCHAR(20) NOT NULL DEFAULT 'pending'`
  — **novo:** `DEFAULT` define o valor que o banco
  usa automaticamente quando a coluna não é informada
  no `INSERT`. Aqui, todo pedido começa com o status
  `'pending'` (pendente) sem precisar ser declarado
  explicitamente.

- `created_at TIMESTAMP NOT NULL DEFAULT NOW()`
  — data e hora de criação do pedido. `DEFAULT NOW()`
  faz o banco preencher automaticamente com a data e
  hora exata do momento do `INSERT`, sem nenhuma
  intervenção manual.

- `CONSTRAINT fk_customer FOREIGN KEY (customer_id)
  REFERENCES customer(customer_id)` — **novo:**
  define uma chave estrangeira (`FOREIGN KEY`) com
  nome explícito (`fk_customer`). Isso significa que
  o valor de `customer_id` em `orders` precisa existir
  na coluna `customer_id` da tabela `customer`. Se
  tentar inserir um pedido com um `customer_id`
  inexistente, o banco rejeita com erro. O nome
  explícito (`CONSTRAINT fk_customer`) facilita
  identificar e remover a restrição no futuro se
  necessário.



### Como um INSERT nessa tabela ficaria

```sql
-- Informando só o necessário:
INSERT INTO orders (customer_id, amount)
VALUES (1, 99.90);

-- O banco preenche automaticamente:
-- status     → 'pending'
-- created_at → data e hora atual
-- order_id   → próximo número da sequência
```