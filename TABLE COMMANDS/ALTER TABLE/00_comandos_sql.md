## RESUMO RÁPIDO — Comandos SQL de Estrutura e Manipulação


### Query
```
+------------------+--------------------------------------------------+
| COMANDO          | SIGNIFICADO                                      |
+------------------+--------------------------------------------------+
| CREATE TABLE     | cria uma tabela                                  |
| SERIAL           | gera números automaticamente                     |
| PRIMARY KEY      | identificador único por linha                    |
| VARCHAR(50)      | texto com limite de caracteres                   |
| NOT NULL         | não permite valor vazio                          |
| UNIQUE           | não permite valores repetidos                    |
| TIMESTAMP        | armazena data e hora                             |
| INTEGER          | armazena números inteiros                        |
| REFERENCES       | cria relacionamento entre tabelas                |
| INSERT INTO      | insere dados na tabela                           |
| VALUES           | define os valores que serão inseridos            |
| UPDATE           | atualiza dados existentes                        |
| SET              | define novo valor em UPDATE                      |
| RETURNING        | mostra resultado após INSERT/UPDATE/DELETE       |
| DELETE FROM      | remove dados da tabela                           |
| ALTER TABLE      | modifica estrutura da tabela                     |
| ADD COLUMN       | adiciona nova coluna                             |
| DROP COLUMN      | remove uma coluna                                |
| SET DEFAULT      | define valor padrão para uma coluna              |
| DROP DEFAULT     | remove valor padrão de uma coluna                |
| SET NOT NULL     | obriga a coluna a ter valor                      |
| DROP NOT NULL    | permite que a coluna aceite valor vazio          |
| ADD CONSTRAINT   | adiciona regra ou restrição na tabela            |
| RENAME TO        | altera o nome de uma tabela                      |
| RENAME COLUMN TO | altera o nome de uma coluna                      |
| IF EXISTS        | executa o comando só se o objeto existir         |
| CASCADE          | remove coluna e tudo que depende dela            |
+------------------+--------------------------------------------------+
```

---

### Grupos por categoria
```
CRIAR ESTRUTURA:
  CREATE TABLE, SERIAL, PRIMARY KEY,
  VARCHAR, INTEGER, TIMESTAMP,
  NOT NULL, UNIQUE, REFERENCES

INSERIR DADOS:
  INSERT INTO, VALUES

ATUALIZAR DADOS:
  UPDATE, SET, RETURNING

REMOVER DADOS:
  DELETE FROM, RETURNING

MODIFICAR ESTRUTURA:
  ALTER TABLE, ADD COLUMN, DROP COLUMN,
  SET DEFAULT, DROP DEFAULT,
  SET NOT NULL, DROP NOT NULL,
  ADD CONSTRAINT, RENAME TO,
  RENAME COLUMN TO, IF EXISTS, CASCADE
```