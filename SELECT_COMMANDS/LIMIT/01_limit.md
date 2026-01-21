# LIMIT — limitar quantidade de linhas retornadas

### Tabela:

| Company | Name   | Date       |
|--------|--------|------------|
| Oppo   | Steven | 07/09/2025 |
| Xioami | David  | 05/02/2025 |
| Huwai  | Claire | 23/07/2025 |
| Apple  | Zach   | 28/08/2025 |
| Apple  | Andew  | 30/05/2025 |

---

### Comando
SELECT *
FROM table_1
ORDER BY date DESC
LIMIT 3;

---

### Resultado esperado

| Company | Name   | Date       |
|---------|--------|------------|
| Oppo    | Steven | 07/09/2025 |
| Apple   | Zach   | 28/08/2025 |
| Huwai   | Claire | 23/07/2025 |

---

### Anotações
O **LIMIT** define **quantas linhas** o SQL deve mostrar depois de aplicar as regras estabelecidas
pelo usuario.

Fluxo do comando:
1. O SQL organiza os dados usando `ORDER BY`
2. Depois disso, aplica o `LIMIT`
3. Apenas os **Numeros de Linhas especificados** são mostradas

Exemplo com condição (**WHERE**):
NOTE: Amount(quantidade) nao existe na tabela, eh so um exemplo caso existisse

SELECT customer_id
FROM payment
WHERE amount > 0  
ORDER BY payment_date ASC
LIMIT 10;

Nesse caso:
- Primeiro o SQL **filtra** (`amount > 0`)
- Depois **ordena** por data
- Por fim **limita** o resultado para **10 linhas**

**Resumo:**
- `LIMIT 3` → retorna apenas 3 linhas
- Sempre pense no LIMIT como o **último passo** do SELECT
- Muito usado para:
  - Verificar top 10 (por ex) de dados e resultados
  - Paginação
  - Testes rápidos de consultas grandes
