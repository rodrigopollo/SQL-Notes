# GROUP BY + SUM() — total gasto por cada pessoa em cada empresa

## Tabela: 
| id | company | name     | sales |
|----|---------|----------|-------|
| 1  | Xerox   | Steveni  | 1.00  |
| 2  | Google  | Cheryl   | 5.00  |
| 3  | Google  | Claire   | 2.00  |
| 4  | Apple   | Cheryl   | 3.00  |
| 5  | Apple   | Steveni  | 1.00  |

## Comando SQL:
SELECT name, company, SUM(sales) AS quantidade_gasta
FROM table_1
GROUP BY name, company
ORDER BY name ASC, quantidade_gasta ASC;

## Resultado Esperado:
| name    | company | quantidade_gasta |
|---------|---------|------------------|
| Cheryl  | Apple   | 3.00             |
| Cheryl  | Google  | 5.00             |
| Claire  | Google  | 2.00             |
| Steveni | Apple   | 1.00             |
| Steveni | Xerox   | 1.00             |

---

## Explicacao:
- `SUM(sales)`  soma os valores da coluna `sales`.
- `GROUP BY name, company` cria grupos usando duas colunas ao mesmo tempo.
- O banco separa os dados por combinacao de pessoa e empresa.
- Depois soma as vendas dentro de cada grupo.

Calculo por grupo:
- Cheryl + Apple -> 3.00
- Cheryl + Google -> 5.00
- Claire + Google -> 2.00
- Steveni + Apple -> 1.00
- Steveni + Xerox -> 1.00

- `ORDER BY name ASC, quantidade_gasta ASC`:
  - Primeiro ordena pelo nome da pessoa.
  - Depois ordena pelo valor gasto dentro de cada pessoa.

## Observacoes:
- `GROUP BY` pode usar mais de uma coluna para criar grupos mais especificos.
- Isso eh muito comum em relatorios onde precisamos analisar comportamento por pessoa e empresa ao mesmo tempo.
- Os espacos mostrados no exemplo original nao existem no resultado real, eles foram apenas usados para facilitar a leitura.