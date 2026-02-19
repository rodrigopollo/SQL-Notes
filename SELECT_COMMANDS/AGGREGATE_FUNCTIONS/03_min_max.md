# MAX() e MIN() — maior e menor valor da coluna SALES

## Tabela:
| id | company | name     | sales |
|----|---------|----------|-------|
| 1  | Xerox   | Steveni  | 100   |
| 2  | Google  | Cheryl   | 500   |
| 3  | Google  | Claire   | 200   |
| 4  | Apple   | Theresa  | 300   |
| 5  | Apple   | Sherri   | 100   |

## Comando SQL:
SELECT MAX(sales), MIN(sales)
FROM table_1;

## Resultado Esperado:
| max | min |
|-----|-----|
| 500 | 100 |

## Explicaçao:
- `MAX()` mostra o **maior valor** da coluna `sales`.
- `MIN()` mostra o **menor valor** da coluna `sales`.
- Tanto MIN como MAX sao **aggregate functions** e analisam todos os registros da tabela.
- Os valores sao: `sales`: 100, 500, 200, 300 e 100.
- O maior valor eh **500** e o menor **100**.

## Observaçoes:
- Funçoes agregadas ignoram `NULL`.
- Usamos `MAX()` e `MIN()` juntos pra obter ver um intervalo de valores especificos.
- Podem ser combinadas com `WHERE` para aplicar filtros no calculo.