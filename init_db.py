import sqlite3

# Conecta ao banco de dados (cria o arquivo se ele não existir)
connection = sqlite3.connect('database.db')

# Abre o arquivo schema.sql para ler o comando de criação da tabela
with open('schema.sql') as f:
    connection.executescript(f.read())

# Cria um "cursor" para executar comandos SQL
cur = connection.cursor()

# Insere duas tarefas iniciais para não começar com a lista vazia
cur.execute("INSERT INTO tasks (title, description) VALUES (?, ?)",
            ('Aprender SQLite', 'Entender como salvar dados em um banco de dados.')
            )

cur.execute("INSERT INTO tasks (title, description) VALUES (?, ?)",
            ('Alimentar o gato', 'Ele não pode ficar com fome!')
            )

# Salva as alterações (commit)
connection.commit()
# Fecha a conexão
connection.close()
