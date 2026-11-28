from datetime import datetime, timedelta, timezone
from jose import jwt
from fastapi import HTTPException, status


SECRET_KEY = "afaffakjbsiudbgvhsdhfbs"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data : dict, expires_delta:timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + timedelta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({
        "exp" : expire
    })

    encoded_token = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    return encoded_token

def verify_access_token(token:str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.JWTError:
        print("Invalid error")
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid Token!!"
        )




if __name__ == "__main__":
    print("this is from jwt_helper file")
    token = create_access_token({"name":"abc"})
    payload = verify_access_token(token)
    print(payload)