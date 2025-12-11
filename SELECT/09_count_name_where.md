# SELECT — COUNT WHERE (contar com condição)

### Exemplo de tabela

| NAME   | CHOICE | ID |
|--------|--------|----|
| Zach   | Green  | 25 |
| David  | Green  | 30 |
| Claire | Yellow | 35 |
| David  | Red    | 40 |

---

### Comando SQL
SELECT COUNT(name) FROM table_2  
WHERE id > 25 AND choice = 'Red';

---

### Resultado esperado
* 1

---

### Explicação
O comando acima conta **quantos nomes** atendem às condições definidas no `WHERE`.

Condições aplicadas:
- O valor de `ID` deve ser **maior que 25**, (> e nao >=)
- O valor de `CHOICE` deve ser **Red**

So **um registro** o unico que compre essas condiçoes foi o **David** (ID 40, Red).  
Por isso, o resultado é:
➡ **1**

---

### Observação

`COUNT(condição)` é muito utilizado quando queremos **quantificar resultados filtrados**,  
ou seja, **não contar tudo**, mas contar **somente o que atende aos critérios**.
