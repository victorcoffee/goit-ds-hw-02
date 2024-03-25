import psycopg2


def execute_query(sql: str) -> list:
    with psycopg2.connect(
        database="postgres",
        user="postgres",
        host="127.0.0.1",
        password="mysecretpassword",
        port=5432,
    ) as conn:
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT *
FROM users;
"""

print(execute_query(sql))
