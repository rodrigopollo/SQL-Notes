# SELECT — WHERE (filtrar linhas por condição)

### Exemplo de tabela

| NAME   | CHOICE |
|--------|--------|
| Zach   | Green  |
| David  | Green  |
| Claire | Yellow |
| David  | Red    |

---

### Comando
SELECT name, choice  
FROM table_1  
WHERE name = 'David';

---

### Resultado esperado

| NAME   | CHOICE |
|--------|--------|
| David  | Green  |
| David  | Red    |

---

### Explicação

O comando **WHERE** funciona como um filtro:  
Mostra **so as linhas que cumprem a condição**.
No exemplo acima, a condição é:

- name = 'David'

Ou seja, queremos **todas as linhas da coluna NAME onde o nome seja David**.

A tabela tem 4 entradas, mas **apenas 2** têm `name = 'David'`.  
Então o SQL retorna somente:

- David — Green  
- David — Red  

---

### Observações
- `WHERE` funciona parecido com um **if** da programação só entra quem for *True*.
- Igual que no IF tbm podemos usar os operadores:  
  `=`, `<`, `>`, `<=`, `>=`, `!=`
- WHERE aparece **sempre depois do FROM**.
