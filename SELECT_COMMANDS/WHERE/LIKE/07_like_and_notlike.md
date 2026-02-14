# LIKE + NOT LIKE — filtro combinado de padrões

## Tabela:
-------------------------------------------------
| id | Company Name | Sales |
-------------------------------------------------
| 1  | Xerox Steveni | 100 |
| 2  | Google Cheryl | 500 |
| 3  | Google Claire | 200 |
| 4  | Apple Theresa | 300 |
| 5  | Apple Sherri  | 100 |
-------------------------------------------------

## Comando SQL:
SELECT name  
FROM table_1  
WHERE name LIKE 'S%'  
  AND name NOT LIKE '%he%';

## Resultado Esperado:
-----------------
| name     |
-----------------
| Steveni |
-----------------

## Contagem:
SELECT COUNT(*)  
FROM table_1  
WHERE name LIKE 'S%'  
  AND name NOT LIKE '%he%';

## Resultado da Contagem
-----------------
| count |
-----------------
| 1     |
-----------------

## Explicação
- `LIKE 'S%'` filtra apenas nomes que **começam com a letra S**.
- `NOT LIKE '%he%'` exclui qualquer nome que **contenha a sequência "he"** em qualquer posição.
- O operador **AND** exige que **as duas condições sejam verdadeiras ao mesmo tempo**.
- `Sherri` é excluído porque contém `he`.
- Apenas **Steveni** começa com `S` **e** não contém `he`.

## Observações
- `%` representa qualquer quantidade de caracteres.
- A ordem das condições no `WHERE` não altera o resultado, apenas a leitura.
- Esse tipo de combinação é muito comum para filtros mais específicos em texto.