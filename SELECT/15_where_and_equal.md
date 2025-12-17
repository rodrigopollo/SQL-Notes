# WHERE + AND — Filtro DUPLO (<=, =)

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
WHERE id <= 30
  AND choice = 'Green';

---

## RESULTADO ESPERADO

| ID | NAME  | CHOICE |
|----|-------|--------|
| 25 | Zach  | Green  |
| 30 | David | Green  |

---

## EXPLICAÇÃO
Condições aplicadas:
- `id <= 30` → seleciona IDs **25 e 30**
- `choice = 'Green'` → seleciona apenas quem escolheu **Green**

Analisando linha por linha:
- Zach (25, Green) -> passa nas duas condições = TRUE
- David (30, Green) -> passa nas duas condições = TRUE
- Claire (35, Yellow) -> ID maior que 30 mas a cor eh diferente = FALSE
- David (40, Red) -> ID maior que 30 mas a cor eh diferente = FALSE

---

## OBSERVAÇÕES
- `<=` significa **menor ou igual**
- `AND` torna o filtro mais restritivo

