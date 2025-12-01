# SELECT DISTINCT — Valores únicos na coluna CHOICE

## Exemplo de tabelas no banco de dados

### Table 1
| NAME   | CHOICE |
|--------|--------|
| Zach   | Green  |
| David  | Green  |
| Claire | Yellow |
| David  | Red    |

---

## Comando SQL
SELECT DISTINCT choice FROM table_1;

---

## Resultado esperado
- Green
- Yellow
- Red

---

## Explicação
Como podemos ver na tabela, a palavra **Green** aparece 2 vezes.  
O comando `DISTINCT` pega apenas **valores únicos**, então ele não repete o mesmo valor.

---

## Observação importante
Usamos `DISTINCT` quando queremos ver **apenas os valores diferentes**, ignorando repetições.

Exemplo:
Se fosse uma tabela de filmes onde vários filmes foram lançados em 2006,  
para descobrir **todos os anos de lançamento diferentes**, usaríamos:

> SELECT DISTINCT ano FROM filmes;
