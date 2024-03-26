import faker
from random import randint, choice
import psycopg2

NUMBER_USERS = 5
NUMBER_STATUSES = 3
NUMBER_TASKS = 7


def main():
    fake_fullnames = []
    fake_emails = []
    fake_titles = []
    fake_descriptions = []
    # fake_status = []

    fake_data = faker.Faker()

    # Фейкові користувачі для таблиці users
    for _ in range(NUMBER_USERS):
        fake_fullnames.append(fake_data.name())
        fake_emails.append(fake_data.email())

    # Фейкові дані для таблиці завдань tasks
    for _ in range(NUMBER_TASKS):
        fake_titles.append(fake_data.catch_phrase())
        fake_descriptions.append(fake_data.text())
        # fake_status.append(
        #     choice(["new", "in progress", "completed"])
        # )  # можно це зробити під час внесення в таблицю

    # для таблиці users
    for_users = []

    for fullname, email in zip(fake_fullnames, fake_emails):
        for_users.append(
            (fullname, email),
        )

    # для таблиці status
    status = [("new",), ("in progress",), ("completed",)]

    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсора для маніпуляцій з даними
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        host="127.0.0.1",
        password="mysecretpassword",
        port=5432,
    )
    cur = conn.cursor()

    # Заповнюємо таблицю із користувачами
    sql_to_users = """
    INSERT INTO users(fullname, email)
    VALUES (?, ?)
    """

    # cur.executemany(sql_to_users, for_users)
    for i in range(NUMBER_USERS):
        cur.execute(
            "INSERT INTO users (fullname, email) VALUES (%s, %s)",
            (fake_fullnames[i], fake_emails[i]),
        )

    # Заповнюємо таблицю із статусами
    sql_to_status = """
    INSERT INTO status(name)
    VALUES (%s)
    """

    cur.executemany(sql_to_status, status)

    # Фіксуємо наші зміни в БД
    conn.commit()


if __name__ == "__main__":
    main()
