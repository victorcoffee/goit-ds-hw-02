-- Отримати всі завдання певного користувача. 
SELECT *
FROM tasks
WHERE user_id = 3;


-- Вибрати завдання за певним статусом.
SELECT t.id, t.title, t.description, t.status_id, t.user_id 
FROM tasks t
WHERE status_id = (
	SELECT id
	FROM status s
	WHERE name='new'
);


-- Оновити статус конкретного завдання. 
UPDATE tasks
SET status_id = 2
WHERE id = 1;


-- Отримати список користувачів, які не мають жодного завдання
SELECT fullname, email
FROM users u 
WHERE id NOT IN (
	SELECT user_id
	FROM tasks t 
);


-- Додати нове завдання для конкретного користувача. 
INSERT INTO tasks(title, description, status_id, user_id)
VALUES ('Negotiation on top level', 'Preparation and organization of the meeting in Dublin', 1, 3)


-- Отримати всі завдання, які ще не завершено
SELECT *
FROM tasks t 
WHERE status_id != (
	SELECT id 
	FROM status s 
	WHERE name = 'completed'
);


-- Видалити конкретне завдання.
DELETE FROM tasks 
WHERE id=6;


-- Знайти користувачів з певною електронною поштою
SELECT *
FROM users u 
WHERE email LIKE '%hall%';


-- Оновити ім'я користувача. 
UPDATE users SET fullname = 'Walter White'
WHERE fullname = 'Andrea White'


-- Отримати кількість завдань для кожного статусу
SELECT status_id, count(*)
FROM tasks t 
GROUP BY status_id 


-- Отримати завдання, які призначені користувачам 
-- з певною доменною частиною електронної пошти.

