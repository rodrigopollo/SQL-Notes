# GROUP BY + MIN() — menor valor de venda por empresa

## Tabela: 
| id | company | name     | sales |
|----|---------|----------|-------|
| 1  | Xerox   | Steveni  | 1.00  |
| 2  | Google  | Cheryl   | 5.00  |
| 3  | Google  | Claire   | 2.00  |
| 4  | Apple   | Cheryl   | 3.00  |
| 5  | Apple   | Steveni  | 1.00  |

## Comando SQL:
SELECT company, MIN(sales) AS menor_venda
FROM table_1
GROUP BY company
ORDER BY menor_venda ASC, company ASC;

## Resultado Esperado:
| company | menor_venda |
|---------|-------------|
| Xerox   | 1.00        |
| Apple   | 1.00        |
| Google  | 2.00        |

---

## Explicacao:
- `MIN(sales)` eh uma aggregate function que retorna o menor valor dentro de cada grupo.
- `GROUP BY company` divide os registros por empresa.
- Primeiro separa as vendas por empresa, depois encontra o menor valor dentro de cada grupo.
- Calculo por empresa:
  - Xerox -> 1.00
  - Apple -> 1.00 (entre 3.00 e 1.00)
  - Google -> 2.00 (entre 5.00 e 2.00)
- `ORDER BY menor_venda ASC, company ASC`:
  - Primeiro ordena em ordem crescente.
  - Se empatar (Xerox e Apple), ordena em ordem alfabetica os resultados empatados.

## Observacoes:
- `MIN()` ignora valores NULL.
- NOTE PROFESSOR: Esse padrao eh comum para identificar valores minimos por categoria.