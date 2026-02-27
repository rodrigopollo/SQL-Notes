# GROUP BY + COUNT() — total de transacoes por empresa

## Tabela:
| id | company | name     | sales |
|----|---------|----------|-------|
| 1  | Xerox   | Steveni  | 1.00  |
| 2  | Google  | Cheryl   | 5.00  |
| 3  | Google  | Claire   | 2.00  |
| 4  | Apple   | Cheryl   | 3.00  |
| 5  | Apple   | Steveni  | 1.00  |

## Comando SQL:
SELECT company, COUNT(sales) AS total_transacoes
FROM table_1
GROUP BY company
ORDER BY total_transacoes ASC, company ASC;

## Resultado Esperado:
| company | total_transacoes |
|---------|------------------|
| Xerox   | 1                |
| Apple   | 2                |
| Google  | 2                |

---

## Explicacao:
- `COUNT(sales)` eh uma aggregate function que conta os registros tem na coluna `sales`.
- `GROUP BY company` agrupa os registros por `company`.
- Calculo por empresa:
  - Xerox -> 1 transacao
  - Apple -> 2 transacoes
  - Google -> 2 transacoes
- `ORDER BY total_transacoes ASC, company ASC`:
  - Primeiro ordena pela quantidade em ordem crescente.
  - Em caso de empate (Apple e Google), ordena pelo nome da empresa em ordem alfabetica.

## Observacoes:
- `COUNT(coluna)` nao conta valores NULL.
- Se fosse usado `COUNT(*)`, contaria todas as linhas do grupo.
- NOTE PROFESSOR: Esse padrao eh muito comum para relatorios de volume e analise de atividade.