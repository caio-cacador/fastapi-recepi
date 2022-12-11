from fastapi import Depends, FastAPI
from api.dependencies.request_validators import token_is_valid
from api.routers import clients


DEPENDENCIES = [Depends(token_is_valid)]

def app():
    app = FastAPI(
        title="CHunt3r Recipe Fast API", 
        openapi_url="/openapi.json"
    )
        
    app.include_router(clients.router, dependencies=DEPENDENCIES)
    return app
    
if __name__ == "__main__":
    app()
