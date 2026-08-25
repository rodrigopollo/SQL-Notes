## ALTER TABLE — Como renomear uma tabela?

**Tabela utilizada:** `information`
```
information (antes do RENAME)
+----+-------------------+
| id | description       |
+----+-------------------+
|  1 | dados gerais      |
|  2 | dados adicionais  |
+----+-------------------+
```

### Query
```sql
ALTER TABLE information
RENAME TO new_info;
```


### Resultado
```
-- Antes:
SELECT * FROM information;  → funciona ✓

-- Depois:
SELECT * FROM information;  → erro ✗
SELECT * FROM new_info;     → funciona ✓
```

---

A query renomeou a tabela `information` para
`new_info`. Os dados e a estrutura da tabela
permanecem intactos — apenas o nome muda.
A partir deste momento, qualquer query que
referencie o nome antigo (`information`)
retornará erro, pois o banco não reconhece
mais esse nome.


### O que cada parte faz

- `ALTER TABLE information` — seleciona a tabela
  que será modificada. `ALTER TABLE` é o comando
  usado para modificar a **estrutura** de uma
  tabela já existente — diferente de `UPDATE`,
  que modifica os **dados**.

- `RENAME TO new_info` — define o novo nome da
  tabela. O nome antigo deixa de existir
  imediatamente após a execução.

---

### Atenção ao renomear tabelas
```
Após o RENAME, tudo que referencia o nome
antigo precisa ser atualizado:

  ✗ queries com FROM information
  ✗ views que usam information
  ✗ foreign keys apontando para information
  ✗ código da aplicação que usa information

→ Todos precisam ser atualizados para new_info
```