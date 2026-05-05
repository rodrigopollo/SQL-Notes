# HAVING + COUNT()

## Tabela: table_1:
---------------------------------------------------
| company | name   | payment_date        | amount |
---------------------------------------------------
| Huwai   | Claire | 2025-07-23 22:05:00 | 25.00  |
| Xioami  | David  | 2025-02-05 14:45:00 | 20.00  |
| Huwai   | Claire | 2025-07-23 09:30:00 | 15.00  |
| Apple   | Andew  | 2025-05-30 23:55:00 | 12.00  |
| Apple   | Zach   | 2025-06-01 10:15:00 | 18.00  |
| Oppo    | Steven | 2025-09-07 21:40:00 | 30.00  |
| Oppo    | Steven | 2025-09-07 08:15:00 | 10.00  |
---------------------------------------------------

## Comando SQL:
SELECT 
    name,
    COUNT(*) AS quantidade_pagamentos
FROM table_1
GROUP BY name
HAVING COUNT(*) > 1
ORDER BY quantidade_pagamentos DESC;


## Resultado Esperado
----------------------------------
| name   | quantidade_pagamentos |
----------------------------------
| Claire | 2                     |
| Steven | 2                     |
----------------------------------

---

## Explicacao
O `GROUP BY` agrupa pelo campo `name`.  
A funcao `COUNT(*)` conta quantos pagamentos cada pessoa fez.

O `HAVING` eh utilizado pra filtrar os resultados que vao aparecer para o usuario (ele n altera nada).

Calculo por pessoa:
- Claire: 2 pagamentos  
- Steven: 2 pagamentos  
- David: 1 pagamento  
- Andew: 1 pagamento  
- Zach: 1 pagamento  

O `HAVING COUNT(*) > 1` filtra apenas pessoas com mais de um pagamento.

## Observacoes
- `COUNT(*)` conta todas as linhas, incluindo valores repetidos.
- `HAVING` eh ideal para filtrar resultados agregados.
- Muito usado para encontrar duplicacoes ou frequencias maiores que 1.