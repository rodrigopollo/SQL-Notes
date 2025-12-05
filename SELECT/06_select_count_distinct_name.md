# SELECT — COUNT DISTINCT (contar valores únicos)

### Exemplo de tabela

| id | name   | choice |
|----|--------|--------|
| 1  | Zach   | Green  |
| 2  | David  | Green  |
| 3  | Claire | Yellow |
| 4  | David  | Red    |

---

### Comando
SELECT COUNT(DISTINCT name) FROM table_1;


### Resultado esperado
* 3

---

### Anotações

Como já vimos em **DISTINCT**, temos dois registros com o valor **"David"** na coluna `name`.  
O SQL **não identifica se é a mesma pessoa** ou pessoas diferentes — ele se importa apenas com 
o **valor repetido**.

Quando há repetição, **um registro é eliminado da contagem**.

Por isso:
- Existem **4 linhas** na tabela.
- Mas apenas **3 nomes diferentes** → Zach, David, Claire.

**Resumo:**
- `COUNT(name)` → conta todas as linhas onde existe nome.
- `COUNT(*)` → conta todas as linhas da tabela.
- `COUNT(DISTINCT name)` → conta apenas **valores únicos**, removendo os repetidos.
