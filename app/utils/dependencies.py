from fastapi import Depends, status, HTTPException
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from app.config import SECRET_KEY, ALGORITHM
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
# 1. A função de dependência que verifica o token

def get_current_user(token: str = Depends(oauth2_scheme)) -> int:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decodifica o token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id_str = payload.get("sub")
        
        # Se não houver 'sub' no payload, o token é inválido para nós
        if user_id_str is None:
            raise credentials_exception
    
        # Converte para int (como você queria)
        user_id = int(user_id_str)
        return user_id
        
    except (JWTError, ValueError):
        raise HTTPException(
            status_code=401,
            detail="Não foi possível validar as credenciais",
            headers={"WWW-Authenticate": "Bearer"},
        )