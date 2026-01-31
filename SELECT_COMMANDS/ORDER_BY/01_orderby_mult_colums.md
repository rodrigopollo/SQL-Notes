# SQL – ORDER BY (ASC alfabético e ASC numérico)

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

## OBJETIVO:
Ordenar os dados seguindo **dois criterios ao mesmo tempo**:
1. Company em ordem **alfabetica crescente (ASC – A → Z)**
2. Sales em ordem **numerica crescente (ASC – menor → maior)** quando a Company for igual


## COMANDO SQL:
SELECT company, name, sales  
FROM table_1  
ORDER BY company ASC, sales ASC;


## RESULTADO ESPERADO:
---------------------------------
| Company | Name   | Sales |
---------------------------------
| Apple  | Andew  | 100   |
| Apple  | Zach   | 300   |
| Google | Claire | 200   |
| Google | David  | 500   |
| Xerox  | Steven | 100   |
---------------------------------

## EXPLICAÇAO:
- O `ORDER BY company ASC` organiza primeiro as empresas em ordem alfabética.
- Como existem empresas repetidas (Apple e Google), entra o segundo critério:
  - `sales ASC` organiza os valores de vendas do menor para o maior **dentro da mesma empresa**.
- Por isso:
  - Apple aparece como:
    - 100
    - 300
  - Google aparece como:
    - 200
    - 500

## OBSERVAÇOES:
- `ASC` eh o padrão do SQL (mesmo sem escrever, ele assume ASC).
- Se fosse usado `sales DESC`, o maior valor apareceria primeiro dentro da mesma empresa.
- A ordem dos campos no `ORDER BY` importa e define a prioridade da organização.

