from datetime import datetime, timedelta, timezone
from jose import jwt

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