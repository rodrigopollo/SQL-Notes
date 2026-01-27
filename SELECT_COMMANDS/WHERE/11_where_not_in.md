# WHERE NOT IN (NUMBER)

## Tabela:

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
WHERE sales NOT IN (100, 200);

## Resultado esperado:

---------------------------------
| Company | Name  | Sales |
---------------------------------
| Google  | David | 500   |
| Apple   | Zach  | 300   |
---------------------------------

## Explicaçao:
O operador **NOT IN** faz exatamente o oposto do **IN**.  
Ele vai retornar **so** as linhas em **sales NAO tem 100 ou 200**.

Entao:
- Valores **100** e **200** foram **excluídos**
- So os registros com **500** e **300** vao ser mostrados no resultado

## Observaçoes:
- `NOT IN (100, 200)` equivale a:
  - `sales != 100 AND sales != 200`

---
  SELECT COUNT(*)
  FROM table_1
  WHERE sales NOT IN (100, 200);

  O resultado seria **2**, pois apenas **2 registros** cumprem essa condição.
