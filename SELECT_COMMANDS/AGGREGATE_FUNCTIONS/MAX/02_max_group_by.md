# GROUP BY + MAX() — maior valor de venda por empresa

## Tabela:
| id | company | name     | sales |
|----|---------|----------|-------|
| 1  | Xerox   | Steveni  | 1.00  |
| 2  | Google  | Cheryl   | 5.00  |
| 3  | Google  | Claire   | 2.00  |
| 4  | Apple   | Cheryl   | 3.00  |
| 5  | Apple   | Steveni  | 1.00  |

## Comando SQL:
SELECT company, MAX(sales) AS maior_venda
FROM table_1
GROUP BY company
ORDER BY maior_venda ASC, company ASC;

## Resultado Esperado:
| company | maior_venda |
|---------|-------------|
| Xerox   | 1.00        |
| Apple   | 3.00        |
| Google  | 5.00        |

---

## Explicacao:
- `MAX(sales)` eh uma aggregate function que retorna o maior valor dentro de cada grupo.
- `GROUP BY company` divide os registros por empresa.
- O banco primeiro separa as vendas por empresa e depois encontra o maior valor dentro de cada grupo.
- Calculo por empresa:
  - Xerox -> 1.00
  - Apple -> 3.00 (entre 3.00 e 1.00)
  - Google -> 5.00 (entre 5.00 e 2.00)
- `ORDER BY maior_venda ASC, company ASC`:
  - Primeiro ordena pelo maior valor em ordem crescente.
  - Em caso de empate, ordenaria pelo nome da empresa em ordem alfabetica.

## Observacoes:
- `MAX()` ignora valores NULL.
