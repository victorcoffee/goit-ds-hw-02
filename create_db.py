import psycopg2


def create_db():
    # читаємо файл зі скриптом для створення БД
    with open("scripts.sql", "r") as f:
        sql = f.read()

    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with psycopg2.connect(
        database="postgres",
        user="postgres",
        host="127.0.0.1",
        password="mysecretpassword",
        port=5432,
    ) as conn:

        cur = conn.cursor()
        # виконуємо скрипт із файлу, який створить таблиці в БД
        cur.execute(sql)


if __name__ == "__main__":
    create_db()
