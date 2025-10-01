-- Apaga a tabela se ela já existir, para podermos rodar o script várias vezes
DROP TABLE IF EXISTS tasks;

-- Cria a nossa tabela de tarefas
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    description TEXT NOT NULL
);