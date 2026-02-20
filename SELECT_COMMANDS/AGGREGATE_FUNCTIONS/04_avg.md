# AVG() — média dos valores da coluna SALES

## Tabela:
| id | company | name     | sales |
|----|---------|----------|-------|
| 1  | Xerox   | Steveni  | 100   |
| 2  | Google  | Cheryl   | 500   |
| 3  | Google  | Claire   | 200   |
| 4  | Apple   | Theresa  | 300   |
| 5  | Apple   | Sherri   | 100   |

## Comando SQL:
SELECT AVG(sales)
FROM table_1;

## Resultado Esperado:
| avg |
|-----|
| 240 |

## Explicaçao:
- `AVG()` eh usado pra calcular a media dos valores de uma coluna numerica.
- A funçao soma todos os valores da coluna `sales` e divide pela quantidade de registros, ou seja, faz a media.
- Soma dos valores: 100 + 500 + 200 + 300 + 100 = **1200**.
- Quantidade de registros: **5**.
- Cálculo: `1200 / 5 = 240`.

## Observaçoes:
- `AVG()` ignora valores `NULL`.
