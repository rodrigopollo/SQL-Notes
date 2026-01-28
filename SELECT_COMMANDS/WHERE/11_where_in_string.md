# WHERE IN (STRING)

## Tabela de exemplo

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
WHERE name IN ('Claire', 'Andew');

## Resultado esperado:

---------------------------------
| Company | Name   | Sales |
---------------------------------
| Google  | Claire | 200   |
| Apple   | Andew  | 100   |
---------------------------------

## Explicaçao:
O operador **IN** também funciona com **STRING (texto)**.  
Nesse caso ele vai mostrar **SO os nomes da coluna name** que sejam **exatamente** iguais a CLAIRE e ANDEW.
Como fica:
- So os nomes **Claire** e **Andew** seram mostrados.
- Todos os outros nomes vao ser ignorados

## Observaçoes:
- `IN ('Claire', 'Andew')` equivale a:
  - `name = 'Claire' OR name = 'Andew'`
- Atençao: **STRING eh case-sensitive** na maioria dos bancos de dados

- Se fosse utilizado:
  SELECT COUNT(*)
  FROM table_1
  WHERE name IN ('Claire', 'Andew');

  O resultado seria **2**, pois **2 registros** cumprem a condição.
