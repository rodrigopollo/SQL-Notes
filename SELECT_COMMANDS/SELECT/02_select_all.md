# SELECT ALL — Selecionar todas as colunas

## Exemplo de tabelas no banco de dados

### Table 1
| c1 | c2 | c3 |
|----|----|----|
| x  | 23 | a  |
| y  | 18 | b  |
| z  | 46 | c  |

### Table 2
| c1 | c2 | c3 |
|----|----|----|
| 1  | Q  | 13 |
| 2  | Q  | 34 |
| 3  | S  | 56 |

### Table 3
| c1 | c2 | c3 |
|----|----|----|
| c  | 0  | 12 |
| b  | 0  | 24 |
| a  | 0  | 45 |

------

## SELECT *

### Forma padrão
SELECT * FROM table_1;

------

### Resultado esperado
| c1 | c2 | c3 |
|----|----|----|
| x  | 23 | a  |
| y  | 18 | b  |
| z  | 46 | c  |

---

### Anotações
- O `*` significa ALL → seleciona **todas** as colunas da tabela.
- O SELECT * retorna os dados exatamente como estão armazenados na tabela.
