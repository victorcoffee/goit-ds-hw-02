from datetime import datetime
import faker
from random import randint, choice
import psycopg2

NUMBER_USERS = 20
NUMBER_STATUSES = 3
NUMBER_TASKS = 10


def generate_fake_data(number_users, number_tasks) -> tuple:
    fake_fullnames = []
    fake_emails = []
    fake_titles = []
    fake_descriptions = []
    fake_status = []

    fake_data = faker.Faker("uk_UA")

    # Фейкові користувачі для таблиці users
    for _ in range(number_users):
        fake_fullnames.append(fake_data.name())
        fake_emails.append(fake_data.email())

    # Фейкові дані для таблиці завдань tasks
    for _ in range(number_tasks):
        fake_titles.append(fake_data.catch_phrase())
        fake_descriptions.append(fake_data.text())
        fake_status.append(
            choice(["new", "in progress", "completed"])
        )  # можно це зробити під час внесення в таблицю

    return fake_fullnames, fake_emails, fake_titles, fake_descriptions


def prepare_data(fullnames, emails, titles, descriptions) -> tuple:

    # для таблиці users
    for_users = []

    for fullname, email in zip(fullnames, emails):
        for_users.append(
            (fullname, email),
        )

    # для таблиці status
    for_status = [("new",), ("in progress",), ("completed",)]

    # для таблиці tasks
    for_tasks = []

    for title, description in zip(titles, descriptions):
        for_tasks.append(
            (title, description, randint(1, NUMBER_STATUSES), randint(1, NUMBER_USERS)),
        )

    return for_users, for_status, for_tasks


def insert_data_to_db(users, status, tasks) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсора для маніпуляцій з даними
    with psycopg2.connect(
        database="postgres",
        user="postgres",
        host="127.0.0.1",
        password="mysecretpassword",
        port=5432,
    ) as conn:

        cur = conn.cursor()

        # Заповнюємо таблицю із користувачами
        sql_to_users = """INSERT INTO users(fullname, email)
                               VALUES (?, ?)"""

        cur.executemany(sql_to_users, users)

        # Заповнюємо таблицю із статусами
        sql_to_users = """INSERT INTO status(name)
                               VALUES (?)"""

        cur.executemany(sql_to_users, users)

        # Останньою заповнюємо таблицю із задачами
        sql_to_tasks = """INSERT INTO tasks(title, description, status_id, user_id)
                              VALUES (?, ?, ?, ?)"""

        cur.executemany(sql_to_tasks, tasks)

        # Фіксуємо наші зміни в БД
        conn.commit()


if __name__ == "__main__":
    fullnames, emails, titles, descriptions  = prepare_data(
        *generate_fake_data(NUMBER_USERS, NUMBER_TASKS)
    )
    insert_data_to_db(for_users, for_status, for_tasks)
