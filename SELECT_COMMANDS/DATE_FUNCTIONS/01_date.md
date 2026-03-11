# DATE() — extrair apenas a data (removendo o horario)

## Tabela:
| company | name   | payment_date       |
|---------|--------|--------------------|
| Oppo    | Steven | 2025-09-07 08:15   |
| Xioami  | David  | 2025-02-05 14:45   |
| Huwai   | Claire | 2025-07-23 09:30   |
| Apple   | Zach   | 2025-08-28 18:10   |
| Apple   | Andew  | 2025-05-30 23:55   |
| Oppo    | Steven | 2025-09-07 21:40   |
| Huwai   | Claire | 2025-07-23 22:05   |

## Comando SQL:
SELECT 
    company, 
    name, 
    DATE(payment_date) AS payment_date
FROM table_1;

## Resultado Esperado:
| company | name   | payment_date |
|---------|--------|--------------|
| Oppo    | Steven | 2025-09-07   |
| Xioami  | David  | 2025-02-05   |
| Huwai   | Claire | 2025-07-23   |
| Apple   | Zach   | 2025-08-28   |
| Apple   | Andew  | 2025-05-30   |
| Oppo    | Steven | 2025-09-07   |
| Huwai   | Claire | 2025-07-23   |

---

## Explicacao:
- `DATE(payment_date)` extrai apenas a parte da data (um valor datetime).
- A parte do horario (hora e minuto) eh removida.
- O valor original permanece no banco sem alteraçoes, so o resultado mostrado eh alterado.
- Entao vai ser mostrado a data normalmente mas sem os horarios, eh um filtro do q quer ver.

## Observacoes:
- `DATE()` eh usado quando precisamos trabalhar so a data e ignorar o horario.
- NOTE PROFESSOR: Muito comum em relatorios diarios e analises por dia.
- A coluna original continua sendo do tipo datetime; a funcao apenas formata o resultado.