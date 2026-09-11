## DROP TABLE — Como remover uma tabela apenas se ela existir?

**Tabela utilizada:** `product_backup`
```
product_backup
+------------+-----------------+--------+-------+
| product_id | name            | price  | stock |
+------------+-----------------+--------+-------+
|          1 | Camiseta Básica |  49.90 |   100 |
|          2 | Tênis Esportivo | 199.90 |    50 |
|          3 | Boné Aba Curva  |  39.90 |     0 |
+------------+-----------------+--------+-------+
```


### Query
```sql
DROP TABLE IF EXISTS product_backup;
```


### Resultado
```
-- Se a tabela product_backup EXISTIR:
→ tabela removida com sucesso

-- Se a tabela product_backup NÃO EXISTIR:
→ sem erro, apenas um aviso:
NOTICE: table "product_backup" does not
exist, skipping
```

---

`DROP TABLE IF EXISTS` remove a tabela inteira —
estrutura e dados — apenas se ela existir. Sem
`IF EXISTS`, tentar remover uma tabela inexistente
interrompe o script com erro. Com `IF EXISTS`, o
banco emite apenas um aviso e continua a execução
normalmente. É muito comum em scripts de banco de
dados que precisam "limpar" e recriar tabelas do zero.



### O que cada parte faz

- `DROP TABLE` — remove permanentemente a tabela
  do banco de dados, junto com todos os seus dados,
  índices e restrições. Diferente de `DELETE`, que
  remove apenas os dados, `DROP TABLE` remove a
  estrutura inteira.

- `IF EXISTS` — instrui o banco a verificar se
  a tabela existe antes de tentar removê-la.
  Torna o comando seguro para uso em scripts
  que podem rodar mais de uma vez.

- `product_backup` — nome da tabela a ser removida.



### Com IF EXISTS vs sem IF EXISTS

```sql
-- SEM IF EXISTS → erro se tabela não existir:
DROP TABLE product_backup;

ERROR: table "product_backup" does not exist

-- COM IF EXISTS → aviso e continua:
DROP TABLE IF EXISTS product_backup;

NOTICE: table "product_backup" does not
exist, skipping
```


### Padrão comum em scripts de banco de dados

```sql
-- Padrão "drop e recria" — muito usado em
-- scripts de migração e testes:

DROP TABLE IF EXISTS product_backup;

CREATE TABLE product_backup AS
SELECT * FROM product;

-- 1ª execução → product_backup não existe
--   → IF EXISTS emite aviso, continua
--   → CREATE TABLE cria a tabela do zero

-- 2ª execução → product_backup já existe
--   → IF EXISTS remove a tabela antiga
--   → CREATE TABLE recria com dados atuais
```

---

### DROP TABLE vs DELETE vs TRUNCATE
```
DROP TABLE IF EXISTS product_backup
→ remove a estrutura inteira da tabela
→ dados, colunas, índices e constraints
  são apagados permanentemente

DELETE FROM product_backup
→ remove apenas os dados
→ a estrutura da tabela permanece intacta

TRUNCATE product_backup
→ remove todos os dados rapidamente
→ a estrutura permanece, mais rápido
  que DELETE para grandes volumes
```