# Authentication API with Flask and PostgreSQL

This is a simple RESTful API built with Flask and PostgreSQL for user management.

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
2. Install dependencies:
  ```bash
  pip install -r requirements.txt
```
3. Set up PostgreSQL and create a database called authentication
4. Endpoints

    GET /users — Get all users

    GET /users/{id} — Get a user by ID

    POST /users — Create a new user

    DELETE /users/{id} — Delete a user by ID

