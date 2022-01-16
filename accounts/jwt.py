from datetime import datetime, timedelta
from http.client import HTTPException
from django.http import HttpResponse
from jose import JWTError,jwt

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 518400

def create_access_token(data: dict):
    '''Generate a new Access Token'''
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
    
def verify_token(token:str):
    '''This function verifies if the header - token is valid or not'''
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        userphone : str = payload.get("sub")
        if userphone is None:
            return HttpResponse("User not registered, Invalid Token !")
        else:
            return userphone
    except JWTError:
        raise 
