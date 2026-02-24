# GROUP BY + SUM()

## Tabela:

------------------------------
| Company | Name     | Sales |
------------------------------
| Xerox   | Steveni  | 1.00  |
| Google  | Cheryl   | 5.00  |
| Google  | Claire   | 2.00  |
| Apple   | Cheryl   | 3.00  |
| Apple   | Steveni  | 1.00  |
------------------------------

## Comando SQL:

SELECT 
    company, 
    SUM(sales) AS soma_total
FROM table_1
GROUP BY company
ORDER BY soma_total ASC;

## Resultado Esperado:

------------------------
| company | soma_total |
------------------------
| Xerox   | 1.00       |
| Apple   | 4.00       |
| Google  | 7.00       |
------------------------

---

## Explicacao:
A clausula `GROUP BY` eh utilizada pra **agrupar registros com o mesmo valor** em uma coluna.  
A funcao `SUM()` calcula a **soma dos valores de `SALES` dentro de cada grupo**.

Calculo por empresa:
- Xerox: 1.00  
- Apple: 3.00 + 1.00 = **4.00**  
- Google: 5.00 + 2.00 = **7.00**

O `ORDER BY soma_total ASC` organiza o resultado do **menor para o maior faturamento**.


## Observacoes:
- Toda coluna no `SELECT` que não for uma função de agregação (como SUM, COUNT, AVG, etc.) 
deve obrigatoriamente aparecer na cláusula `GROUP BY`

Ex desse exercicio:
company e SUM(sales) foram usados no `SELECT`
`SUM` eh um AGGREGATE FUNCION, ou seja, nao vai ser usado em GROUP BY.
company em vez disso eh 1 coluna real e existente da tabela e tem que aparecer no GROUP BY

- `SUM()` ignora valores `NULL`.
- `GROUP BY` eh geralmente usado junto com funcoes de agregacao (`SUM`, `AVG`, `COUNT`, `MIN`, `MAX`).