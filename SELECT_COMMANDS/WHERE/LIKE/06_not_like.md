# NOT LIKE — nomes que NÃO contêm determinado padrão

## Tabela: 
----------------------------
| id | Company Name | Sales |
----------------------------
| 1  | Xerox Steveni | 100 |
| 2  | Google Cheryl | 500 |
| 3  | Google Claire | 200 |
| 4  | Apple Theresa | 300 |
| 5  | Apple Sherri  | 100 |
----------------------------

## Comando SQL:
SELECT name  
FROM table_1  
WHERE name NOT LIKE '%he%';

## Resultado Esperado:
Steveni 
Claire  


## Contagem:
SELECT COUNT(*)  
FROM table_1  
WHERE name NOT LIKE '%he%';

## Resultado da Contagem:
2

---

## Explicaçao:
- O **NOT LIKE** inverte a logica, mostrando so os nomes que **nao tem 'HE'** nele.
- No exemplo, **Cheryl**, **Theresa** e **Sherri** sao excluidos porque TEM **he**.
- Restando so **Steveni** e **Claire**, ou seja, **2 registros**.

## Observaçoes:
- Sempre conferir se o campo correto esta sendo usado no WHERE (neste caso, `name`).