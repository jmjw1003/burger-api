from fastapi import FastAPI
from app.api.v1.endpoints import burgers

app = FastAPI(
    title="Burger Ordering API",
    version="1.0.0",
    description="API to simulate ordering burgers."
)

# Include API routes
app.include_router(burgers.router, prefix="/api/v1/burgers", tags=["Burgers"])
