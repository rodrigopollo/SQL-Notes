# LIKE + NOT LIKE — filtro combinado de padrões

## Tabela:
| id | company | name     | sales |
|----|---------|----------|-------|
| 1  | Xerox   | Steveni  | 100   |
| 2  | Google  | Cheryl   | 500   |
| 3  | Google  | Claire   | 200   |
| 4  | Apple   | Theresa  | 300   |
| 5  | Apple   | Sherri   | 100   |

## Comando SQL:
SELECT name  
FROM table_1  
WHERE name LIKE 'S%'  
  AND name NOT LIKE '%he%';

## Resultado Esperado:
| name     |
|----------|
| Steveni  |

## Contagem:
SELECT COUNT(*)  
FROM table_1  
WHERE name LIKE 'S%'  
  AND name NOT LIKE '%he%';

## Resultado da Contagem:
| count |
|-------|
| 1     |

---

## Explicaçao:
- `LIKE 'S%'` seleciona so os nomes que começam com a letra **S**.
- `NOT LIKE '%he%'` remove qualquer nome que tenha **he**.
- `AND`  as 2 condiçoes tem q ser verdadeiras.
- `Sherri` começa com **S**, mas tem **he** = FALSE
- Apenas **Steveni** encaixa nas 2 regras = TRUE

## Observaçoes:
- `%` representa qualquer quantidade de caracteres antes ou depois do padrão, ate mesmo nada.
