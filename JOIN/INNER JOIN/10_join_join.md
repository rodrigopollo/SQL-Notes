# INNER JOIN Multiplo (3 Tabelas)

## Tabela: actor
-----------------------------------------
| actor_id | first_name | last_name |
-----------------------------------------
| 1        | Nick       | Wahlberg  |
| 2        | Ed         | Chase     |
| 3        | Jennifer   | Davis     |
-----------------------------------------

## Tabela: film_actor
------------------------
| actor_id | film_id |
------------------------
| 1        | 10      |
| 1        | 11      |
| 2        | 12      |
------------------------

## Tabela: film
--------------------------------
| film_id | title            |
--------------------------------
| 10      | Action Hero      |
| 11      | Romantic Escape  |
| 12      | Mystery Night    |
--------------------------------


## Comando SQL
SELECT
    f.title,
    a.first_name,
    a.last_name
FROM actor AS a
JOIN film_actor AS fa
    ON a.actor_id = fa.actor_id
JOIN film AS f
    ON fa.film_id = f.film_id
WHERE
    a.first_name = 'Nick'
    AND a.last_name = 'Wahlberg';


## Resultado Esperado
------------------------------------------------
| title            | first_name | last_name |
------------------------------------------------
| Action Hero      | Nick       | Wahlberg  |
| Romantic Escape  | Nick       | Wahlberg  |
------------------------------------------------

---

## Explicacao
Nesse exemplo se usam mais de um `INNER JOIN` para conectar as 3 tabelas.

Fluxo da query:
1. A tabela `actor` contem os atores
2. A tabela `film` contem os nomes dos filmes
3. A tabela `film_actor` faz a ligacao entre as 2 tabelas (actor e film)

 * Primeiro JOIN ->  a.actor_id = fa.actor_id
Liga os atores ao filmes que eles fizeram com a tabela `film_actor`, mas nessa tabela os filmes estao 
identificados por ID e nao por nome por isso precisamos de outro JOIN.

 * Segundo JOIN ->  fa.film_id = f.film_id
Liga a tabela `film_actor` com a tabela `film` pra descobrir o nome dos filmes de cada ID 
(ex: ID 10 = Action Hero )


Depois disso, o `WHERE` filtra so os filmes que o nosso ator participou:
- first_name = 'Nick'
- last_name = 'Wahlberg'

Resultado:
- Nick Wahlberg participou do filme `Action Hero`
- Nick Wahlberg participou do filme `Romantic Escape`

## Observacoes
- Esse tipo de tabela intermediaria eh chamado de `junction table` ou `bridge table`.
- Muito usado em relacionamentos `many-to-many`.
- Um ator pode participar de varios filmes.
- Um filme pode possuir varios atores.
- Multiplos `JOIN` sao extremamente comuns em bancos relacionais reais.