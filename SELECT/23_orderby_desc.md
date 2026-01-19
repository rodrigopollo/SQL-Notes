# ORDER BY — múltiplas colunas (DESC)

### Tabela:

| Company | Name   | Sales |
|--------|--------|-------|
| Apple  | Andew  | 100   |
| Google | David  | 500   |
| Apple  | Zach   | 300   |
| Google | Claire | 200   |
| Xerox  | Steven | 100   |

---

### Comando:
SELECT company, name, sales
FROM table_1
ORDER BY company DESC, sales DESC;

---

### Resultado esperado:

| Company | Name   | Sales |
|--------|--------|-------|
| Xerox  | Steven | 100   |
| Google | David  | 500   |
| Google | Claire | 200   |
| Apple  | Zach   | 300   |
| Apple  | Andew  | 100   |

---

### Anotações
Neste exemplo usamos **ORDER BY** com **duas colunas**:
- Primeiro o SQL vai ordenar todas as **company em ordem DESC**  
- Dentro de cada empresa (company), ele ordena os **sales em ordem DESC**

Ou seja, a ordem funciona em **camadas**:
1. Company, o primeiro comando de ORDER BY foi para ordenar COMPANY em ordem DESC.
DEPOIS
2. Sales, ele vai fazer a mesma coisa, mas sempre dando prioridade para COMPANY primeiro.

Também é possível combinar outras colunas e ordens:
- `ORDER BY company ASC, name ASC`
- `ORDER BY company DESC, name ASC`
- `ORDER BY sales DESC`

**Regra importante:**
- `ASC` → ordem crescente (A → Z, menor → maior)
- `DESC` → ordem decrescente (Z → A, maior → menor)
