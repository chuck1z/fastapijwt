import time
import jwt
from fastapi import HTTPException
from pydantic import BaseModel

import secrets
JWT_SECRET = secrets.token_hex(16)
JWT_ALGORITHM = "HS256"

print(JWT_SECRET)

def sign(email):
    payload = {
        "email": email,
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token

def decode(token):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token
        
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

class SignUpSchema(BaseModel):
    name: str
    email: str
    password: str

class SignInSchema(BaseModel):
    email: str
    password: str

userlist = []

def signup(name, email, password):
    for user in userlist:
        if user.email == email:
            raise HTTPException(status_code=400, detail="Email already registered")
    user = SignUpSchema(name=name, email=email, password=password)
    userlist.append(user)

    token = sign(user.email)
    return token

def signin(email, password):
    for user in userlist:
        if user.email == email:
            if user.password == password:
                token = sign(user.email)
                return token
            else:
                raise HTTPException(status_code=400, detail="Incorrect password")
    raise HTTPException(status_code=400, detail="Email not registered")

