# SELECT — COUNT (contar linhas)

### Exemplo de tabela

| id | name   | choice |
|----|--------|--------|
| 1  | Zach   | Green  |
| 2  | David  | Green  |
| 3  | Claire | Yellow |
| 4  | David  | Red    |

---

### Comando:
SELECT COUNT(name) FROM table_1;

### Resultado esperado
* 4

---

### Anotações

Com esse comando você está pedindo para o programa dizer **quantas linhas existem na coluna `name`** 
da tabela `table_1`.
Como a tabela é pequena e tem apenas 4 linhas, se você trocar:

- `COUNT(name)` por `COUNT(choice)`
- ou usar `COUNT(*)`

o resultado **vai continuar sendo 4**, porque a tabela tem 4 linhas no total.

**Resumo:**

- `COUNT(name)` → conta quantas linhas têm valor na coluna `name`
- `COUNT(choice)` → conta quantas linhas têm valor na coluna `choice`
- `COUNT(*)` → conta **todas** as linhas da tabela (independente da coluna)
