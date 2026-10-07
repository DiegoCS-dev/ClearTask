from fastapi import Request, status, HTTPException
from jose import jwt, JWTError

from app.config import SECRET_KEY, ALGORITHM


def get_current_user(request: Request) -> int:

    print("COOKIES DA REQUISIÇÃO:", request.cookies)

    access_token = request.cookies.get("access_token")

    print("TOKEN RECEBIDO:", access_token)

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
    )

    if not access_token:
        raise credentials_exception

    try:
        payload = jwt.decode(
            access_token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        print("PAYLOAD:", payload)

        user_id_str = payload.get("sub")

        if user_id_str is None:
            raise credentials_exception

        return int(user_id_str)

    except (JWTError, ValueError) as e:
        print("Erro JWT:", e)
        raise credentials_exception