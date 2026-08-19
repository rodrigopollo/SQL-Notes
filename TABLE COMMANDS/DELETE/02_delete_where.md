## DELETE + WHERE + RETURNING — Como remover todos os produtos inativos do catálogo?

**Tabela utilizada:** `product`
```
product (antes do DELETE)
+------------+------------------+--------+-------+--------+
| product_id | name             | price  | stock | active |
+------------+------------------+--------+-------+--------+
|          1 | Camiseta Básica  |  49.90 |   100 | TRUE   |
|          2 | Tênis Esportivo  | 199.90 |    50 | TRUE   |
|          3 | Boné Aba Curva   |  39.90 |     0 | FALSE  |
|          4 | Calça Jeans      | 129.90 |    75 | TRUE   |
+------------+------------------+--------+-------+--------+
```

---

### Query
```sql
DELETE FROM product
WHERE
    active = FALSE
RETURNING
    product_id,
    name,
    active;
```



### Resultado
```
+------------+----------------+--------+
| product_id | name           | active |
+------------+----------------+--------+
|          3 | Boné Aba Curva | FALSE  |
+------------+----------------+--------+
```

---

A query removeu permanentemente todos os produtos com
`active = FALSE` da tabela `product`. Neste caso apenas
o Boné Aba Curva foi afetado — era o único inativo.
`RETURNING` confirmou exatamente qual produto foi
removido. Os demais produtos com `active = TRUE`
permaneceram intactos.



### O que cada parte faz

- `DELETE FROM product` — seleciona a tabela `product`
  como origem da remoção. Sem `WHERE`, todos os
  produtos seriam deletados.

- `WHERE active = FALSE` — filtra apenas os produtos
  inativos. `FALSE` é um booleano — sem aspas. Se
  no futuro outros produtos forem desativados,
  esse mesmo comando removeria todos eles de uma vez.

- `RETURNING product_id, name, active` — retorna as
  colunas escolhidas dos registros removidos,
  confirmando o que foi deletado sem precisar de
  um `SELECT` separado.



### Estado da tabela após o DELETE
```
product (depois do DELETE)
+------------+------------------+--------+-------+--------+
| product_id | name             | price  | stock | active |
+------------+------------------+--------+-------+--------+
|          1 | Camiseta Básica  |  49.90 |   100 | TRUE   |
|          2 | Tênis Esportivo  | 199.90 |    50 | TRUE   |
|          4 | Calça Jeans      | 129.90 |    75 | TRUE   |
+------------+------------------+--------+-------+--------+
```

> Note que `product_id 3` não existe mais — e o banco
> não renumera os ids automaticamente. Isso é esperado
> e correto: o `SERIAL` nunca reutiliza valores já
> gerados, mesmo após um `DELETE`.

---

### DELETE vs UPDATE active = FALSE

```
UPDATE product               DELETE FROM product
SET active = FALSE     vs    WHERE active = FALSE
WHERE product_id = 3;

→ mantém o registro          → remove o registro
  mas o desativa               permanentemente
→ histórico preservado       → histórico perdido
→ reversível                 → irreversível
```

Na prática, desativar com `UPDATE` (active = FALSE)
é mais seguro que deletar — preserva o histórico de
pedidos e relatórios vinculados ao produto. O `DELETE`
é usado quando o registro realmente não tem mais
nenhuma utilidade no banco.