# INNER JOIN + WHERE (Filtro por Localizacao)

## Tabela: address
---------------------------------------------------
| address_id | address         | district   |
---------------------------------------------------
| 101        | Main Street 10  | California |
| 102        | Green Road 55   | Texas      |
| 103        | Yellow Ave 99   | California |
| 104        | Blue Street 77  | Florida    |
---------------------------------------------------

## Tabela: customer
---------------------------------------------------------------------------
| customer_id | first_name | last_name | email              | address_id |
---------------------------------------------------------------------------
| 1           | Steven     | Cole      | steven@example.com | 101        |
| 2           | Claire     | Reed      | claire@example.com | 102        |
| 3           | David      | Hunt      | david@example.com  | 103        |
| 4           | Zach       | Stone     | zach@example.com   | 104        |
---------------------------------------------------------------------------

## Comando SQL
SELECT
    a.district,
    c.first_name,
    c.last_name,
    c.email
FROM customer AS c
JOIN address AS a
    ON c.address_id = a.address_id
WHERE a.district = 'California';


## Resultado Esperado
---------------------------------------------------------------
| district   | first_name | last_name | email              |
---------------------------------------------------------------
| California | Steven     | Cole      | steven@example.com |
| California | David      | Hunt      | david@example.com  |
---------------------------------------------------------------

## Explicacao

O `JOIN` conecta as tabelas `customer` e `address` usando o campo `address_id`.

O `WHERE` filtra os registros quando  -->  a.district = 'California'

Resultado:
- Steven mora em California
- David mora em California
- Claire e Zach sao removidos porque pertencem a outros distritos

## Observacoes
- `JOIN` = `INNER JOIN`.
- `WHERE` se utiliza para filtrar os resultados depois do `JOIN`.
- Esse tipo de consulta eh muito comum para localizar clientes por cidade, estado ou pais.
- Alias (`c` e `a`) ajudam a deixar a query mais limpa e facil de ler.