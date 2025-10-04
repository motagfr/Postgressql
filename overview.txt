-- SELECT * FROM actor;
-- SELECT first_name, last_name, email FROM customer; 
-- SELECT DISTINCT release_year FROM film;  --  ditinct here selects enique rows in a column and ignores the dupliucates
-- SELECT DISTINCT (rental_rate) FROM film;
-- SELECT DISTINCT film.rating FROM film --semicolon ain't necessary
-- SELECT DISTINCT rating FROM film;
-- SELECT COUNT (*) FROM film; 
-- SELECT COUNT (rating) FROM film
--  SELECT COUNT (DISTINCT film.rating) FROM film --how many unique ratings are in a column
--  SELECT COUNT (*) FROM payment
-- select column_name from INFORMATION_SCHEMA.COLUMNS where table_name = 'film'
-- SELECT DISTINCT amount FROM payment

-- SELECT * FROM customer
-- WHERE customer.first_name='Jared';   

-- SELECT * FROM film
-- WHERE film.rental_rate<4 AND film.replacement_cost>=27.99
-- AND rating='R'    

-- SELECT * FROM film
-- WHERE film.rental_rate<4 AND film.replacement_cost>=27.99
-- AND rating='R' AND NOT rental_duration=5

-- SELECT COUNT(*) FROM film
-- WHERE film.rental_rate<4 AND film.replacement_cost>=27.99
-- AND rating='R' OR rating='PG-13'

-- SELECT * FROM film
-- WHERE rating!='R';

-- SELECT email FROM customer
-- WHERE customer.first_name='Nancy' AND last_name='Thomas'

-- SELECT film.description FROM film 
-- WHERE film.title='Outlaw Hanky';

-- SELECT phone FROM address
-- WHERE address.address='259 Ipoh Drive';

-- SELECT store_id,first_name,last_name FROM customer
-- ORDER BY store_id DESC,first_name ASC,last_name

-- SELECT first_name,last_name FROM customer
-- ORDER BY store_id DESC,first_name ASC

-- SELECT * FROM payment
-- WHERE payment.amount!=0 
-- ORDER BY payment_date DESC
-- LIMIT 5;

-- SELECT * FROM payment
-- LIMIT 1;

-- SELECT title,length FROM film
-- ORDER BY length 
-- limit 5

-- SELECT COUNT(title) FROM film
-- WHERE length<=50

-- SELECT * FROM payment
-- WHERE amount BETWEEN 8 AND 9; --inclusive of 8 and 9

-- SELECT COUNT(*) FROM payment
-- WHERE amount NOT BETWEEN 8 AND 9; --excusive of 8 and 9

-- SELECT * FROM payment
-- WHERE payment_date BETWEEN '2007-02-01' AND '2007-02-15'--here the transactions on the last day don't appear unless they occur at 0.00 becasue the date column has hour and minutes

-- SELECT DISTINCT(amount) FROM payment

-- SELECT * FROM payment
-- WHERE amount IN (8.99,10.99,11.99)

-- SELECT COUNT(*) FROM payment
-- WHERE amount NOT IN (8.99,10.99,11.99)

-- SELECT * FROM customer
-- WHERE first_name IN ('Jimmie','David','Jenny')

--wild cards include % which means any string of characters and _ underscore which denotes only one CHARACTER
--LIKE is case-sensitive, but ILIKE is case-insensitive
--posgresql does support full regex capabilities

-- SELECT * FROM customer
-- WHERE first_name LIKE 'Ju%' AND last_name LIKE 'N%'

-- SELECT * FROM customer
-- WHERE first_name ILIKE 'a%' AND last_name NOT LIKE 'R%'
-- ORDER BY last_name; 

-- SELECT COUNT(*) FROM film
-- WHERE rating='R' AND replacement_cost BETWEEN 5 AND 15;

-- SELECT COUNT(title) FROM film  --How many films have Truman somewhere in the title
-- WHERE title LIKE '%Truman%'

