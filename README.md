# Football Teams API

This is a simple API to manage football teams, built with FastAPI and SQLAlchemy.

## Features

- Add, view, update, and delete football teams
- Uses SQLite as the database

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/tu_usuario/football-teams-api.git
    cd football-teams-api
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    uvicorn main:app --reload
    ```

## Endpoints

- **GET /teams**: Retrieve all teams
- **GET /teams/{id}**: Retrieve a specific team by ID
- **POST /teams**: Create a new team
- **PUT /teams/{id}**: Update a team by ID
- **DELETE /teams/{id}**: Delete a team by ID

## Project Structure

```bash
├── config/
│   └── database.py   # Database connection settings
├── models/
│   └── team_model.py # SQLAlchemy model for Football Team
├── routers/
│   └── team_router.py # API routes for Football Team
├── schemas/
│   └── team_schema.py # Pydantic schemas for Football Team
├── services/
│   └── team_service.py # Service layer for handling logic
├── main.py           # FastAPI entry point
└── requirements.txt  # List of dependencies
