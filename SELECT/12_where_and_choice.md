# SELECT — WHERE com AND (filtrar registros específicos)

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
WHERE name = 'David' AND choice = 'Red';

---

### Resultado esperado

| NAME  | CHOICE |
|-------|--------|
| David | Red    |

---

### Anotações
O comando `WHERE` é usado para **filtrar linhas** com condições.
Neste exemplo, estamos dizendo:

- Mostre apenas os registros que:
  - `name` seja **David**
  - **E** (`AND`) `choice` seja **Red**

Mesmo existindo **dois registros com o nome David**, apenas **um** atende às duas condições.
**Resumo:**
- `WHERE` → filtra registros
- `AND` → todas as condições devem ser verdadeiras
- Apenas linhas que cumprem **todas as regras** aparecem no resultado
