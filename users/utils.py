from cryptography.fernet import Fernet
from config import settings


def encrypt(text: str) -> str:
    fernet = Fernet(key=settings.secret_key)
    return fernet.encrypt(str(text).encode()).decode()


def decrypt(text: str) -> str:
    fernet = Fernet(key=settings.secret_key)
    return fernet.decrypt(str(text).encode()).decode()

