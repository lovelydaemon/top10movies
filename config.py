from dotenv import dotenv_values

config = dotenv_values('.env', verbose=True)

def create_db_uri(config: dict[str, str | None]) -> str:
    """Return the db URI, default sqlite."""
    base = config.get('DB_BASE', 'sqlite')
    user = config.get('DB_USER')
    host = config.get('DB_HOST', 'localhost')
    name = config.get('DB_NAME', 'db_name')

    if base == 'sqlite':
        return f'{base}:///{name}'

    if not user:
        raise ValueError('Required user login and password')
    return f'{base}://{user}@{host}/{name}'

class Config():
    SECRET_KEY = config.get('SECRET_KEY', 'default_key')
    SQLALCHEMY_DATABASE_URI = create_db_uri(config)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
