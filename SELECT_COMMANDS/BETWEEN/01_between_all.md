# WHERE BETWEEN — Intervalo de Valores Numéricos

## 📌 Conceito:
As duas condições abaixo fazem **exatamente a mesma coisa**:

- `WHERE valor >= 5 AND valor <= 10`
- `WHERE valor BETWEEN 5 AND 10`

O comando **BETWEEN** mostra oq esta **Do primeiro valor ate o Ultimo valor** inserido.

---

## 📋 Tabela usada no exemplo:

| Company | Name   | Sales |
|--------|--------|-------|
| Xerox  | Steven | 100   |
| Google | David  | 550   |
| Google | Claire | 200   |
| Apple  | Zach   | 250   |
| Apple  | Andew  | 350   |

---

## 🧠 Comando SQL:
SELECT *  
FROM table_1  
WHERE sales BETWEEN 250 AND 550;

---

## Resultado Esperado:

| Company | Name   | Sales |
|--------|--------|-------|
| Google | David  | 550   |
| Apple  | Zach   | 250   |
| Apple  | Andew  | 350   |

---

## 📝 Observações Importantes
- O **BETWEEN eh inclusivo**, ou seja:
  - O valor **250 entra**
  - O valor **550 entra**
- O resultado contém **3 linhas**
- Se fosse usado:
  
  SELECT COUNT(*)  
  FROM table_1  
  WHERE sales BETWEEN 250 AND 550;

  👉 O resultado seria **3**

---

## 📌 Resumo rápido
- `BETWEEN` = intervalo **de A ate C**
- Inclui os valores **A** e **B** ou seja A, B e C seriam mostrados.
- Eh mais facil de usar e ler do que `>= AND <=`
