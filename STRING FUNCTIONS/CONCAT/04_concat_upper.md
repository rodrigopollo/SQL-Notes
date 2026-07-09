## CONCAT() — Como formatar um identificador com nome completo em maiúsculas e código?

**Tabela utilizada:** `customer`
```
+-------------+------------+-----------+
| customer_id | first_name | last_name |
+-------------+------------+-----------+
|           1 | Ana        | Souza     |
|           2 | Bruno      | Lima      |
|           3 | Carla      | Mendes    |
|           4 | Daniel     | Rocha     |
|           5 | Elisa      | Cunha     |
|           6 | Fernando   | Alves     |
|           7 | Gabriela   | Nunes     |
|           8 | Henrique   | Pinto     |
+-------------+------------+-----------+
```


### Query
```sql
SELECT
    CONCAT(
        UPPER(first_name),
        ' ',
        UPPER(last_name),
        ' - ',
        'Código: ',
        customer_id
    ) AS identificador
FROM customer;
```


### Resultado
```
+-----------------------------+
| identificador               |
+-----------------------------+
| ANA SOUZA - Código: 1       |
| BRUNO LIMA - Código: 2      |
| CARLA MENDES - Código: 3    |
| DANIEL ROCHA - Código: 4    |
| ELISA CUNHA - Código: 5     |
| FERNANDO ALVES - Código: 6  |
| GABRIELA NUNES - Código: 7  |
| HENRIQUE PINTO - Código: 8  |
+-----------------------------+
```

---

Este exercício combina três recursos em uma única expressão `CONCAT()`: `UPPER()` para padronizar a 
capitalização, textos fixos para formatar a estrutura visual, e uma coluna numérica (`customer_id`) 
concatenada diretamente como texto. O resultado é um identificador único por cliente, legível e padronizado
útil para geração de etiquetas, relatórios de exportação, mensagens automáticas ou qualquer situação onde
os dados precisam ser apresentados em um formato fixo e reconhecível.


### O que cada parte faz

- `UPPER(first_name)` — **novo:** `UPPER()` é o oposto de `LOWER()` — converte todos os caracteres de um texto
para letras maiúsculas. Aqui garante que o primeiro nome apareça em caixa alta independentemente de como está
armazenado na tabela.
- `' '` — espaço em branco fixo entre o primeiro nome e o sobrenome.
- `UPPER(last_name)` — sobrenome convertido para maiúsculas pelo mesmo motivo.
- `' - '` — separador fixo entre o nome completo e o código, com espaços em ambos os lados para melhor legibilidade.
- `'Código: '` — texto fixo que aparece igual em todas as linhas, identificando o que vem a seguir.
- `customer_id` — coluna numérica da tabela, concatenada diretamente ao texto. O `CONCAT()` no PostgreSQL 
converte automaticamente números para texto ao concatená-los com strings, sem necessidade de `CAST()`.
- `AS identificador` — apelido para nomear a coluna resultante.
- `FROM customer` — define a tabela de origem dos dados.


### Como o CONCAT monta cada linha
```
UPPER('Ana')  +  ' '  +  UPPER('Souza')  +  ' - '  +  'Código: '  +  1
→  'ANA'      +  ' '  +  'SOUZA'         +  ' - '  +  'Código: '  +  '1'
→  'ANA SOUZA - Código: 1'
```