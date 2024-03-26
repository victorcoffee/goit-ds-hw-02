-- Модуль 2. Завдання 1

-- Створення таблиць
DROP TABLE IF EXISTS users CASCADE;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  fullname VARCHAR(100),
  email VARCHAR(100) UNIQUE
);


DROP TABLE IF EXISTS status CASCADE;
CREATE TABLE status (
id SERIAL PRIMARY KEY,
name VARCHAR(50) UNIQUE
);


-- FOREIGN KEY в консолі не проходили
DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  title VARCHAR(50),
  description text,
 status_id INTEGER REFERENCES status(id)
  	on delete CASCADE
  	on update CASCADE,
 user_id INTEGER REFERENCES users(id)
  	on delete CASCADE
  	on update CASCADE
);
