import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Função para se conectar ao banco de dados


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Isso nos permite acessar as colunas por nome
    return conn


@app.route('/')
def pagina_inicial():
    conn = get_db_connection()
    # Executa o SELECT e pega todas as tarefas do banco
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', tarefas=tasks)


@app.route('/adicionar', methods=['POST'])
def adicionar_tarefa():
    titulo = request.form['title']
    descricao = request.form['description']

    conn = get_db_connection()
    # Executa o INSERT para adicionar a nova tarefa no banco
    conn.execute('INSERT INTO tasks (title, description) VALUES (?, ?)',
                 (titulo, descricao))
    conn.commit()
    conn.close()
    return redirect(url_for('pagina_inicial'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