-- SELECT title FROM film
-- WHERE title LIKE '%Truman%'

--Most common aggregate functions AVG(),count(),max(),min(),sum()
--these functions occur only in the SELECT clause or HAVING clause

-- SELECT MIN(replacement_cost) FROM film;
-- SELECT MIN(replacement_cost),max(replacement_cost) FROM film;
-- SELECT ROUND(AVG(replacement_cost),2) FROM film --AVG gives you alot of significant digits by default, so has to be rounded

--in the SELECT statement, columns must either have an aggregate function or be in the GROUP BY call. 
--WHERE staments dshould not refer tothe aggregation result. We will use having to filter on those results.
--If you want to sort results based on the aggreagte, make sure to reference the entire function.ACCESS

-- SELECT customer_id FROM customer
-- GROUP BY customer_id   --this code is like using DISTINCT

--  SELECT customer_id,SUM(amount),COUNT(amount) FROM payment
--  GROUP BY customer_id  --total sum spent by each customer, who may have rented many times
--  ORDER BY SUM(amount) DESC

-- SELECT customer_id,staff_id,SUM(amount) FROM payment
-- GROUP BY customer_id,staff_id
-- ORDER BY customer_id,staff_id

--if you are to group by a date column that has a time stamp(that is minute hour second) we must call a specialized date function.

-- SELECT DATE(payment_date), SUM(amount) FROM payment
-- GROUP BY DATE(payment_date)
-- ORDER BY SUM(amount) DESC

-- SELECT COUNT(amount) FROM payment

-- SELECT DISTINCT staff_id,COUNT(amount) FROM payment
-- GROUP BY staff_id  --number of payments handle per staff member. 

-- SELECT rating,ROUND(AVG(replacement_cost),2) FROM film
-- GROUP BY rating --average repalcement cost per rating

-- SELECT customer_id,SUM(amount) FROM payment  --top 5 customers by total spending
-- GROUP BY customer_id
-- ORDER BY SUM(amount) DESC
-- LIMIT 5;

-- SELECT customer_id,SUM(amount) FROM payment 
-- GROUP BY customer_id
-- HAVING SUM(amount)>100  --a WHERE statement comes before group by and HAVING after because SUM will not be calculated before Group BY

-- SELECT store_id,COUNT(*) FROM customer --stores having more that 300 customers
-- GROUP BY store_id                      -- if you write customer_id it's better than wrting *   
-- HAVING COUNT(*)>300

-- SELECT customer_id,COUNT(payment_id) FROM payment
-- GROUP BY customer_id
-- HAVING COUNT(payment_id)>=40

-- SELECT customer_id,SUM(amount) FROM payment
-- WHERE staff_id=2            --customers who spent more than 100 with staff number 2
-- GROUP BY customer_id
-- HAVING SUM(amount)>100
-- ORDER BY SUM(amount) DESC

-- SELECT SUM(amount) AS net_revenue FROM payment --this is aliasing, which makes queries easy to read for analysts.

--IN posgresql INNER JOIN is the same as JOIN

-- SELECT payment_id,payment.customer_id,first_name  --since customer_id isn't unique to either table you have to clarify which table it comes from
-- FROM payment            --in this talble you will only see customers who have made a payment, not otheres.
-- INNER JOIN customer
-- ON payment.customer_id = customer.customer_id

-- SELECT * FROM payment   
-- FULL OUTER JOIN customer
-- ON customer.customer_id = payment.customer_id
-- WHERE customer.customer_id IS NULL 
-- OR payment.payment_id IS NULL  --entries unique to either table, not both

-- SELECT * FROM payment --all entries except those not found in customer. Remember that tables will be joined and some columns may be empty
-- LEFT OUTER JOIN customer --LEFT JOIN is the same as LEFT OUTER JOIN
-- ON customer.customer_id = payment.customer_id
-- WHERE customer.customer_id IS NULL --this line returns entries unique to table payment only

