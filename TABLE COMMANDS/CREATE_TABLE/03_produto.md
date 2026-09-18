## CREATE TABLE — Como criar uma tabela de avaliações de produtos?

**Tabela criada:** `product_review`
```
product_review (estrutura após o CREATE TABLE)
+-------------+--------------+--------------------------------+
| coluna      | tipo         | restrições                     |
+-------------+--------------+--------------------------------+
| review_id   | SERIAL       | PRIMARY KEY                    |
| customer_id | INTEGER      | NOT NULL, FK → customer        |
| product_id  | INTEGER      | NOT NULL, FK → product         |
| rating      | INTEGER      | NOT NULL, CHECK (1 a 5)        |
| comment     | TEXT         | (nenhuma)                      |
| created_at  | TIMESTAMP    | NOT NULL, DEFAULT NOW()        |
+-------------+--------------+--------------------------------+
```



### Query
```sql
CREATE TABLE product_review (
    review_id   SERIAL      PRIMARY KEY,
    customer_id INTEGER     NOT NULL,
    product_id  INTEGER     NOT NULL,
    rating      INTEGER     NOT NULL
                CHECK (rating >= 1 AND rating <= 5),
    comment     TEXT,
    created_at  TIMESTAMP   NOT NULL DEFAULT NOW(),

    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES customer(customer_id),

    CONSTRAINT fk_product
        FOREIGN KEY (product_id)
        REFERENCES product(product_id),

    CONSTRAINT unique_review
        UNIQUE (customer_id, product_id)
);
```



### Resultado
```
product_review (pronta para receber dados)
+-----------+-------------+------------+--------+---------+------------+
| review_id | customer_id | product_id | rating | comment | created_at |
+-----------+-------------+------------+--------+---------+------------+
| (vazia)   |             |            |        |         |            |
+-----------+-------------+------------+--------+---------+------------+
```

---

A query cria a tabela `product_review` com 6 colunas.
Ela liga duas tabelas já existentes — `customer` e
`product` — através de chaves estrangeiras. O ponto
mais interessante é o `CONSTRAINT unique_review`:
ele impede que o mesmo cliente avalie o mesmo produto
mais de uma vez, combinando duas colunas como critério
de unicidade. O `rating` só aceita valores de 1 a 5
— qualquer outro valor é rejeitado pelo `CHECK`.



### O que cada parte faz

- `review_id SERIAL PRIMARY KEY` — identificador
  gerado automaticamente a cada nova avaliação.

- `customer_id INTEGER NOT NULL` — id do cliente
  que fez a avaliação. Obrigatório — uma avaliação
  sem cliente não faz sentido.

- `product_id INTEGER NOT NULL` — id do produto
  avaliado. Obrigatório pelo mesmo motivo.

- `rating INTEGER NOT NULL CHECK (rating >= 1
  AND rating <= 5)` — nota da avaliação. O `CHECK`
  usa duas condições com `AND` para garantir que
  o valor esteja entre 1 e 5. Notas como 0, 6 ou
  negativas são rejeitadas automaticamente.

- `comment TEXT` — comentário opcional do cliente.
  `TEXT` sem limite de caracteres. Sem `NOT NULL`
  pois o cliente pode dar uma nota sem escrever
  nada.

- `created_at TIMESTAMP NOT NULL DEFAULT NOW()`
  — data e hora da avaliação, preenchida
  automaticamente pelo banco no `INSERT`.

- `CONSTRAINT fk_customer FOREIGN KEY
  (customer_id) REFERENCES customer(customer_id)`
  — garante que só é possível avaliar com um
  `customer_id` que exista na tabela `customer`.

- `CONSTRAINT fk_product FOREIGN KEY (product_id)
  REFERENCES product(product_id)` — garante que
  só é possível avaliar um `product_id` que exista
  na tabela `product`.

- `CONSTRAINT unique_review UNIQUE
  (customer_id, product_id)` — **novo:** `UNIQUE`
  aplicado sobre **duas colunas juntas**. Isso
  significa que a combinação `customer_id +
  product_id` deve ser única — o mesmo cliente
  não pode avaliar o mesmo produto duas vezes.
  Um cliente pode avaliar produtos diferentes,
  e produtos diferentes podem ser avaliados pelo
  mesmo cliente — só não podem se repetir juntos.

---

### Como um INSERT nessa tabela ficaria
```sql
INSERT INTO product_review (
    customer_id,
    product_id,
    rating,
    comment
)
VALUES
    (1, 1, 5, 'Produto excelente!'),
    (2, 1, 4, 'Muito bom, recomendo.'),
    (1, 2, 3, NULL);
```

```
+-----------+-------------+------------+--------+----------------------+---------------------+
| review_id | customer_id | product_id | rating | comment              | created_at          |
+-----------+-------------+------------+--------+----------------------+---------------------+
|         1 |           1 |          1 |      5 | Produto excelente!   | 2025-09-29 14:37:52 |
|         2 |           2 |          1 |      4 | Muito bom, recomendo.| 2025-09-29 14:37:52 |
|         3 |           1 |          2 |      3 | NULL                 | 2025-09-29 14:37:52 |
+-----------+-------------+------------+--------+----------------------+---------------------+
```

---

### O que o UNIQUE duplo protege
```sql
-- Cliente 1 já avaliou o produto 1.
-- Tentar avaliar de novo:
INSERT INTO product_review
    (customer_id, product_id, rating)
VALUES (1, 1, 2);

ERROR: duplicate key value violates unique
constraint "unique_review"
DETAIL: Key (customer_id, product_id)=
(1, 1) already exists.
```