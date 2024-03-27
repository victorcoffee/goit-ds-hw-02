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

SELECT t.id, t.title, t.description, t.status_id, u.fullname, u.email 
FROM tasks AS t
INNER JOIN users AS u
ON t.user_id = u.id 
WHERE u.email LIKE '%@example.com';


-- Отримати список завдань, що не мають опису
SELECT * 
FROM tasks
WHERE description IS NULL
OR description = '';


-- Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
SELECT u.fullname, t.title, t.status_id 
FROM users AS u
INNER JOIN tasks AS t
ON u.id = t.user_id 
WHERE t.status_id = 2;

-- Другий варіант
SELECT u.fullname, t.title, t.user_id, s.name
FROM users AS u
INNER JOIN tasks AS t ON t.user_id = u.id 
INNER JOIN status AS s ON s.id = t.status_id
WHERE s.name = 'in progress';

-- Отримати користувачів та кількість їхніх завдань.
SELECT u.fullname, COUNT(t.title)  
FROM users AS u
LEFT JOIN tasks AS t
ON u.id = t.user_id 
GROUP BY u.id;