-- SELECT film.film_id,title,inventory_id,store_id --films that are in the film table and not just in the inventory alone, say without a title.
-- FROM film
-- LEFT JOIN inventory 
-- ON inventory.film_id = film.film_id

-- SELECT film.film_id,title,inventory_id,store_id --films that are in the film table and not just in the inventory alone, say without a title.
-- FROM film
-- LEFT JOIN inventory 
-- ON inventory.film_id = film.film_id
-- WHERE inventory.film_id IS NULL

--ONe can swtich the order of tables in left join to get right join.

-- SELECT district,email FROM customer
-- INNER JOIN address 
-- ON address.address_id = customer.address_id
-- WHERE address.district='California' --The emails of the customers who live in california.

-- SELECT title,first_name,last_name FROM film --list of all the movies actor *Nick Wahlberg* has been in
-- JOIN film_actor                             ---here we joined three tables.
-- ON film_actor.film_id = film.film_id
-- JOIN actor
-- ON film_actor.actor_id = actor.actor_id 
-- WHERE actor.first_name='Nick' 
-- AND actor.last_name='Wahlberg'


-- SELECT first_name,last_name,COUNT(film.title) AS total_movies_acted --how many movies each actor has played
-- FROM actor
-- JOIN film_actor 
-- ON film_actor.actor_id = actor.actor_id
-- JOIN film ON film.film_id = film_actor.film_id
-- GROUP BY first_name,last_name
-- ORDER BY COUNT(*) DESC

-- SELECT first_name,last_name,total_movies_acted FROM --top 10 actors
-- (SELECT first_name,last_name,COUNT(film.title) AS total_movies_acted 
-- FROM actor
-- JOIN film_actor 
-- ON film_actor.actor_id = actor.actor_id
-- JOIN film ON film.film_id = film_actor.film_id
-- GROUP BY first_name,last_name
-- ORDER BY COUNT(*) DESC)
-- LIMIT 10;   --Performing a query on a result from another query

--SHOW ALL 
--SHOW timezone
--SELECT NOW() --returns a timestap with timezone information of current time.
-- SELECT timeofday() --above information as a string
-- SELECT CURRENT_TIME --time without time zone
-- SELECT CURRENT_DATE --date without time zone
-- SELECT CURRENT_TIMESTAMP --timestamp with time zone 

-- SELECT extract(YEAR FROM  payment_date) AS year,AGE(payment_date),
-- to_char(payment_date,'dd-Mon-YYYY HH12:MI:SS AM') AS formatted_date --check the documentation for to_char function
-- FROM payment

-- SELECT ROUND(rental_rate/replacement_cost,4)*100 AS rental_to_replacement_percent 
-- FROM film --check the documentation for mathematical functions in PostgreSQL.

-- SELECT first_name || ' ' || last_name AS full_name --string concatenation operator is ||
-- FROM actor 

-- SELECT title,rental_rate FROM film
-- WHERE rental_rate> (SELECT AVG(rental_rate) FROM film)  --SUBQUERY


-- SELECT title FROM film --we use the IN operator when the subquery returns multiple rows
-- WHERE film_id IN
-- (SELECT inventory.film_id FROM rental
-- inner join inventory
-- ON rental.inventory_id = inventory.inventory_id
-- WHERE rental_date BETWEEN '2005-05-25' AND '2005-06-01')
-- ORDER BY title;

-- SELECT first_name,last_name FROM customer
-- WHERE EXISTS
-- (SELECT * FROM payment
-- WHERE payment.customer_id = customer.customer_id AND amount>11) --EXISTS is used when you want to check if a subquery returns any rows. It returns true or false.

-- -- 1) Using JOIN (watch duplicates)
-- SELECT DISTINCT c.first_name, c.last_name
-- FROM customer c
-- JOIN payment p ON p.customer_id = c.customer_id
-- WHERE p.amount > 11;

