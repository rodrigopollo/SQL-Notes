# SQL – WHERE AND (Filtro múltiplo)

## TABELA: table_2

---------------------------------
| NAME   | Choice  | ID |
---------------------------------
| Zach   | Green   | 25 |
| David  | Green   | 30 |
| Claire | Yellow  | 35 |
| David  | Red     | 40 |
---------------------------------

## OBJETIVO
Mostrar **apenas os nomes** que cumprem **todas** as condições abaixo:

- ID **maior que 25**
- Choice **igual a 'Red'**

## COMANDO SQL

SELECT name  
FROM table_2  
WHERE id > 25 AND choice = 'Red';

## RESULTADO ESPERADO

-----------------
| NAME  |
-----------------
| David |
-----------------

## EXPLICAÇÃO
- So mostra quem tem:
  - ID = 40
  - Choice = 'Red'
- Entao so mostra **David**.

## OBSERVAÇÕES
- Se uma linha nao cumprir **qualquer** condiçao, ela eh descartada.
- `AND` deixa o filtro mais restritivo adicionando uma segunda verificaçao.
- Note que tem 2 "David" na tabela, mas so **um** atende as condições.

