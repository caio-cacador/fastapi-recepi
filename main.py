import logging
from fastapi import Depends, FastAPI
from api.dependencies.request_validators import token_is_valid
from api.routers import clients


logging.getLogger("uvicorn.error")

DEPENDENCIES = [Depends(token_is_valid)]


app = FastAPI(
    title="CHunt3r Recipe Fast API", 
    openapi_url="/openapi.json"
)
    
app.include_router(clients.router, dependencies=DEPENDENCIES)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
