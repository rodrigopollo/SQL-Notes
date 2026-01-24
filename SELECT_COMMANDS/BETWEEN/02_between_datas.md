# BETWEEN DATE — Filtrar registros entre **datas**

## Tabela:

------------------------------------
| Company | Name   | Date       |
------------------------------------
| Oppo   | Steven | 07/09/2025 |
| Xioami | David  | 05/02/2025 |
| Huwai  | Claire | 23/07/2025 |
| Apple  | Zach   | 28/08/2025 |
| Apple  | Andew  | 30/05/2025 |
------------------------------------


## Comando SQL:
SELECT *
FROM table_1
WHERE date BETWEEN '01/07/2025' AND '07/09/2025';

---

## Resultado esperado:

------------------------------------
| Company | Name   | Date       |
------------------------------------
| Oppo   | Steven | 07/09/2025 |
| Huwai  | Claire | 23/07/2025 |
| Apple  | Zach   | 28/08/2025 |
------------------------------------

---

## NOTE:
- `BETWEEN` **inclui** as datas inicial e final.
- Se a coluna for `TIMESTAMP` (data + hora), a pratica correta seria:
  - usar a data inicial normalmente
  - usar **data final + 1 dia**

Exemplo:
- `'01/07/2025' AND '07/09/2025'`
- vai virar: `'01/07/2025' AND '08/09/2025'`
 
---

## Explicaçao:
- O operador **BETWEEN DATE** retorna todos os registros cuja data esteja **dentro do intervalo informado**
- As datas **01/07/2025** e **07/09/2025** tbm sao incluidas no resultado
- As datas fora desse intervalo nao vao aparecer


## Observaçoes:
- Quando for `TIMESTAMP`, usamos a **data final + 1 dia** pra nao perder os registros do ultimo dia
