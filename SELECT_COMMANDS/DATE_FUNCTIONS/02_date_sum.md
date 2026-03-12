# DATE() + GROUP BY + SUM() — lucro diario por empresa

## Tabela: 
| company | name   | payment_date        | amount |
|---------|--------|---------------------|--------|
| Oppo    | Steven | 2025-09-07 08:15:00 | 10.00  |
| Xioami  | David  | 2025-02-05 14:45:00 | 20.00  |
| Huwai   | Claire | 2025-07-23 09:30:00 | 15.00  |
| Apple   | Andew  | 2025-05-30 23:55:00 | 12.00  |
| Apple   | Zach   | 2025-06-01 10:15:00 | 18.00  |
| Oppo    | Steven | 2025-09-07 21:40:00 | 30.00  |
| Huwai   | Claire | 2025-07-23 22:05:00 | 25.00  |

## Comando SQL:
SELECT
   company,
   DATE(payment_date) AS payment_day,
   SUM(amount) AS valor_total
FROM table_1
GROUP BY
   company,
   DATE(payment_date)
ORDER BY
   company ASC,
   payment_day ASC,
   valor_total ASC;

## Resultado Esperado:
| company | payment_day | valor_total |
|---------|-------------|-------------|
| Apple   | 2025-05-30  | 12.00       |
| Apple   | 2025-06-01  | 18.00       |
| Huwai   | 2025-07-23  | 40.00       |
| Oppo    | 2025-09-07  | 40.00       |
| Xioami  | 2025-02-05  | 20.00       |

---

## Explicacao
- `DATE(payment_date)` extrai so a data do campo datetime, removendo o horario.
- `SUM(amount)` soma todos os valores da coluna `amount`.
- `GROUP BY company, DATE(payment_date)` cria grupos usando empresa e data.
- Isso permite calcular o lucro total por empresa em cada dia.

Calculo dos grupos:
- Apple 2025-05-30 -> 12.00
- Apple 2025-06-01 -> 18.00
- Huwai 2025-07-23 -> 15.00 + 25.00 = 40.00
- Oppo 2025-09-07 -> 10.00 + 30.00 = 40.00
- Xioami 2025-02-05 -> 20.00

- `ORDER BY company ASC, payment_day ASC, valor_total ASC`
  - primeiro ordena pela empresa
  - depois pela data
  - depois pelo valor total

## Observacoes
- `DATE()` usamos principalmente quando queremos agrupar informaçoes(dados) por dia.
- NOTE PROFESSOR: Sem `DATE()`, cada horario diferente seria tratado como um registro separado.
- NOTE PROFESSOR: Esse padrao eh comum em analises de vendas, faturamento e relatorios diarios.