# MIN() — menor valor da coluna SALES

## Tabela:
| id | company | name     | sales |
|----|---------|----------|-------|
| 1  | Xerox   | Steveni  | 100   |
| 2  | Google  | Cheryl   | 500   |
| 3  | Google  | Claire   | 200   |
| 4  | Apple   | Theresa  | 300   |
| 5  | Apple   | Sherri   | 100   |

## Comando SQL:
SELECT MIN(sales)
FROM table_1;

## Resultado Esperado:
| min |
|-----|
| 100 |

## Explicaçao:
- A função **MIN()** retorna o menor valor encontrado em uma coluna numerica.
- Aqui ela percorre todos os valores da coluna **sales**.
- Sales tem os valores: 100, 500, 200, 300 e 100.
- O menor eh **100**.

## Observaçoes:
- `MIN()` ignora valores `NULL`.
- Pode ser usada com `WHERE` pra filtrar antes de calcular o menor valor.
- Note Professor: Muito comum em relatorios, analises e queries de validaçao.
