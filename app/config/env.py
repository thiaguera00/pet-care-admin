from decouple import config

SECRET_KEY = config('SECRET_KEY', None)
ALGORITHM = config('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(config('ACCESS_TOKEN_EXPIRE_MINUTES', 60))