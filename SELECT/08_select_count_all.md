# SELECT COUNT(*) — Contar todas as linhas da tabela

### Exemplo de tabela

| NAME   | CHOICE |
|--------|--------|
| Zach   | Green  |
| David  | Green  |
| Claire | Yellow |
| David  | Red    |

---

## Comando SQL
SELECT COUNT(*) FROM table_1;

---

## Resultado esperado
* 4

---

## Anotaçoes
O comando `COUNT(*)` conta **todas as linhas** da tabela, independente da coluna ou do conteúdo.

Comando muito util em **tabelas grandes**, onde não eh possível visualizar manualmente quantos
registros existem.  
Pensa em uma tabela com 15.000 linhas, seria inviavel contar uma a uma.

Com `COUNT(*)`, o SQL faz isso por voce e te retorna o total de registros.

---

## Observação importante
Vc tbm pode usar o nome de uma coluna (ex.: `COUNT(name)`), o uso de `COUNT(*)` é considerado:

- **mais claro**
- **mais direto**
- **mais comum**

Eh um comando que a gente vai usar quando quiser contar **todas as linhas da tabela**.
