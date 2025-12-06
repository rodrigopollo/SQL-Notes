# SELECT — COUNT DISTINCT (contar valores únicos em uma coluna)

### Exemplo de tabela

| id | name   | choice |
|----|--------|--------|
| 1  | Zach   | Green  |
| 2  | David  | Green  |
| 3  | Claire | Yellow |
| 4  | David  | Red    |

---

### Contando valores únicos na coluna `choice`
SELECT COUNT(DISTINCT choice) FROM table_1;


### Resultado esperado
* 3

---

### Anotações
A lógica é a mesma do exemplo anterior com `name`, mas agora aplicada na coluna `choice`.  
Como existem dois registros com o valor **Green**, o comando `DISTINCT` mantém apenas um deles para a contagem.

Por isso, o resultado é **3**, pois só existem três valores diferentes:

- Green  
- Yellow  
- Red  

**Resumo:**
- `COUNT(choice)` → conta 4 linhas com valores na coluna choice.  
- `COUNT(DISTINCT choice)` → conta apenas valores diferentes (resultado = 3).
