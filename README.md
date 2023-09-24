# Simple JWT on FastAPI

This is a simple FastAPI project that demonstrates how to implement JWT (JSON Web Tokens) authentication for secure routes using [jwtsign](https://github.com/yourusername/jwtsign) for token generation and [jwtvalidate](https://github.com/yourusername/jwtvalidate) for token validation.

## Getting Started

### Prerequisites

Before you begin, ensure you have Python installed on your system. You'll also need to install FastAPI and the required dependencies.

```bash
pip install fastapi pydantic jwtsign jwtvalidate
```

### Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/chuck1z/fastapijwt.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-fastapi-jwt-project
   ```

3. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

4. Access the FastAPI interactive documentation at `http://localhost:8000/docs` to test the API endpoints.

### API Endpoints

- `POST /secure`: A secure route that requires a valid JWT token for access. You can obtain a token by signing in or signing up.

- `POST /generate-token`: Generates a JWT token for a given `user_id`.

- `POST /signup`: Registers a new user and returns a JWT token upon successful registration.

- `POST /signin`: Signs in an existing user and returns a JWT token upon successful authentication.

### Example Usage

To generate a JWT token for a user:

```http
POST /generate-token

{
  "user_id": "your_user_id"
}
```

To sign up a new user:

```http
POST /signup

{
  "name": "Your Name",
  "email": "your@email.com",
  "password": "your_password"
}
```

To sign in:

```http
POST /signin

{
  "email": "your@email.com",
  "password": "your_password"
}
```

### Dependencies

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance) web framework for building APIs with Python 3.6+.

- [Pydantic](https://pydantic-docs.helpmanual.io/): Data validation and parsing using Python type hints.

- [jwtsign](https://github.com/yourusername/jwtsign): A library for JWT token generation.

- [jwtvalidate](https://github.com/yourusername/jwtvalidate): A library for JWT token validation.
