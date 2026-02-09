# ILIKE — Começa com "s" e termina com "i" (case-insensitive)

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
Mostrar todos os nomes que **começam com "s"** e **terminam com "i"**,  
**independente de maiúsculas ou minúsculas**.

## Comando SQL:
SELECT *  
FROM table_1  
WHERE name ILIKE 's%' AND name ILIKE '%i';

## Resultado esperado:

-----------------------------  
| Company | Name    | Sales |  
-----------------------------  
| Xerox  | Steveni | 100   |  
| Apple  | Sherri  | 100   |  
-----------------------------  

---

## Se usasemos Contagem:
SELECT COUNT(*)  
FROM table_1  
WHERE name ILIKE 's%' AND name ILIKE '%i';

### Resultado da contagem:
2

---

## Explicaçao:
- `ILIKE`
  - Funciona como o `LIKE`, mas **ignora maiusculas e minusculas**
- `name ILIKE 's%'`
  - O nome deve **começar com "s" ou "S"**
- `name ILIKE '%i'`
  - O nome deve **terminar com "i" ou "I"**
- `AND`
  - As duas condiçoes precisam ser verdadeiras ao mesmo tempo

Analisando os nomes:
- Steveni → começa com S e termina com i = TRUE  
- Sherri → começa com S e termina com i = TRUE  
- Cheryl → não começa com S = FALSE  
- Claire → não começa com S = FALSE  
- Theresa → não termina com i = FLASE  

## Observaçoes:
- `AND` sempre restringe o resultado final
