"""FastAPI application with auth middleware for simulating APIs."""
import os
from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse
from typing import Optional


app = FastAPI(title="Simulated API", version="0.1.0")

# Get the static token from environment variable
AUTH_TOKEN = os.environ.get("AUTH_TOKEN", "default_secret_token")


@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    """Middleware to check Authorization header against configured static token."""
    authorization = request.headers.get("Authorization")
    
    # Check if Authorization header is present and matches the configured token
    if not authorization:
        return JSONResponse(
            status_code=401,
            content={"detail": "Authorization header is missing"}
        )
    
    # Support both "Bearer <token>" and direct token format
    token = authorization
    if authorization.startswith("Bearer "):
        token = authorization[7:]  # Remove "Bearer " prefix
    
    if token != AUTH_TOKEN:
        return JSONResponse(
            status_code=401,
            content={"detail": "Invalid authorization token"}
        )
    
    # Token is valid, proceed with the request
    response = await call_next(request)
    return response


@app.get("/user-details/{user_id}")
async def get_user_details(user_id: str):
    """Get user details by ID."""
    return {
        "user_id": user_id,
        "username": f"user_{user_id}",
        "email": f"user_{user_id}@example.com",
        "status": "active"
    }


@app.get("/")
async def root():
    """Root endpoint for health check."""
    return {"message": "Simulated API is running", "version": "0.1.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8050)
