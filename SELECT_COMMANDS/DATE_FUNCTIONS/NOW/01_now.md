## NOW() — Qual é a data e hora atuais do sistema?

**Tabela utilizada:** `payments`

```
+------------+---------------------+--------+
| payment_id | payment_date        | amount |
+------------+---------------------+--------+
|          1 | 2025-01-15 10:30:00 |  10.00 |
|          2 | 2025-03-22 18:45:00 |  20.00 |
|          3 | 2025-07-05 09:00:00 |  30.00 |
|          4 | 2025-09-10 14:20:00 |  40.00 |
|          5 | 2026-02-01 12:10:00 |  50.00 |
+------------+---------------------+--------+
```

### Query
```sql
SELECT NOW() AS data_hora_atual;
```


### Resultado
```
+-------------------------+
| data_hora_atual         |
+-------------------------+
| 2025-09-29 14:37:52-03  |
+-------------------------+
```


### O que cada parte faz

- `NOW()` — **novo:** é uma função do PostgreSQL que retorna a data e hora exatas do momento em que
a query é executada, incluindo fuso horário. O resultado muda a cada execução — não é um valor fixo
armazenado em nenhuma tabela.
- `AS data_hora_atual` — apelido para exibir o resultado com um nome legível na coluna de saída.
- **Sem `FROM`:** ao contrário de todas as queries anteriores, esta não consulta nenhuma tabela. 
No PostgreSQL, `SELECT` pode ser usado sozinho quando o resultado vem de uma função ou valor fixo que
não depende de dados armazenados. `NOW()` é gerado diretamente pelo sistema, então nenhuma tabela precisa
ser acessada.



