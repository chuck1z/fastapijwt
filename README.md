# Simple JWT on FastAPI

This is a simple FastAPI project that demonstrates how to implement JWT (JSON Web Tokens) authentication for secure routes using [jwtsign](https://github.com/yourusername/jwtsign) for token generation and [jwtvalidate](https://github.com/yourusername/jwtvalidate) for token validation.

## Getting Started

### Prerequisites

Before you begin, ensure you have Python installed on your system.

### Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/chuck1z/fastapijwt.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-fastapi-jwt-project
   ```

3. Install the required dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

5. Access the FastAPI interactive documentation at `http://localhost:8000/docs` to test the API endpoints.

### API Endpoints

- `POST /signup`: Registers a new user and returns a JWT token upon successful registration.

- `POST /signin`: Signs in an existing user and returns a JWT token upon successful authentication.

- `POST /authtest`: Decode the token given from /signup or /signin

### Example Usage

Sign Up

```bash
curl --request POST \
  --url http://localhost:8000/signup \
  --header 'content-type: application/json' \
  --data '{"name": "example_name", "email": "example@email.com", "password": "password123"}'
```

Sign In

```bash
curl --request POST \
  --url http://localhost:8000/signin \
  --header 'content-type: application/json' \
  --data '{"email": "example@email.com", "password": "password123"}'
```

Auth Test

```bash
curl --request POST \
  --url http://localhost:8000/authtest?token={your_jwt_token} \
  --header 'content-type: application/json'
```

### Dependencies

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance) web framework for building APIs with Python 3.6+.

- [Pydantic](https://pydantic-docs.helpmanual.io/): Data validation and parsing using Python type hints.

- [jwtsign](https://github.com/yourusername/jwtsign): A library for JWT token generation.

- [jwtvalidate](https://github.com/yourusername/jwtvalidate): A library for JWT token validation.
