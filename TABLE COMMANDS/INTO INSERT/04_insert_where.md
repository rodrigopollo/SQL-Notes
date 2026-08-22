## INSERT INTO + SELECT — Como copiar dados de uma tabela para outra?

**Tabelas utilizadas:** `account`, `account_backup`
```
account
+---------+----------+----------+---------------------+
| user_id | username | password | created_on          |
+---------+----------+----------+---------------------+
|       1 | Jose     | 12345    | 2025-01-10 09:00:00 |
|       2 | Maria    | abcde    | 2025-03-22 14:00:00 |
|       3 | Carlos   | qwerty   | 2025-07-05 11:00:00 |
+---------+----------+----------+---------------------+

account_backup (antes do INSERT)
+---------+----------+----------+---------------------+
| user_id | username | password | created_on          |
+---------+----------+----------+---------------------+
| (vazia) |          |          |                     |
+---------+----------+----------+---------------------+
```


### Query
```sql
INSERT INTO account_backup (
    user_id,
    username,
    password,
    created_on
)
SELECT
    user_id,
    username,
    password,
    created_on
FROM account
WHERE
    created_on < '2025-06-01';
```



### Resultado — linhas inseridas em account_backup
```
+---------+----------+----------+---------------------+
| user_id | username | password | created_on          |
+---------+----------+----------+---------------------+
|       1 | Jose     | 12345    | 2025-01-10 09:00:00 |
|       2 | Maria    | abcde    | 2025-03-22 14:00:00 |
+---------+----------+----------+---------------------+
```

---

A query copiou 2 registros de `account` para
`account_backup` — apenas os usuários criados
antes de junho de 2025. Carlos não foi copiado
pois seu `created_on` é posterior ao filtro.
Nenhum valor foi digitado manualmente no `VALUES`
— os dados vieram direto do `SELECT`.



### O que cada parte faz

- `INSERT INTO account_backup (...)` — seleciona
  a tabela de destino e as colunas que receberão
  os dados.

- `SELECT user_id, username, password, created_on
  FROM account` — **novo:** em vez de `VALUES`,
  o `INSERT` usa um `SELECT` como fonte de dados.
  Tudo que o `SELECT` retornar será inserido na
  tabela de destino. A ordem das colunas do
  `SELECT` deve bater com a ordem das colunas
  declaradas no `INSERT INTO`.

- `WHERE created_on < '2025-06-01'` — filtra
  quais linhas do `SELECT` serão inseridas.
  Funciona como qualquer `WHERE` normal.

---

### INSERT com VALUES vs INSERT com SELECT

```sql
-- VALUES → dados digitados manualmente:
INSERT INTO account_backup (user_id, username)
VALUES (1, 'Jose');

-- SELECT → dados vêm de outra tabela:
INSERT INTO account_backup (user_id, username)
SELECT user_id, username
FROM account
WHERE created_on < '2025-06-01';
```

`INSERT INTO ... SELECT` é muito usado na prática
para criar backups, popular tabelas de histórico,
migrar dados entre tabelas ou duplicar registros
com filtros específicos — sem precisar digitar
nenhum valor manualmente.



### Ordem de execução
```
1º → o SELECT roda e retorna as linhas filtradas:
     user_id 1 → created_on 2025-01-10 → ✓
     user_id 2 → created_on 2025-03-22 → ✓
     user_id 3 → created_on 2025-07-05 → ✗

2º → o INSERT copia essas linhas para
     account_backup na mesma ordem das colunas
     declaradas no INSERT INTO
```