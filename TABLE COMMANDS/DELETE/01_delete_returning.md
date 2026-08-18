## DELETE + RETURNING — Como remover um registro e confirmar o que foi deletado?

**Tabela utilizada:** `job`
```
job (antes do DELETE)
+--------+-----------+
| job_id | job_name  |
+--------+-----------+
|    101 | Analista  |
|    102 | Engenheiro|
|    103 | Cowboy    |
+--------+-----------+
```

### Query

```sql
DELETE FROM job
WHERE
    job_name = 'Cowboy'
RETURNING *;
```


### Resultado
```
+--------+----------+
| job_id | job_name |
+--------+----------+
|    103 | Cowboy   |
+--------+----------+
```

---

A query removeu permanentemente o registro `Cowboy`
da tabela `job`. `RETURNING *` retornou todas as
colunas da linha deletada — útil para confirmar
exatamente o que foi removido sem precisar de um
`SELECT` separado. Após a execução, a linha com
`job_id 103` deixa de existir na tabela.



### O que cada parte faz

- `DELETE FROM job` — seleciona a tabela `job` como
  origem da remoção. Sem `WHERE`, **todas** as linhas
  da tabela seriam deletadas.

- `WHERE job_name = 'Cowboy'` — limita a remoção
  apenas à linha cujo `job_name` seja `'Cowboy'`.
  String entre aspas simples. É o filtro que protege
  as demais linhas de serem apagadas.

- `RETURNING *` — retorna todas as colunas da linha
  removida já com os dados que existiam antes da
  deleção. Após o `DELETE`, a linha não existe mais
  na tabela — `RETURNING` é a única forma de ver
  os dados dela sem um `SELECT` anterior.



### Estado da tabela após o DELETE
```
job (depois do DELETE)
+--------+------------+
| job_id | job_name   |
+--------+------------+
|    101 | Analista   |
|    102 | Engenheiro |
+--------+------------+
```


### Boas práticas no DELETE
```
1. Sempre use WHERE no DELETE — sem ele, todos
   os registros da tabela são removidos.

2. Teste o filtro com SELECT antes de deletar:

   SELECT * FROM job WHERE job_name = 'Cowboy';
   → confirma qual linha será afetada
   → só então rode o DELETE

3. Use RETURNING para ver o que foi removido
   → única forma de confirmar sem SELECT separado

4. DELETE é permanente — não existe "desfazer"
   a menos que esteja dentro de uma transação
   com ROLLBACK disponível.
```