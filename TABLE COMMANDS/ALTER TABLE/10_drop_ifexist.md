## ALTER TABLE — Como remover uma coluna apenas se ela existir?

**Tabela utilizada:** `account`
```
account
+---------+----------+--------+---------------------+
| user_id | username | active | created_on          |
+---------+----------+--------+---------------------+
|       1 | Jose     | TRUE   | 2025-01-10 09:00:00 |
|       2 | Maria    | TRUE   | 2025-03-22 14:00:00 |
|       3 | Carlos   | TRUE   | 2025-07-05 11:00:00 |
+---------+----------+--------+---------------------+
```


### Query
```sql
ALTER TABLE account
DROP COLUMN IF EXISTS active;
```


### Resultado
```
-- Se a coluna active EXISTIR:
→ coluna removida com sucesso

-- Se a coluna active NÃO EXISTIR:
→ sem erro, apenas um aviso:
NOTICE: column "active" of relation
"account" does not exist, skipping
```

---

`IF EXISTS` torna o `DROP COLUMN` seguro: se a
coluna existir ela é removida normalmente; se não
existir o banco apenas emite um aviso e continua
a execução sem interromper com erro. É especialmente
útil em scripts que rodam várias vezes ou em
ambientes onde a estrutura da tabela pode variar.



### O que cada parte faz

- `ALTER TABLE account` — seleciona a tabela
  cuja estrutura será modificada.

- `DROP COLUMN IF EXISTS active` — **novo:**
  `IF EXISTS` instrui o banco a verificar se
  a coluna existe antes de tentar removê-la.
  Sem `IF EXISTS`, tentar remover uma coluna
  inexistente retorna erro e interrompe
  a execução do script inteiro.



### Com IF EXISTS vs sem IF EXISTS
```sql
-- SEM IF EXISTS → erro se coluna não existir:
ALTER TABLE account
DROP COLUMN active;

ERROR: column "active" of relation
"account" does not exist

-- COM IF EXISTS → aviso e continua:
ALTER TABLE account
DROP COLUMN IF EXISTS active;

NOTICE: column "active" of relation
"account" does not exist, skipping
```

---

### Quando usar IF EXISTS na prática
```
1. Scripts de migração que rodam em vários
   ambientes (dev, homologação, produção)
   → cada ambiente pode estar em um estado
     diferente da tabela

2. Scripts que podem ser executados mais
   de uma vez
   → na segunda execução a coluna já foi
     removida na primeira

3. Manutenção em tabelas que evoluem
   com o tempo
   → nem sempre todas as colunas existem
     em todos os ambientes
```