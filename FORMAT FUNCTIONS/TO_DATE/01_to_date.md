## TO_DATE() — Como transformar um texto em uma data real?

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
    TO_DATE('29-09-2025', 'DD-MM-YYYY') AS as_date;
```

### Resultado
```
+------------+
| as_date    |
+------------+
| 2025-09-29 |
+------------+
```

---

`TO_DATE()` é especialmente útil quando os dados chegam de fontes externas — como planilhas, formulários
ou arquivos CSV — onde as datas são gravadas como texto em formatos variados (`'29/09/2025'`, 
`'Sep 29 2025'`, `'29-09-2025'` etc). Antes de armazenar ou comparar esses valores no banco, é necessário
convertê-los para o tipo `date` com `TO_DATE()`, garantindo que o banco consiga tratá-los como datas de
verdade.


### O que cada parte faz

- `TO_DATE()` — **novo:** função que converte um texto que parece uma data em um valor de data real, que
o banco consegue entender, armazenar e usar em cálculos. Recebe dois argumentos:
  - `'29-09-2025'` — o texto a ser convertido. Para o banco, antes da conversão, isso é apenas uma sequênci
  a de caracteres — letras e números juntos, sem nenhum significado especial.
  - `'DD-MM-YYYY'` — a máscara que ensina ao banco como interpretar o texto: `DD` = dia, `MM` = mês, 
  `YYYY` = ano. A máscara precisa bater exatamente com o formato do texto passado — se o texto fosse 
  `'2025/09/29'`, a máscara teria que ser `'YYYY/MM/DD'`.
- `AS as_date` — apelido para nomear a coluna de saída.
- **Sem `FROM`:** o resultado vem diretamente dos argumentos passados à função, sem precisar consultar
nenhuma tabela.


### Por que isso importa?

```
Texto de entrada  →  '29-09-2025'         (string: o banco não sabe que é uma data)
Após TO_DATE()   →   2025-09-29           (date: agora o banco entende como data)
```

Depois da conversão, o valor passa a ser uma data de verdade — o banco consegue:

- Somar ou subtrair dias: `TO_DATE('29-09-2025', 'DD-MM-YYYY') + INTERVAL '7 days'`
- Comparar com outras datas: `TO_DATE('29-09-2025', 'DD-MM-YYYY') > payment_date`
- Extrair partes: `EXTRACT(MONTH FROM TO_DATE('29-09-2025', 'DD-MM-YYYY'))`

Nada disso seria possível com o texto `'29-09-2025'` puro, pois para o banco ele é apenas uma sequência de 
caracteres, sem estrutura de data.



