class Config:
    DEBUG = 'DEBUG'
    SECRET_KEY = 'SECRET_KEY'
    ALLOWED_HOSTS = 'ALLOWED_HOSTS'


class Database:
    NAME = 'DATABASE_NAME'
    USER = 'DATABASE_USER'
    PASSWORD = 'DATABASE_PASSWORD'
    HOST = 'DATABASE_HOST'
    PORT = 'DATABASE_PORT'


class UserType:
    OPERATOR = 'operator'
    MEMBER = 'member'

    ROLE_CHOICES = (
        (OPERATOR, 'Operator'),
        (MEMBER, 'Member'),
    )


class Decision:
    LOGIN = 'login'
    REGISTER = 'register'

