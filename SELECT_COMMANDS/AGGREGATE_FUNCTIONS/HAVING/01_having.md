# HAVING + SUM()

## Tabela: table_1

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

## Comando SQL
SELECT 
    name, 
    SUM(amount) AS quantidade_gasta
FROM table_1
GROUP BY name
HAVING SUM(amount) > 18
ORDER BY quantidade_gasta ASC;


## Resultado Esperado

-----------------------------
| name   | quantidade_gasta |
-----------------------------
| David  | 20.00            |
| Claire | 40.00            |
| Steven | 40.00            |
-----------------------------

---

## Explicacao
O `GROUP BY` agrupa os registros pelo campo `name`.  
O `SUM(amount)` calcula o total gasto por cada pessoa.

O `HAVING` eh utilizado pra **filtrar os resultados ants de motrar para o usuario sem modificar nada**.

Calculo por pessoa:
- Claire: 25.00 + 15.00 = 40.00  
- David: 20.00  
- Steven: 30.00 + 10.00 = 40.00  
- Andew: 12.00  
- Zach: 18.00  

Depois de calcular todos os valores, o `HAVING SUM(amount) > 18` filtra e mostra so quem gastou mais de 18.

## Observacoes
- `WHERE` filtra **antes** do `GROUP BY`.
- `HAVING` filtra **depois** do `GROUP BY`.
- `HAVING` eh usado com funcoes de agregacao (`SUM`, `AVG`, `COUNT`, etc).
- Registros com valores menores ou iguais a 18 nao vao aparecer para o USUARIO por causa da condiçao do HAVING.