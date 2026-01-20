# SQL – ORDER BY (DESC alfabético e DESC numérico)

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
Ordenar os dados usando **ordem decrescente (DESC)**:
1. Company em ordem alfabetica **decrescente (Z → A)**
2. Sales em ordem numerica **decrescente (maior → menor)** quando a Company for igual

---

## COMANDO SQL
SELECT company, name, sales  
FROM table_1  
ORDER BY company DESC, sales DESC;

---

## RESULTADO ESPERADO
---------------------------------
| Company | Name   | Sales |
---------------------------------
| Xerox  | Steven | 100   |
| Google | David  | 500   |
| Google | Claire | 200   |
| Apple  | Zach   | 300   |
| Apple  | Andew  | 100   |
---------------------------------


## EXPLICAÇAO
- `ORDER BY company DESC` organiza primeiro as empresas em ordem alfabetica decrescente.
- Como existem empresas repetidas (Google e Apple), entra o segundo criterio:
  - `sales DESC` organiza as vendas do maior para o menor **dentro da mesma empresa**.
- Por isso:
  - Google aparece como:
    - 500
    - 200
  - Apple aparece como:
    - 300
    - 100

## OBSERVAÇOES
- `DESC` inverte completamente a ordem padrão do SQL, por padrao ele vem ASCENDENTE.
- Da pra misturar tbm, por exemplo:
  - `ORDER BY company ASC, name DESC`
- A ordem dos campos no `ORDER BY` define a prioridade da organização.
