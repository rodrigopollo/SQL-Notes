# SELECT — WHERE (condições numéricas)

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
WHERE id > 30;

---

### Resultado esperado

| NAME   | CHOICE | ID |
|--------|--------|----|
| Claire | Yellow | 35 |
| David  | Red    | 40 |

---

### Anotações
Aqui o `WHERE` tem uma **condição numérica**.

O SQL faz o seguinte:
- Analisa a coluna `id`
- Seleciona **apenas as linhas** onde o valor do `id` é **maior que 30**

Por isso:
- `id = 25` → ignorado
- `id = 30` → ignorado
- `id = 35` → incluído
- `id = 40` → incluído

**Resumo:**
- `WHERE id > 30` → filtra valores **maiores que 30**
- `SELECT *` → retorna **todas as colunas** das linhas filtradas
- O resultado mostra **so as linhas que cumprem a condição**
