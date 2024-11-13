# GraphQL with FastAPI

This repository demonstrates the integration of **GraphQL** with **FastAPI**, a modern Python web framework, to create efficient and scalable APIs. The project combines GraphQL's flexibility with FastAPI's speed, showcasing best practices for setting up GraphQL endpoints, handling queries, mutations, and managing resolvers in a clean, Pythonic way.

## Features

- GraphQL integration with FastAPI for building robust APIs
- Docker setup for MySQL database for easy deployment and management
- Sample queries, mutations, and resolver functions
- Environment configurations and setup instructions

## Getting Started

### Prerequisites

- Python 3.10+
- Docker (for database setup)

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/bhargav2800/your-repo-name.git
    cd your-repo-name
    ```

2. **Install Requirements**

    Make sure you have `pip` installed, then install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. **Docker Setup for MySQL**

    This project includes a `docker-compose.yml` file for setting up a MySQL database. To start the MySQL container, run:

    ```bash
    docker-compose up -d
    ```

    This will spin up a MySQL instance, which you can configure in the FastAPI app.

### Running the FastAPI Server

After completing the setup steps, you can start the FastAPI server:

```bash
uvicorn main:app --reload
