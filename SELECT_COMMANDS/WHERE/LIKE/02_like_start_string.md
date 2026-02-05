# LIKE — Começa com determinada letra (C%)

## Tabela:

-----------------------------  
| Company | Name    | Sales |  
-----------------------------  
| Xerox  | Steveni | 100   |  
| Google | Cheryl  | 500   |  
| Google | Claire  | 200   |  
| Apple  | Theresa | 300   |  
| Apple  | Sherri  | 100   |  
-----------------------------  

## Objetivo:
Mostrar todos os nomes que **começam com a letra "C"**.

## Comando SQL:
SELECT *  
FROM table_1  
WHERE name LIKE 'C%';

## Resultado esperado:

-----------------------------  
| Company | Name    | Sales |  
-----------------------------  
| Google | Cheryl | 500   |  
| Google | Claire | 200   |  
-----------------------------  

## Comando:
SELECT COUNT(*)  
FROM table_1  
WHERE name LIKE 'C%';

### Resultado da contagem:
2

## Explicaçao:
- `'C%'` significa o seguinte:
  - `C` → o texto **deve começar** com a letra C  
  - `%` → pode ter **qualquer coisa depois** (qualquer quantidade de caracteres)

Portanto:
- Cheryl → começa com C ✔  
- Claire → começa com C ✔  
- Os outros nomes não começam com C 

## Observaçoes:
- `%C` → termina com C  
- `%C%` → contém C em qualquer posiçao  
- `_C%` → C na **segunda posiçao**
