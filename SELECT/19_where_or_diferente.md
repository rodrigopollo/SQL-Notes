```md
# SQL – WHERE OR (usando !=)

## TABELA>

---------------------------------
| NAME   | Choice  | ID |
---------------------------------
| Zach   | Green   | 25 |
| David  | Green   | 30 |
| Claire | Yellow  | 35 |
| David  | Red     | 40 |
---------------------------------

## OBJETIVO
Mostrar os **nomes** que cumprem **pelo menos uma** das condições:
- ID **menor que 40**
- Choice **diferente de 'Green'**

## COMANDO SQL
SELECT name  
FROM table_2  
WHERE id < 40 OR choice != 'Green';

## RESULTADO ESPERADO

-----------------
| NAME  |
-----------------
| Zach  |
| David |
| Claire|
| David |
-----------------

## EXPLICAÇAO
- O operador `OR` significa **OU** (ja visto anteriormente).
- O operador `!=` significa **diferente de**.
- A linha sera mostrada se **qualquer uma** das condiçoes for verdadeira.

Linha por linha:
- Zach (ID 25)
  - ID < 40 → TRUE  
  - Entra no resultado

- David (ID 30)  
  - ID < 40 → TRUE  
  - Entra no resultado

- Claire (ID 35)
  - ID < 40 → TRUE  
  - Choice != 'Green' → TRUE  
  - Entra no resultado

- David (ID 40)  
  - ID < 40 → FALSE  
  - Choice != 'Green' (Red) → TRUE  
  - Entra no resultado

## OBSERVAÇÕES
- Com `OR`, basta **uma condição verdadeira** para a linha aparecer.
- Por isso, neste exemplo, **todas as linhas** da tabela são retornadas.
- Para tornar o filtro mais restritivo, podemos usar `AND` em vez de `OR`.
```
