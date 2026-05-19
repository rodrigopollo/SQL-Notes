# INNER JOIN Multiplo + DATE()

## Tabela: film
------------------------------
| film_id | title            |
------------------------------
| 1       | Action Hero      |
| 2       | Mystery Night    |
| 3       | Romantic Escape  |
| 4       | Space Journey    |
------------------------------

## Tabela: inventory
--------------------------
| inventory_id | film_id |
--------------------------
| 101          | 1       |
| 102          | 2       |
| 103          | 3       |
| 104          | 4       |
--------------------------

## Tabela: rental
--------------------------------------------------
| rental_id | inventory_id | return_date         |
--------------------------------------------------
| 1         | 101          | 2005-05-29 10:15:00 |
| 2         | 102          | 2005-05-30 18:40:00 |
| 3         | 103          | 2005-05-28 21:00:00 |
| 4         | 104          | 2005-05-31 09:20:00 |
--------------------------------------------------

## Comando SQL
SELECT
    f.title,
    DATE(r.return_date) AS return_date
FROM film AS f
INNER JOIN inventory AS i
    ON i.film_id = f.film_id
INNER JOIN rental AS r
    ON r.inventory_id = i.inventory_id
WHERE
    r.return_date >= '2005-05-29'
    AND r.return_date <= '2005-05-30'
ORDER BY
    f.title ASC;


## Resultado Esperado
--------------------------------
| title          | return_date |
--------------------------------
| Action Hero    | 2005-05-29  |
--------------------------------

---

## Explicacao
Este exemplo utiliza multiplos `INNER JOIN` para conectar 3 tabelas diferentes.

Fluxo da query:
1. A tabela `film` tem os nomes dos filmes
2. A tabela `inventory` conecta os filmes ao inventario
3. A tabela `rental` tem os alugueis e devolucoes

- Primeiro JOIN  -->  i.film_id = f.film_id
    * Liga os filmes ao inventario.

- Segundo JOIN  -->  r.inventory_id = i.inventory_id
    * Liga o inventario aos alugueis.

Depois disso, o `WHERE` filtra so registros onde:
- `return_date` eh maior ou igual a `2005-05-29`
- `return_date` eh menor ou igual a `2005-05-30`

A funcao:
DATE(r.return_date)  remove a parte da hora e mostra so a data.

Resultado:
- So `Action Hero` entra no filtro
- Os outros filmes tem datas fora da faixa


## Observacoes
- `DATE()` extrai so a data de um valor `TIMESTAMP`.
- Multiplos `JOIN` sao muito comuns em bancos relacionais reais.
- `ORDER BY f.title ASC` organiza os filmes em ordem alfabetica.
- O filtro funciona usando comparacao de datas.