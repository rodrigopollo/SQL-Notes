# NOT BETWEEN — Filtra valores que **NAO** estejam dentro de um intervalo

## Tabela usada no exemplo:

---------------------------------
| Company | Name   | Sales |
---------------------------------
| Xerox  | Steven | 100   |
| Google | David  | 550   |
| Google | Claire | 200   |
| Apple  | Zach   | 250   |
| Apple  | Andew  | 350   |
---------------------------------

## Comando SQL:
SELECT *
FROM table_1
WHERE sales NOT BETWEEN 250 AND 550;

## Resultado esperado:

---------------------------------
| Company | Name   | Sales |
---------------------------------
| Xerox  | Steven | 100   |
| Google | Claire | 200   |
---------------------------------

## Explicaçao:
O operador **NOT BETWEEN** vai mostrar todos os registros que o valor **nao esteja dentro do intervalo inserido**.

Neste caso:
- O intervalo eh de **250 ate 550**
- Os valores **250 e 550 sao incluidos** no intervalo
- Entao, so os valores **menores que 250** ou **maiores que 550** são retornados

## Observaçoes:
- `BETWEEN` inclui os valores limites
- `NOT BETWEEN` exclui tudo que estiver dentro do intervalo (inclusive os limites)
