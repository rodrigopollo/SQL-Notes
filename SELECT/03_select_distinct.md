# SELECT DISTINCT — Selecionar valores únicos

## Comando
SELECT DISTINCT (name) FROM table_1;

Como podemos ver no banco de dados, o nome **David** aparece mais de uma vez.
Sendo assim, esse comando vai selecionar **somente os nomes diferentes**.


## EXEMPLO: SELECT DISTINCT (name) FROM table_1

### Database — Table 1
| NAME   | Choice |
|--------|--------|
| Zach   | Green  |
| David  | Green  |
| Claire | Yellow |
| David  | Red    |

----------

### Resultado esperado
A lista com os nomes únicos será:

- Zach
- David
- Claire

---------

### Observação importante
O comando `DISTINCT` filtra valores repetidos, mas **não identifica se são pessoas diferentes ou a mesma pessoa alterando sua escolha**.

Ou seja:
- O primeiro **David** (que escolheu **Green**)
- e o segundo **David** (que escolheu **Red**)  
→ **podem ser a mesma pessoa ou pessoas diferentes, e o banco não tem como saber apenas pelo nome.**
