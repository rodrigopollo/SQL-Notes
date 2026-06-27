## TO_NUMBER() — Como transformar um texto em um número real?

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
    amount,
    TO_NUMBER('30.00', '99.99') AS as_number
FROM payments
WHERE amount >= TO_NUMBER('30.00', '99.99');
```

### Resultado
```
+------------+--------+-----------+
| payment_id | amount | as_number |
+------------+--------+-----------+
|          3 |  30.00 |     30.00 |
|          4 |  40.00 |     30.00 |
|          5 |  50.00 |     30.00 |
+------------+--------+-----------+
```

---

A query filtra os pagamentos com `amount` igual ou superior a `30.00`, usando `TO_NUMBER()` para converter
o texto `'30.00'` em número antes da comparação. Os `payment_id` 1 (R$ 10,00) e 2 (R$ 20,00) ficaram de 
fora por estarem abaixo do limite. A coluna `as_number` exibe o mesmo valor `30.00` em todas as linhas pois
é um valor fixo definido na query, não uma coluna da tabela. Na prática, `TO_NUMBER()` é mais usado quando
valores numéricos chegam de fontes externas gravados como texto — como arquivos CSV, formulários ou 
integrações com outros sistemas — e precisam ser convertidos antes de qualquer operação no banco.


### O que cada parte faz

- `payment_id, amount` — colunas trazidas diretamente da tabela, sem nenhuma transformação.
- `TO_NUMBER('30.00', '99.99') AS as_number` — **novo:** `TO_NUMBER()` converte um texto que parece um 
número em um número real, que o banco consegue usar em cálculos e comparações. No PostgreSQL, exige 
obrigatoriamente dois argumentos:
  - `'30.00'` — o texto a ser convertido. Para o banco, antes da conversão, é apenas uma sequência de 
  caracteres sem valor numérico.
  - `'99.99'` — a máscara que ensina ao banco como interpretar o texto. Cada `9` representa um dígito 
  esperado; o `.` representa o separador decimal. Para números maiores, a máscara seria proporcional:
  `'999.99'` para até 3 dígitos inteiros, `'9999.99'` para 4, e assim por diante.
- `WHERE amount >= TO_NUMBER('30.00', '99.99')` — uso prático: o texto `'30.00'` é convertido em número
antes de ser comparado com a coluna `amount`. Sem `TO_NUMBER()`, o banco estaria comparando um número com
um texto — o que geraria erro ou resultados incorretos.
- `FROM payments` — define a tabela de origem dos dados.


### Por que isso importa?
```
Texto de entrada  →  '30.00'          (string: o banco não sabe que é um número)
Após TO_NUMBER()  →   30.00           (numeric: agora o banco entende como número)
```

Depois da conversão, o valor passa a ser um número de verdade — o banco consegue:

- Comparar com outras colunas numéricas: `amount >= TO_NUMBER('30.00', '99.99')`
- Usar em cálculos: `TO_NUMBER('30.00', '99.99') * 1.1`
- Somar com outros valores: `amount + TO_NUMBER('30.00', '99.99')`