-- -- 2) Using IN
-- SELECT first_name, last_name
-- FROM customer
-- WHERE customer_id IN (
--   SELECT customer_id FROM payment WHERE amount > 11
-- );

-- SELECT title c FROM film --AS is optional for aliasing

-- EXPLAIN ANALYZE
-- SELECT first_name, last_name
-- FROM customer
-- WHERE EXISTS (
--   SELECT *
--   FROM payment
--   WHERE payment.customer_id = customer.customer_id
--     AND amount > 11
-- );

--when using self join it is necessary to use an aliad for the table, otherwise table names would be ambiguous.

-- SELECT f1.title,f2.title,f1.length
-- FROM film AS f1
-- JOIN film AS f2 ON
-- f2.film_id != f1.film_id
-- AND f1.length = f2.length
-- WHERE f1.length=117

-------------------
-- from here we'll be working on Learning data base.

-- CREATE TABLE account(
--     user_id SERIAL PRIMARY KEY,
--     username VARCHAR(50) UNIQUE NOT NULL,
--     password VARCHAR(50) NOT NULL,
--     email VARCHAR(100) UNIQUE NOT NULL,
--     created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     last_login TIMESTAMP
-- )

-- CREATE TABLE job(
-- job_id SERIAL PRIMARY KEY,
-- job_name VARCHAR(50) UNIQUE NOT NULL
-- );
-- CREATE TABLE account_job(
--     user_id INTEGER REFERENCES account(user_id),
--     job_id INTEGER REFERENCES job(job_id),
--     hire_date TIMESTAMP
-- )

--when inserting values into a table, you don't have to provide values for serial columns, they will be auto-generated.

-- INSERT INTO account(username,password,email,created_on)
-- VALUES 
-- ('johndoe','password123','jodo@gmail.com',CURRENT_TIMESTAMP)

-- SELECT * FROM account;

-- INSERT INTO job(job_name)
-- VALUES
-- ('Data Analyst'),
-- ('Data Scientist'),
-- ('Database Administrator'),
-- ('Data Engineer'),
-- ('Machine Learning Engineer');

-- SELECT * FROM job;

-- INSERT INTO account_job(user_id,job_id,hire_date)
-- VALUES
-- (1,1,CURRENT_TIMESTAMP),
-- (1,3,CURRENT_TIMESTAMP);

-- SELECT * FROM account_job;

-- INSERT INTO account_job(user_id,job_id,hire_date)
-- VALUES  --this produces an error because user_id 10 does not exist in account table
-- (10,1,CURRENT_TIMESTAMP)

-- -- SELECT * FROM account;
-- UPDATE account
-- SET last_login=CURRENT_TIMESTAMP
-- WHERE username='johndoe'; --this doesn't return any rows because UPDATE doesn't return rows. You have to use SELECT to see the changes.

-- SELECT * FROM account;
-- SELECT * FROM account_job;

-- UPDATE account_job --updating hire_date for user_id 1 and job_id 3 from account_job table
-- SET hire_date=account.created_on --this is called update join
-- FROM account
-- WHERE account.user_id=account_job.user_id;

-- SELECT * FROM account_job;

-- UPDATE account
-- SET password='newpassword456'
-- WHERE username='johndoe'
-- RETURNING *; --this returns the updated rows.

-- DELETE FROM job
-- WHERE job_name='Data Engineer'
-- RETURNING *; --this returns the deleted rows.
-- SELECT * FROM job;

-- CREATE TABLE information(
--     info_id SERIAL PRIMARY KEY,
--     title VARCHAR(50) NOT NULL,
--     person VARCHAR(50) NOT NULL UNIQUE
-- );
-- SELECT * FROM information;

-- ALTER TABLE information
-- RENAME to new_information; --renaming a table

-- -- SELECT * FROM new_information;
-- ALTER TABLE new_information
-- RENAME COLUMN person TO people; --renaming a column

