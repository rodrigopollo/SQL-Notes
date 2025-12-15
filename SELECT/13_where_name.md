# SELECT — WHERE (filtrar uma linha específica)

### Exemplo de tabela (table_2)

| NAME   | CHOICE | ID |
|--------|--------|----|
| Zach   | Green  | 25 |
| David  | Green  | 30 |
| Claire | Yellow | 35 |
| David  | Red    | 40 |

---

### Comando
SELECT * FROM table_2  
WHERE name = 'Claire';

---

### Resultado esperado

| NAME   | CHOICE | ID |
|--------|--------|----|
| Claire | Yellow | 35 |

---

### Anotações
Neste exemplo:
- Estamos dizendo, selecione **todas as colunas** (`SELECT *`)
- Mas **apenas da linha** onde o valor de `name` seja **Claire**

Mesmo existindo várias linhas na tabela, **somente uma** tem **CLAIRE**.

**Resumo:**
- `SELECT *` → seleciona **todas as colunas**
- `WHERE name = 'Claire'` → filtra **apenas a linha desejada**
- O resultado mostra **uma linha completa**, já filtrada
