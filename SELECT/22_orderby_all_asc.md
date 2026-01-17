```md
# SQL – ORDER BY usando SELECT *

## TABELA:
---------------------------------
| Company | Name   | Sales |
---------------------------------
| Apple  | Andew  | 100   |
| Google | David  | 500   |
| Apple  | Zach   | 300   |
| Google | Claire | 200   |
| Xerox  | Steven | 100   |
---------------------------------

## OBJETIVO
Ordenar **apenas pela coluna Company**, mantendo **todas as colunas visíveis** usando `SELECT *`.

## COMANDO SQL
SELECT *  
FROM table_1  
ORDER BY company ASC;

## RESULTADO ESPERADO
---------------------------------
| Company | Name   | Sales |
---------------------------------
| Apple  | Andew  | 100   |
| Apple  | Zach   | 300   |
| Google | David  | 500   |
| Google | Claire | 200   |
| Xerox  | Steven | 100   |
---------------------------------

## EXPLICAÇÃO
- `ORDER BY company ASC` organiza **somente pela coluna Company**, em ordem alfabetica crescente.
- Como **não existe um segundo criterio de ordenaçao**, os valores de `Sales`:
seguem a ordem original dentro de cada Company

## OBSERVAÇÕES
- Se quiser organizar tbm os valores de vendas, precisa de outra condiçao:
  
  ORDER BY company ASC, sales ASC
```
