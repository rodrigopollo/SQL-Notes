# LIKE — Contém a sequência "%he%"

## Tabela de exemplo:

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
Mostrar todos os nomes que **contenham a sequência de letras "he" em qualquer posição** do texto.

## Comando SQL:
SELECT *  
FROM table_1  
WHERE name LIKE '%he%';

## Resultado esperado:

-----------------------------  
| Company | Name     | Sales |  
-----------------------------  
| Google | Cheryl   | 500   |  
| Apple  | Theresa | 300   |  
| Apple  | Sherri  | 100   |  
-----------------------------  

## Caso quisessemos usar Contagem (COUNT):
SELECT COUNT(*)  
FROM table_1  
WHERE name LIKE '%he%';

### Resultado da contagem:
3

---

## Explicaçao:
- `LIKE '%he%'`
  - `%` antes de `he` → pode vim qualquer coisa antes ou nada, nao importa.  
  - `he` → tem que ter 'HE' 
  - `%` depois de `he` → tbm nao importa oq vem depois, ou ate se nao vem nada  
- Ou seja: 
    O nome **pode ter qualquer coisa**, desde que **contenha "he" em algum ponto**

Analisando os nomes:
- Cheryl → tem "he" = TRUE    
- Theresa → tem "he" = TRUE  
- Sherri → tem "he" = TRUE  
- Steveni → nao tem "he" = FALSE  
- Claire → nao tem "he" = FALSE   

## Observaçoes:
- `LIKE` eh **case-sensitive**
- Para ignorar maiusculas/minusculas, usamos `ILIKE`
- `%` representa qualquer quantidade de caracteres ou nenhum
