# MAX() — maior valor da coluna SALES

## Tabela: 
| id | company | name     | sales |
|----|---------|----------|-------|
| 1  | Xerox   | Steveni  | 100   |
| 2  | Google  | Cheryl   | 500   |
| 3  | Google  | Claire   | 200   |
| 4  | Apple   | Theresa  | 300   |
| 5  | Apple   | Sherri   | 100   |

## Comando SQL:
SELECT MAX(sales)
FROM table_1;

## Resultado Esperado:
| max |
|-----|
| 500 |

## Explicaçao:
- `MAX()` eh um **aggregate function** que mostra o maior valor de uma coluna.
- A funçao vai percorrer todos os valores da coluna `sales`.
- Valores existentes: 100, 500, 200, 300, 100.
- O maior valor eh **500**.

## Observaçoes:
- `MAX()` ignora valores `NULL`.
- Pode ser combinada com `WHERE` para encontrar o maior valor dentro de um subconjunto de dados.

