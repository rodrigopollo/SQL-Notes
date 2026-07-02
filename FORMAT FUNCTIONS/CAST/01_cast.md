## CAST() — Como converter o tipo de uma coluna para texto?

**Tabela utilizada:** `payments`

```
+------------+---------------------+--------+
| payment_id | payment_date        | amount |
+------------+---------------------+--------+
|          1 | 2025-01-15 10:30:00 |  10.00 |
|          2 | 2025-03-22 18:45:00 |  20.00 |
|          3 | 2025-07-05 09:00:00 |  30.00 |
|          4 | 2025-09-10 14:20:00 |  40.00 |
|          5 | 2026-02-01 12:10:00 |  50.00 |
+------------+---------------------+--------+
```

> **Conceito novo neste exercício:** `CAST()` para converter um valor de um tipo de dado para outro, e uma armadilha importante do tipo `CHAR` no PostgreSQL quando o tamanho não é especificado.

---

### Query

```sql
SELECT
    payment_id,
    CAST(payment_date AS CHAR) AS date_as_text
FROM payments;
```

### Resultado

```
+------------+--------------+
| payment_id | date_as_text |
+------------+--------------+
|          1 | 2            |
|          2 | 2            |
|          3 | 2            |
|          4 | 2            |
|          5 | 2            |
+------------+--------------+
```

---

`CAST()` é o jeito padrão do SQL de mudar o tipo de um valor, funcionando de forma parecida na maioria dos
bancos de dados — diferente de `TO_CHAR`, `TO_DATE` e `TO_NUMBER`, que são funções de formatação específicas
do PostgreSQL com mais controle sobre a máscara de exibição. A grande lição prática deste exercício é que 
tipos com tamanho fixo (`CHAR`) exigem atenção redobrada no PostgreSQL: omitir o tamanho não significa "sem
limite" como muitos esperariam vindo de outros bancos — significa `CHAR(1)`. Por isso, na prática profissional,
é mais seguro usar `VARCHAR` ou `TEXT` quando o tamanho final não é conhecido de antemão, reservando 
`CHAR(n)` apenas para casos onde o tamanho é realmente fixo e conhecido (como códigos de UF com 2 letras,
por exemplo).


### O que cada parte faz

- `payment_id` — coluna trazida diretamente da tabela, sem nenhuma transformação.
- `CAST(payment_date AS CHAR) AS date_as_text` — **novo:** `CAST()` é o comando padrão do SQL (reconhecido 
por praticamente todos os bancos de dados, diferente de `TO_CHAR`/`TO_DATE`/`TO_NUMBER`, que são funções 
específicas do PostgreSQL/Oracle) para converter um valor de um tipo para outro. A sintaxe geral é 
`CAST(valor AS tipo_de_dado)`.
- `FROM payments` — define a tabela de origem dos dados.

> ⚠️ **Armadilha do `CHAR` sem tamanho no PostgreSQL:** quando `CHAR` é usado sem informar um tamanho
entre parênteses, o PostgreSQL assume automaticamente **`CHAR(1)`** — ou seja, apenas 1 caractere. A conversão
acontece em duas etapas silenciosas: primeiro `payment_date` vira o texto completo (`'2025-01-15 10:30:00'`),
depois esse texto é truncado para apenas 1 caractere. Como o `CAST` explícito trunca sem gerar erro, a query
roda normalmente e devolve um resultado incorretamente curto, sem nenhum aviso.


| Tipo usado sem tamanho             | Comportamento no PostgreSQL                                                              |
|------------------------------------|------------------------------------------------------------------------------------------|
| `CHAR` (ou `CHARACTER`)            | assume `CHAR(1)` — trunca para 1 caractere                                               |
| `VARCHAR` (ou `CHARACTER VARYING`) | sem limite — mantém a string inteira                                                     |
| `TEXT`                             | sem limite — mantém a string inteira (tipo específico do PostgreSQL, fora do padrão SQL) |

> Para obter o resultado pretendido neste exercício (a data completa como texto), o correto seria 
`CAST(payment_date AS TEXT)` ou `CAST(payment_date AS CHAR(19))`, informando o tamanho exato esperado.


### Outras formas de usar CAST() (referência rápida)

| Conversão       | Exemplo                      | Resultado real no PostgreSQL                                                                                       |
|-----------------|------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Texto → Data    | `CAST('2025-09-29' AS DATE)` | `2025-09-29` — funciona normalmente                                                                                |
| Número → Texto  | `CAST(123 AS CHAR)`          | ⚠️ `'1'` — mesma armadilha do `CHAR(1)`. Para o número completo, use `CAST(123 AS CHAR(3))` ou `CAST(123 AS TEXT)` |
| Texto → Decimal | `CAST('123.45' AS DECIMAL)`  | `123.45` — funciona normalmente, pois `DECIMAL` sem precisão/escala definida não trunca                            |


**Comparação rápida — `CHAR` vs `TEXT`:**

```sql
CAST(payment_date AS CHAR) → '2'                    -- truncado para 1 caractere
CAST(payment_date AS TEXT) → '2025-01-15 10:30:00'  -- string completa, sem truncar
```


