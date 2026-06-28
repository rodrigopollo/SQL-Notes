## TO_NUMBER() — Qual seria o novo valor de cada pagamento após um acréscimo de R$ 5,00?

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
SELECT
    payment_id,
    amount                            AS valor_original,
    amount + TO_NUMBER('5.00', '9.99') AS valor_com_acrescimo
FROM payments;
```

### Resultado
```
+------------+----------------+---------------------+
| payment_id | valor_original | valor_com_acrescimo |
+------------+----------------+---------------------+
|          1 |          10.00 |               15.00 |
|          2 |          20.00 |               25.00 |
|          3 |          30.00 |               35.00 |
|          4 |          40.00 |               45.00 |
|          5 |          50.00 |               55.00 |
+------------+----------------+---------------------+
```

---

A query projeta o novo valor de cada pagamento após somar R$ 5,00, sem alterar nada na tabela — o resultado
existe apenas na exibição. O acréscimo `'5.00'` chega como texto (simulando um valor vindo de fora do banco,
como um formulário ou arquivo externo) e é convertido por `TO_NUMBER()` antes de participar do cálculo. 
Na prática, esse padrão é comum em pipelines de dados onde valores numéricos são recebidos como texto de 
fontes externas e precisam ser convertidos antes de qualquer operação.


### O que cada parte faz

- `payment_id` — coluna trazida diretamente da tabela, sem nenhuma transformação.
- `amount AS valor_original` — exibe o valor original de cada pagamento com o apelido `valor_original`
para deixar o resultado mais legível na comparação.
- `amount + TO_NUMBER('5.00', '9.99') AS valor_com_acrescimo` — aqui está o uso prático: o texto `'5.00'`
é convertido em número real por `TO_NUMBER()` e somado diretamente à coluna `amount`. Sem a conversão, 
o banco não conseguiria fazer a soma, pois não é possível somar um número com um texto. A máscara `'9.99'`
define que o texto tem 1 dígito inteiro e 2 decimais.
- `FROM payments` — define a tabela de origem dos dados.



