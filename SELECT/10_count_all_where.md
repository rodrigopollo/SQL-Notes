# COUNT WHERE — Mostra quantas linhas cumprem com determinadas condições

-------------------------------------
| NAME   | CHOICE | ID              |
|--------|--------|-----------------|
| Zach   | Green  | 25              |
| David  | Green  | 30              |
| Claire | Yellow | 35              |
| David  | Red    | 40              |
-------------------------------------


# COMANDO SQL
SELECT COUNT(*) FROM table_2 
WHERE id > 35 OR choice = 'Green';

# RESULTADO ESPERADO
3

# EXPLICAÇÃO
O resultado eh 3 pq:
- 2 registros tem CHOICE = 'Green';
- 1 registro tem ID > 35
Como foi utilizado o operador OR, basta que uma das condições seja verdadeira para que a linha
seja contabilizada.

# OBSERVAÇÕES
COUNT(*) conta todas as linhas que cumprem as condiçoes, incluido os valores repetidos.
