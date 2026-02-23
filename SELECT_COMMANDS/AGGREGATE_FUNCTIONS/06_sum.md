# Função SUM()

## Tabela: 

------------------------------
| Company | Name     | Sales |
------------------------------
| Xerox   | Steveni  | 100   |
| Google  | Cheryl   | 500   |
| Google  | Claire   | 200   |
| Apple   | Theresa  | 300   |
| Apple   | Sherri   | 100   |
------------------------------

## Comando SQL:

SELECT SUM(sales)
FROM table_1;

## Resultado Esperado:
1200

---

## Explicaçao:
A funçao `SUM()` se usa pra calcular a **soma total** dos valores de uma coluna.

Soma dos valores da coluna `SALES`:
100 + 500 + 200 + 300 + 100 = **1200**

## Observaçoes:
- `SUM()` so consedera valores numericos.
- Valores `NULL` sao ignorados
- NOTA PROFESSOR: Muito utilizada em **relatorios**, **dashboards** e **analises financeiras**.