-- SELECT * FROM new_information;

-- INSERT INTO new_information(title)
-- VALUES
-- ('Data Analyst'); --this produces an error because people column is NOT NULL and has no default value.

-- ALTER TABLE new_information
-- ALTER COLUMN people SET DEFAULT 'Unknown'; --setting a default value for a column

-- ALTER TABLE new_information
-- ALTER COLUMN people DROP NOT NULL; --dropping NOT NULL constraint from a column 

-- INSERT INTO new_information(title)
-- VALUES
-- ('Data Analyst'); --this works now because people column is no longer NOT NULL
-- SELECT * FROM new_information;

-- ALTER TABLE new_information
-- ADD COLUMN new_column TIMESTAMP DEFAULT CURRENT_TIMESTAMP; --adding a new column to a table
-- SELECT * FROM new_information; --i added another column by mistake

-- ALTER TABLE new_information
-- DROP COLUMN new_column;--dropping a column from a tab
-- SELECT * FROM new_information

-- ALTER TABLE new_information
-- DROP COLUMN IF EXISTS people; --dropping a column if it exists
-- SELECT * FROM new_information;

-- CREATE TABLE employee(
--     emp_id SERIAL PRIMARY KEY,
--     first_name VARCHAR(50) NOT NULL,
--     last_name VARCHAR(50) NOT NULL,
--     birthday DATE CHECK(birthday > '1900-01-01'),
--     email VARCHAR(100) UNIQUE,
--     hire_date DATE CHECK(hire_date>=birthday),
--     salary NUMERIC CHECK(salary>=0),
--     job_title VARCHAR(50) NOT NULL
-- );
-- SELECT * FROM employee;

-- INSERT INTO employee(first_name,
-- last_name,
-- birthday,
-- email,hire_date,salary,job_title)
-- VALUES
-- -- ('John','Doe','1885-06-15','johnDow@gmail.com','2020-01-10',60000,'Data Analyst'), --here birthday is less than 1900-01-01 so there will be an error
-- ('Jane','Smith','1990-09-25','Jane@gmail.com','2019-03-15',75000,'Data Scientist'),
-- ('Alice','Johnson','1988-12-05','Alice@mail.com','2018-07-20',80000,'Database Administrator'),
-- ('Bob','Brown','1975-04-30','bin@mail.com','2015-11-05',95000,'Data Engineer');

-- SELECT * FROM employee;
--serial will generate a number both when you delete rows or fail to insert them! Keep that in mind.

--now switiching to dvdrental database

-- SELECT customer_id, --creating a new column based on conditions in another column
-- CASE 
--     WHEN customer_id<100 THEN 'Premium'
--     WHEN customer_id BETWEEN 100 AND 300 THEN 'Gold'
--     ELSE 'Silver' 
-- END AS customer_type
-- FROM customer;


-- SELECT customer_id, --case by equality with an expression
-- CASE customer_id
--     WHEN 2 THEN 'Winner'
--     WHEN 5 THEN 'Second Place'
--     ELSE 'Normal' 
-- END AS raffle_results
-- FROM customer;

--study coalesce function

--select CAST(inventory_id AS VARCHAR) from rental

--a veiw is a datbase object that is of a stored query. So you don't have to repeat a query again.
--a veiw can be accessed as a table by Postgresql.
--note that a view does not store data physically, it simply stores the query.

-- CREATE VIEW active_actors AS  
-- SELECT first_name,last_name,COUNT(film.title) AS total_movies_acted --how many movies each actor has played
-- FROM actor
-- JOIN film_actor 
-- ON film_actor.actor_id = actor.actor_id
-- JOIN film ON film.film_id = film_actor.film_id
-- GROUP BY first_name,last_name
-- ORDER BY COUNT(*) DESC;

-- SELECT * FROM active_actors

--DROP VIEW IF EXISTS active_actors

--ALTER VIEW active_actors RENAME TO most_active_actors



