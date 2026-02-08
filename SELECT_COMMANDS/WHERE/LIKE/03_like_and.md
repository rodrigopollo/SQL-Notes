# LIKE — Começa com "C" e termina com "e"

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
Mostrar todos os nomes que **começam com "C"** **AND** **terminam com "e"**.

## Comando SQL:
SELECT *  
FROM table_1  
WHERE name LIKE 'C%' AND name LIKE '%e';

## Resultado esperado:

-----------------------------  
| Company | Name   | Sales |  
-----------------------------  
| Google | Claire | 200   |  
-----------------------------  

## Contagem:
SELECT COUNT(*)  
FROM table_1  
WHERE name LIKE 'C%' AND name LIKE '%e';

### Resultado da contagem:
1

## Explicaçao:
- `name LIKE 'C%'`
  - O nome **deve começar** com a letra **C**
- `name LIKE '%e'`
  - O nome **deve terminar** com a letra **e**
- `AND`
  - **As duas condiçoes precisam ser verdadeiras ao mesmo tempo**

Analisando os nomes:
- Cheryl → começa com C, mas **nao termina** com e = FALSE 
- Claire → começa com C **e termina** com e = TRUE
- Os demais não começam com C = FALSE

## Observaçoes:
- Poderia ser escrito tambem como: `name LIKE 'C%e'`
- `%` representa qualquer quantidade de caracteres antes ou depois
- `AND` sempre restringe o resultado (menos linhas)
