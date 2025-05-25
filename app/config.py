from urllib.parse import quote_plus

class Config:
    # Configuración manual de la base de datos
    DB_USER = 'root'
    DB_PASSWORD = 'A$2001M$10D$25'
    DB_HOST = 'localhost'
    DB_NAME = 'medinno'

    # Escapamos caracteres especiales de la contraseña
    password_esc = quote_plus(DB_PASSWORD)

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{password_esc}@{DB_HOST}:3306/{DB_NAME}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False