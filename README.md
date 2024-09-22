# 🛠️ Event and Ticket Management System

## 🎯 Project Objective
The goal is to submit a GitHub repository that follows best practices and coding standards. This includes:
- Setting up a **MySQL** database using **Docker Compose**.
- Implementing full CRUD functionality for entities such as **Event** and **Ticket**.
- Ensuring code quality with **Pylint** and achieving a score greater than **7**.

## 🧰 Technologies Used
- **FastAPI**: Python web framework for building APIs.
- **MySQL**: Relational database for data storage.
- **Docker & Docker Compose**: Container orchestration for setting up services.
- **Pylint**: Static code analysis tool for Python.
- **PEP8**: Python style guide for writing clean code.

---

## ⚙️ Project Setup

### ✅ Prerequisites
Make sure you have the following installed:
- **🐳 Docker** (v20.x or higher)
- **🐳 Docker Compose** (v2.x or higher)
- **🐍 Python** (v3.8 or higher)
- **Pylint** (v2.x or higher)

### 🚀 1. Running Docker (Database Setup)

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/ImplementacionPylintBlack.git
    cd ImplementacionPylintBlack
    ```

2. Build and run the Docker containers (MySQL & Adminer):
    ```bash
    docker-compose up --build
    ```

3. Verify that the database is running:
   - Access **Adminer** at [http://localhost:8080](http://localhost:8080).
   - Use the credentials from the `.env` file or the default ones below:
     - **System**: MySQL
     - **Server**: db
     - **User**: root
     - **Password**: root
     - **Database**: pylintPep8

---

### ⚡ 2. Running FastAPI with Uvicorn

1. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

3. Open the API docs in your browser to test the endpoints:
    - API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 🧪 3. Running Pylint for Code Quality

The project is configured with a `.pylintrc` file to set custom rules. To run Pylint and check the code quality:

1. Run Pylint on the project:
    ```bash
    pylint app/
    ```

2. Ensure the score is **above 7** for successful project submission.

---

## 📂 Project Structure

- **`/services/`**: Contains business logic (CRUD operations) for events and tickets.
- **`/routes/`**: Defines API routes for entity operations.
- **Entities**:
  - **🎫 Ticket**: `id`, `evento_id` (FK), `usuario_id` (FK), `fecha_compra`
  - **📅 Evento**: `id`, `nombre`, `fecha`, `ubicacion`

---

## 🎨 PEP8 Compliance & Code Formatting

To ensure the code follows **PEP8** standards, the project uses **Black** for auto-formatting:

1. Install **Black**:
    ```bash
    pip install black
    ```

2. Format the code:
    ```bash
    black .
    ```
---

## 🏗️ Docker Compose Configuration

The project uses a `docker-compose.yml` file to set up the MySQL database and Adminer. Make sure to configure the `.env` file with your database credentials before running the containers.

---
**Presented By: Brahyam Hurtado Quiceno and Santiago Parra**
