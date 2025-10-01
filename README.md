# To-Do List com Flask e Docker 📝🐳

Este é um projeto de estudo para criar uma aplicação de lista de tarefas (To-Do List) simples, utilizando Python com o framework Flask para o back-end e Docker para a containerização.

O objetivo principal é servir como uma ferramenta de ensino para conceitos de desenvolvimento web, persistência de dados com SQLite e o fluxo de trabalho com Docker e Git/GitHub.

---

### ✨ Tecnologias Utilizadas

* **Back-end:** Python
* **Framework:** Flask
* **Banco de Dados:** SQLite
* **Containerização:** Docker
* **Controle de Versão:** Git & GitHub

---

### 🚀 Funcionalidades Atuais

* Visualização de tarefas existentes.
* Adição de novas tarefas através de um formulário.
* Persistência de dados em um banco de dados SQLite.

---

### ⚙️ Como Rodar o Projeto Localmente

Para executar este projeto, você precisará ter o **Git** e o **Docker Desktop** instalados em sua máquina.

1.  **Clone o repositório:**
    ```bash
    git clone (https://github.com/isadora-laviola/todo-list-flask-docker.git)
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd todo-list-flask-docker
    ```

3.  **Construa a imagem Docker:**
    Este comando lê o `Dockerfile` e cria a imagem da nossa aplicação.
    ```bash
    docker build -t todo-app .
    ```

4.  **Inicie o contêiner Docker:**
    Este comando inicia a aplicação a partir da imagem que acabamos de construir.
    ```bash
    docker run -p 5000:5000 todo-app
    ```

    * **Para desenvolvimento (com auto-reload):** Se você pretende alterar o código, use o comando abaixo. Ele cria um "volume" que espelha o código do seu computador para dentro do contêiner, aplicando as alterações instantaneamente.
        ```bash
        docker run -p 5000:5000 -v .:/app todo-app
        ```

5.  **Acesse a aplicação:**
    Abra seu navegador e visite `http://localhost:5000`.

---

### 🔜 Próximos Passos

Este projeto está em evolução! As próximas funcionalidades planejadas são:
* [ ] Implementar a funcionalidade de **deletar** uma tarefa.
* [ ] Implementar a funcionalidade de **editar** uma tarefa.
* [ ] Melhorar o estilo da página com CSS.