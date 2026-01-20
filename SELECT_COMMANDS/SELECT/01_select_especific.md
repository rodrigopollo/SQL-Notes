# SELECT — Selecionar colunas específicas

### Exemplo de tabelas
| c1 | c2 | c3 |
|----|----|----|
| x  | 23 | a  |
| y  | 18 | b  |
| z  | 46 | c  |

### Selecionando colunas específicas
SELECT c1, c3 FROM table_1;



### Resultado esperado
 ----------------
|  c1     c3     |
 ----------------
|   x      a     |
|   y      b     |
|   z      c     |
 ----------------

### Anotações
- Selecione toda a coluna c1 → resultado: x, y, z
- Selecione toda a coluna c3 → resultado: a, b, c


