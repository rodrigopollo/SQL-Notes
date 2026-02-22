# Função ROUND(AVG())

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

SELECT ROUND(AVG(sales), 2)
FROM table_1;

## Resultado Esperado:

240,00

---

## Explicaçao:
 `AVG()` calcula a media dos valores da coluna `SALES`.  
 `ROUND()` usamos para especificar quantas casas decimais queremos ver, neste caso 2 (ex: 10.00)

- Soma total de `SALES`:  
  100 + 500 + 200 + 300 + 100 = **1200**
- Quantidade de registros: **5**

O `AVG()` vai calcular a media:
    1200 / 5 = 240

O `ROUND(AVG(sales), 2)`, vai pegar o resultado da media **240** e aplicar a quantidade de casas decimais
que voce quer, neste caso foi 2 e vai mostrar pra voce **240,00**, com duas casas decimais.

## Observaçoes:
- `AVG()` ignora valores `NULL`.
- Se usar `ROUND()`, em um numero inteiro (`INT`) ele vai mostrar como numero real (`REAL`), por exemplo: `240` → `240,00`.
- DICA PROFESSOR: De preferencia ao uso de `ROUND()` quando o valor for realmente `REAL` ou em casos de **relatorios**
e **planilhas**, onde o formato visual eh importante.