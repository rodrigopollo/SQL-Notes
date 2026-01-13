```md
# SQL – WHERE OR (Filtro múltiplo)

## TABELA: 

---------------------------------
| NAME   | Choice  | ID |
---------------------------------
| Zach   | Green   | 25 |
| David  | Green   | 30 |
| Claire | Yellow  | 35 |
| David  | Red     | 40 |
---------------------------------

## OBJETIVO
Mostrar uma lista com os **nomes** que cumprem **pelo menos uma** das condiçoes:
- ID **maior que 35**
- Choice **igual a 'Green'**

## COMANDO SQL
SELECT name  
FROM table_2  
WHERE id > 35 OR choice = 'Green';

## RESULTADO ESPERADO

-----------------
| NAME  |
-----------------
| Zach  |
| David |
| David |
-----------------

## EXPLICAÇÃO
- O operador `OR` significa **OU**.
- A info vai ser mostrada se **qualquer uma** das condiçoes for verdadeira.
  - Zach → Choice é Green → TRUE
  - David (ID 30) → Choice é Green → TRUE
  - Claire → não cumpre nenhuma condição → FALSE
  - David (ID 40) → ID > 35 → TRUE

## OBSERVAÇÕES
- `OR` eh menos restritivo que `AND`.
- Resultados podem incluir valores repetidos.
- Para remover duplicados, seria necessário usar `DISTINCT`.
```
