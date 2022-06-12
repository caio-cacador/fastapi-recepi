import logging
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBearer

security = HTTPBearer()
logger = logging.getLogger("uvicorn.error")

async def token_is_valid(credentials: HTTPBasicCredentials = Depends(security)):
    """
        Function that is used to validate the token in the case that it requires it
    """
    logger.info(f'Checking token...')
    token = credentials.credentials

    try:
        if token == 'token':
            return
        
        raise Exception()
        
    except Exception as ex:
        logger.error(f'Token is invalid: {token}')
        raise HTTPException(status_code=401, detail=str(ex))
