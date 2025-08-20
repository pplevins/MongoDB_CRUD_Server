import uvicorn
from fastapi import FastAPI

from api import router as soldier_router

app = FastAPI(
    title="Soldiers Database API",
    summary="A FastAPI backend service that supplying REST API to the soldiers MongoDB collection.",
)

app.include_router(soldier_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
