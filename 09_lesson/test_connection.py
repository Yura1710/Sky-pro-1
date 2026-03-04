from sqlalchemy import create_engine
from config import DATABASE_URL

try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print(" Подключение к БД успешно!")
    connection.close()
except Exception as e:
    print(f" Ошибка подключения: {e}")
