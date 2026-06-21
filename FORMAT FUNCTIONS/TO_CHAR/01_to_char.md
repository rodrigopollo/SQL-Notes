## TO_CHAR() — Como exibir a data de cada pagamento em um formato de texto legível?

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
    payment_date,
    TO_CHAR(payment_date, 'DD/MM/YYYY') AS data_formatada
FROM payments;
```

### Resultado
```
+------------+---------------------+----------------+
| payment_id | payment_date        | data_formatada |
+------------+---------------------+----------------+
|          1 | 2025-01-15 10:30:00 | 15/01/2025     |
|          2 | 2025-03-22 18:45:00 | 22/03/2025     |
|          3 | 2025-07-05 09:00:00 | 05/07/2025     |
|          4 | 2025-09-10 14:20:00 | 10/09/2025     |
|          5 | 2026-02-01 12:10:00 | 01/02/2026     |
+------------+---------------------+----------------+
```

---

A query exibe a mesma data de cada pagamento, mas reformatada do padrão técnico `YYYY-MM-DD HH:MI:SS`
(usado internamente pelo banco) para o formato `DD/MM/YYYY`, mais comum em relatórios e telas voltadas
ao usuário final brasileiro. `TO_CHAR` é amplamente usado quando os dados do banco precisam ser exibidos
em interfaces, exportados para planilhas ou enviados em relatórios, onde a legibilidade importa mais do
que a estrutura interna da data.


### O que cada parte faz

- `payment_id, payment_date` — colunas trazidas diretamente da tabela, sem nenhuma transformação.
- `TO_CHAR(payment_date, 'DD/MM/YYYY') AS data_formatada` — **novo:** `TO_CHAR()` converte um valor 
de data, hora ou número em **texto** (`string`), seguindo um padrão de formatação definido no segundo 
argumento. Diferente de `EXTRACT`, que retorna um número, `TO_CHAR` retorna sempre texto — o que é útil 
para exibição em relatórios, mas não deve ser usado em cálculos ou comparações de datas.
- `'DD/MM/YYYY'` — a máscara de formatação. Cada letra representa uma parte da data:
  - `DD` → dia com 2 dígitos (01–31)
  - `MM` → mês com 2 dígitos (01–12)
  - `YYYY` → ano com 4 dígitos
  
  A máscara pode ser combinada de outras formas, como `'YYYY-MM-DD'`, `'DD "de" Month "de" YYYY'`, ou 
incluir hora com `HH24:MI:SS`.
- `FROM payments` — define a tabela de origem dos dados.

> **Atenção:** o resultado de `TO_CHAR` é sempre texto, mesmo que pareça uma data. Isso significa que
`data_formatada > '01/01/2025'` faria uma comparação de texto (ordem alfabética), não de data — o que 
pode gerar resultados incorretos. Para cálculos ou comparações, sempre use a coluna de data original 
(`payment_date`), não o resultado de `TO_CHAR`.
