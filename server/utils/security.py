from server.config import config
import jwt

def jwtDecode(encoded):
    return jwt.decode(encoded, config.JWT_KEY, algorithms=["HS256"])