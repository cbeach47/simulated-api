# simulated-api
FastAPI server that simulates various APIs for testing

## Features

- FastAPI-based API server
- Authentication middleware checking Authorization header
- `/user-details/{ID}` endpoint for retrieving user details
- Configurable static token authentication
- Runs on port 8050

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

### Install dependencies

```bash
uv sync
```

### Configuration

Set the `AUTH_TOKEN` environment variable to configure the static authentication token:

```bash
export AUTH_TOKEN=your_secret_token_here
```

Or copy `.env.example` to `.env` and modify the token:

```bash
cp .env.example .env
# Edit .env with your token
```

## Running the Application

### Using uv

```bash
uv run python main.py
```

### Using uvicorn directly

```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8050
```

## Usage

### Authentication

All requests require an `Authorization` header with the configured token:

```bash
# Using Bearer token format
curl -H "Authorization: Bearer your_secret_token_here" http://localhost:8050/user-details/123

# Using direct token format
curl -H "Authorization: your_secret_token_here" http://localhost:8050/user-details/123
```

### Endpoints

#### GET /user-details/{ID}

Returns user details for the specified user ID.

**Example:**
```bash
curl -H "Authorization: Bearer your_secret_token_here" http://localhost:8050/user-details/123
```

**Response:**
```json
{
  "user_id": "123",
  "username": "user_123",
  "email": "user_123@example.com",
  "status": "active"
}
```

#### GET /

Health check endpoint that returns API status.

**Example:**
```bash
curl -H "Authorization: Bearer your_secret_token_here" http://localhost:8050/
```

**Response:**
```json
{
  "message": "Simulated API is running",
  "version": "0.1.0"
}
```

### Error Responses

#### Missing Authorization Header
```json
{
  "detail": "Authorization header is missing"
}
```

#### Invalid Token
```json
{
  "detail": "Invalid authorization token"
}
```
