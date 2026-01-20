# WHERE + AND — Filtro TRIPLO (>, <, =)

## TABELA USADA (table_2)

| ID | NAME   | CHOICE |
|----|--------|--------|
| 25 | Zach   | Green  |
| 30 | David  | Green  |
| 35 | Claire | Yellow |
| 40 | David  | Red    |

---

## COMANDO SQL

SELECT *
FROM table_2
WHERE id >= 30
  AND choice = 'Green'
  AND name = 'David';

---

## RESULTADO ESPERADO

| ID | NAME  | CHOICE |
|----|-------|--------|
| 30 | David | Green  |

---

## EXPLICAÇÃO
Este exemplo utiliza **TRÊS filtros ao mesmo tempo**, unidos pelo **AND**.

Condiçoes:
- `id >= 30` → aceita IDs **30 ou maiores**
- `choice = 'Green'` → so registros com escolha **Green**
- `name = 'David'` → so registros com nome **David**

Linha por linha:
- Zach (25, Green) -> ID menor que 30 = FALSE
- David (30, Green) -> passa em TODAS as condições = TRUE
- Claire (35, Yellow) -> nome e escolha diferentes = FALSE
- David (40, Red) -> escolha diferente = FASE

Como **AND exige que todas as condições sejam verdadeiras**, so **uma linha** eh correta (David Green).

---

##  OBSERVAÇÕES IMPORTANTES
- `AND` eh cumulativo: **todas** as condições precisam ser verdadeiras
- Se fosse usado `>` em vez de `>=`, **nenhuma linha seria mostrada**

