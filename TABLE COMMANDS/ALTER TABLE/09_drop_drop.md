## ALTER TABLE — Como remover múltiplas colunas de uma tabela?

**Tabela utilizada:** `product`
```
product (antes do DROP COLUMN)
+------------+------------------+--------+-------+
| product_id | name             | price  | stock |
| active     | description      |        |       |
+------------+------------------+--------+-------+
|          1 | Camiseta Básica  |  49.90 |   100 |
|            | TRUE             | algodão|       |
|          2 | Tênis Esportivo  | 199.90 |    50 |
|            | TRUE             | couro  |       |
|          3 | Boné Aba Curva   |  39.90 |     0 |
|            | FALSE            | NULL   |       |
+------------+------------------+--------+-------+
```

```
product (antes do DROP COLUMN — formato correto)
+------------+-----------------+--------+-------+--------+-------------+
| product_id | name            | price  | stock | active | description |
+------------+-----------------+--------+-------+--------+-------------+
|          1 | Camiseta Básica |  49.90 |   100 | TRUE   | algodão     |
|          2 | Tênis Esportivo | 199.90 |    50 | TRUE   | couro       |
|          3 | Boné Aba Curva  |  39.90 |     0 | FALSE  | NULL        |
+------------+-----------------+--------+-------+--------+-------------+
```


### Query
```sql
ALTER TABLE product
DROP COLUMN active,
DROP COLUMN description;
```



### Resultado
```
product (depois do DROP COLUMN)
+------------+-----------------+--------+-------+
| product_id | name            | price  | stock |
+------------+-----------------+--------+-------+
|          1 | Camiseta Básica |  49.90 |   100 |
|          2 | Tênis Esportivo | 199.90 |    50 |
|          3 | Boné Aba Curva  |  39.90 |     0 |
+------------+-----------------+--------+-------+
```

---

A query removeu permanentemente as colunas `active`
e `description` da tabela `product` em um único
comando. Os dados das colunas removidas são perdidos
para sempre. As colunas restantes e seus dados
permanecem intactos.



### O que cada parte faz

- `ALTER TABLE product` — seleciona a tabela
  cuja estrutura será modificada.

- `DROP COLUMN active` — remove permanentemente
  a coluna `active` e todos os seus dados.

- `DROP COLUMN description` — **novo:** é possível
  encadear múltiplos `DROP COLUMN` em um único
  `ALTER TABLE`, separando cada um por vírgula.
  Cada `DROP COLUMN` remove uma coluna diferente
  na mesma operação.



### Um DROP por vez vs múltiplos em um comando
```sql
-- Um DROP por vez (menos eficiente —
-- 2 operações separadas no banco):
ALTER TABLE product DROP COLUMN active;
ALTER TABLE product DROP COLUMN description;

-- Múltiplos DROPs em um único comando
-- (recomendado):
ALTER TABLE product
DROP COLUMN active,
DROP COLUMN description;
```

---

### Cuidado porque — DROP COLUMN é irreversível
```
Antes de remover qualquer coluna, sempre:

1. Confirme quais dados serão perdidos:
   SELECT active, description
   FROM product;

2. Faça backup se necessário:
   CREATE TABLE product_backup
   AS SELECT * FROM product;

3. Verifique dependências:
   SELECT * FROM information_schema.columns
   WHERE table_name = 'product'
   AND column_name IN ('active', 'description');

→ Só então execute o DROP COLUMN.
```