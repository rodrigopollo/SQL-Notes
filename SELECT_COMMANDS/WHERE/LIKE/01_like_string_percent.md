# LIKE — sequência de caracteres (_ e %)

## Tabela:

-----------------------------
| Company | Name     | Sales |
-----------------------------
| Xerox   | Steveni  | 100   |
| Google  | Cheryl   | 500   |
| Google  | Claire   | 200   |
| Apple   | Theresa  | 300   |
| Apple   | Sherri   | 100   |
-----------------------------

## Comando SQL:
SELECT *
FROM table_1
WHERE name LIKE '_her%';


## Resultado esperado:

-----------------------------
| Company | Name     | Sales |
-----------------------------
| Google  | Cheryl   | 500   |
| Apple   | Theresa  | 300   |
| Apple   | Sherri   | 100   |
-----------------------------

--- 

## Explicaçao:


Aqui estamos usan do **_her%** que significa o seguinte:

- `_` (underscore)  
  Representa **exatamente 1 caracterer**.  Ca
  Aqui significa: *depois do primeiro caractere*.

- `her`  
  Sao as letras que **TEM QUE existir exatamente nessa mesma ordem**.  
  ATENÇAO: Em muitos bancos de dados, isso eh **case-sensitive**.

- `%`  
  Representa **qualquer sequencia de caracteres**, inclusive nenhuma.  
  Ou seja: nao importa o que vem depois de `her`

## Por que esses nomes apareceram?:
- **Cheryl** → C + her + yl  
- **Theresa** → T + her + esa  
- **Sherri** → S + her + ri  

Todos seguem o padrao:  
**1 letra qualquer + "her" + qualquer coisa ou nada**

## Observações importantes:
- Se fosse `__her%`  
  → significaria **depois dos 2 primeiros caracteres**. 

- Se fosse `%her`  
  → não importa o que vem antes, **termina com "her"**. (Ex: Esther)

- Se fosse `%her%`  
  → "her" pode estar **em qualquer posição da palavra**. (Ex: Esther, Sherri, Theressa etc...)
