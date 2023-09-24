from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwtsign import decode

class Bearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    def validate(self, jwtoken: str):
        try:
            payload = decode(jwtoken)
            return True
        except:
            return False

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        
        if not credentials:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

        if credentials.scheme != "Bearer":
            raise HTTPException(status_code=403, detail="Invalid authentication scheme.")

        if not self.validate(credentials.credentials):
            raise HTTPException(status_code=403, detail="Invalid token or expired token.")

        return credentials.credentials
