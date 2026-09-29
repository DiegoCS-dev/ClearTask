from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

print(os.getenv("SECRET_KEY"))
print(os.getenv("ALGORITHM"))
print(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))