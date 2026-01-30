# WHERE IN (NUMBER)

## Tabela de exemplo:

---------------------------------
| Company | Name   | Sales |
---------------------------------
| Xerox   | Steven | 100   |
| Google  | David  | 500   |
| Google  | Claire | 200   |
| Apple   | Zach   | 300   |
| Apple   | Andew  | 100   |
---------------------------------

## Comando SQL:
SELECT *
FROM table_1
WHERE sales IN (100, 200);

## Resultado esperado:

---------------------------------
| Company | Name   | Sales |
---------------------------------
| Xerox   | Steven | 100   |
| Google  | Claire | 200   |
| Apple   | Andew  | 100   |
---------------------------------

## Explicaçao:
O operador **IN** eh usado para filtrar valores especificos dentro de uma coluna.  
Neste exemplo, ele vai mostrar **so** as linhas onde **sales** eh igual a **100 ou 200**.
Tudo que nao for **100 ou 200** nao vai aparecer no resultado.


## Observaçoes:
- `IN (100, 200)` funciona como um atalho para:
  - `sales = 100 OR sales = 200`
  
  SELECT COUNT(*)
  FROM table_1
  WHERE sales IN (100, 200);

  O resultado seria **3**, pois existem **3 registros** ja que tem 3 registros com esses valores na tabela.
