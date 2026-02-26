# GROUP BY + SUM() — total gasto por cada pessoa

## Tabela: 
| id | company | name     | sales |
|----|---------|----------|-------|
| 1  | Xerox   | Steveni  | 1.00  |
| 2  | Google  | Cheryl   | 5.00  |
| 3  | Google  | Claire   | 2.00  |
| 4  | Apple   | Cheryl   | 3.00  |
| 5  | Apple   | Steveni  | 1.00  |

## Comando SQL:
SELECT name, SUM(sales) AS soma_total
FROM table_1
GROUP BY name
ORDER BY soma_total ASC, name ASC;

## Resultado Esperado:
| name     | soma_total |
|----------|------------|
| Claire   | 2.00       |
| Steveni  | 2.00       |
| Cheryl   | 8.00       |

## Explicaçao:
- `SUM(sales)` eh um **aggregate function** que soma os valores da coluna `sales`.
- `GROUP BY name` agrupa os registros pelo nome da pessoa.
- O banco separa os dados por pessoa e soma os valores gastos por cada um.
- Calculo por pessoa:
  - **Steveni** → 1.00 + 1.00 = 2.00
  - **Cheryl** → 5.00 + 3.00 = 8.00
  - **Claire** → 2.00
- `ORDER BY soma_total ASC, name ASC`:
  - Primeiro ordena pelo total em ordem crescente.
  - Se empatar (Steveni e Claire com 2.00), ordena pelo nome em ordem alfabetica.

## Observaçoes:
- Toda coluna no `SELECT` que não for uma função de agregação (como SUM, COUNT, AVG, etc.) 
deve obrigatoriamente aparecer na cláusula `GROUP BY`
- `AS soma_total` cria um alias (apelido) pro calculo.
- NOTE PROFESSOR: Esse padrao eh muito comum em relatorios financeiros e analises de gastos.