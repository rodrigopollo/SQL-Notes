## UPDATE + SUBQUERY — Como aplicar desconto nos produtos com estoque zerado?

**Tabela utilizada:** `product`

```
product (antes do UPDATE)
+------------+------------------+--------+-------+
| product_id | name             | price  | stock |
+------------+------------------+--------+-------+
|          1 | Camiseta Básica  |  49.90 |   100 |
|          2 | Tênis Esportivo  | 199.90 |    50 |
|          3 | Boné Aba Curva   |  39.90 |     0 |
|          4 | Calça Jeans      | 129.90 |     0 |
+------------+------------------+--------+-------+
```


### Query
```sql
UPDATE product
SET
    price = price * 0.80
WHERE product_id IN (
    SELECT product_id
    FROM product
    WHERE stock = 0
)
RETURNING
    product_id,
    name,
    price,
    stock;
```



### Resultado
```
+------------+----------------+--------+-------+
| product_id | name           | price  | stock |
+------------+----------------+--------+-------+
|          3 | Boné Aba Curva |  31.92 |     0 |
|          4 | Calça Jeans    | 103.92 |     0 |
+------------+----------------+--------+-------+
```

---

A query aplicou 20% de desconto nos produtos com
estoque zerado — Boné e Calça Jeans. A Camiseta
e o Tênis não foram afetados pois ainda têm
estoque. `price * 0.80` mantém 80% do valor
original, equivalente a um desconto de 20%.
`RETURNING` confirmou os novos preços sem precisar
de um `SELECT` separado.



### O que cada parte faz

- `UPDATE product` — seleciona a tabela `product`
  como destino da modificação.

- `SET price = price * 0.80` — **novo:** o novo
  valor usa a própria coluna `price` no cálculo.
  Isso é possível no `SET` — o banco lê o valor
  atual da coluna e aplica a operação. `* 0.80`
  equivale a aplicar 20% de desconto:
  `49.90 * 0.80 = 39.92`.

- `WHERE product_id IN (...)` — usa o resultado
  da subquery como filtro, atualizando apenas
  os produtos cujo `product_id` esteja na lista
  retornada.

- **Subquery:**
  - `SELECT product_id FROM product` — busca ids
    na própria tabela `product`.
  - `WHERE stock = 0` — filtra apenas os produtos
    sem estoque. Inteiro sem aspas.

- `RETURNING product_id, name, price, stock` —
  retorna as colunas escolhidas já com os novos
  preços aplicados.



### Como o desconto é calculado
```
Boné Aba Curva:
  39.90 * 0.80 = 31.92  (desconto de R$ 7.98)

Calça Jeans:
  129.90 * 0.80 = 103.92  (desconto de R$ 25.98)
```



### Estado da tabela após o UPDATE
```
product (depois do UPDATE)
+------------+------------------+--------+-------+
| product_id | name             | price  | stock |
+------------+------------------+--------+-------+
|          1 | Camiseta Básica  |  49.90 |   100 |
|          2 | Tênis Esportivo  | 199.90 |    50 |
|          3 | Boné Aba Curva   |  31.92 |     0 |
|          4 | Calça Jeans      | 103.92 |     0 |
+------------+------------------+--------+-------+
```

---

### Ordem de execução
```
1º → a subquery roda e retorna os product_id
     com stock = 0:
     product_id 3 → stock 0 ✓
     product_id 4 → stock 0 ✓
     lista retornada: [3, 4]

2º → o UPDATE filtra product:
     product_id 1 → não está em [3, 4] → mantido
     product_id 2 → não está em [3, 4] → mantido
     product_id 3 → está em [3, 4] → atualizado ✓
     product_id 4 → está em [3, 4] → atualizado ✓

3º → RETURNING exibe as linhas modificadas
     com os novos preços
```