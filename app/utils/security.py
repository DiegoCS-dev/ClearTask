import os
from jose import  jwt, JWTError
from datetime import datetime, timedelta, timezone
from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
def criar_token(id_user):
    data_expiracao = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    dict_informacao = {"sub": str(id_user), "exp": data_expiracao}
    encode_jwt =jwt.encode(dict_informacao, SECRET_KEY, ALGORITHM)
    return encode_jwt
