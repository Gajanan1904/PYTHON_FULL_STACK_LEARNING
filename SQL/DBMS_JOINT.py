# ===============================
# DATABASE & TABLE CREATION
# ===============================

CREATE DATABASE customer;
USE customer;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(50),
    amount INT
);

INSERT INTO customers VALUES
(1, 'Aman', 'Delhi'),
(2, 'Riya', 'Mumbai'),
(3, 'Kabir', 'Delhi'),
(4, 'Neha', 'Pune'),
(5, 'Arjun', 'Bangalore'),
(6, 'Simran', 'Mumbai'),
(7, 'Rahul', 'Delhi'),
(8, 'Pooja', 'Chennai'),
(9, 'Vikas', 'Pune'),
(10, 'Anita', 'Bangalore');

INSERT INTO orders VALUES
(101, 1, 'Laptop', 60000),
(102, 1, 'Mouse', 1500),
(103, 2, 'Mobile', 30000),
(104, 3, 'Keyboard', 2500),
(105, 3, 'Monitor', 12000),
(106, 5, 'Tablet', 20000),
(107, 6, 'Laptop', 65000),
(108, 7, 'Mobile', 28000),
(109, 7, 'Earphones', 2000),
(110, 11, 'Camera', 40000);

# ===============================
# Q1 Show customer_name, product, amount
# ===============================
SELECT c.customer_name, o.product, o.amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;

# +---------------+-----------+--------+
# | customer_name | product   | amount |
# +---------------+-----------+--------+
# | Aman          | Laptop    | 60000  |
# | Aman          | Mouse     | 1500   |
# | Riya          | Mobile    | 30000  |
# | Kabir         | Keyboard  | 2500   |
# | Kabir         | Monitor   | 12000  |
# | Arjun         | Tablet    | 20000  |
# | Simran        | Laptop    | 65000  |
# | Rahul         | Mobile    | 28000  |
# | Rahul         | Earphones | 2000   |
# +---------------+-----------+--------+

# ===============================
# Q2 Show customer_name, product, order_id
# ===============================
SELECT c.customer_name, o.product, o.order_id
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;

# +---------------+-----------+----------+
# | customer_name | product   | order_id |
# +---------------+-----------+----------+
# | Aman          | Laptop    | 101      |
# | Aman          | Mouse     | 102      |
# | Riya          | Mobile    | 103      |
# | Kabir         | Keyboard  | 104      |
# | Kabir         | Monitor   | 105      |
# | Arjun         | Tablet    | 106      |
# | Simran        | Laptop    | 107      |
# | Rahul         | Mobile    | 108      |
# | Rahul         | Earphones | 109      |
# +---------------+-----------+----------+

# ===============================
# Q3 Customers from Delhi who placed orders
# ===============================
SELECT c.customer_name, o.product
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE c.city = 'Delhi';

# +---------------+-----------+
# | customer_name | product   |
# +---------------+-----------+
# | Aman          | Laptop    |
# | Aman          | Mouse     |
# | Kabir         | Keyboard  |
# | Kabir         | Monitor   |
# | Rahul         | Mobile    |
# | Rahul         | Earphones |
# +---------------+-----------+

# ===============================
# Q4 Show all customers even if they have no orders
# ===============================
SELECT c.customer_name, o.product
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;

# +---------------+-----------+
# | customer_name | product   |
# +---------------+-----------+
# | Aman          | Mouse     |
# | Aman          | Laptop    |
# | Riya          | Mobile    |
# | Kabir         | Monitor   |
# | Kabir         | Keyboard  |
# | Neha          | NULL      |
# | Arjun         | Tablet    |
# | Simran        | Laptop    |
# | Rahul         | Earphones |
# | Rahul         | Mobile    |
# | Pooja         | NULL      |
# | Vikas         | NULL      |
# | Anita         | NULL      |
# +---------------+-----------+

# ===============================
# Q5 Show all orders even if customer does not exist
# ===============================
SELECT *
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.customer_id;

# +----------+-------------+-----------+--------+-------------+---------------+-----------+
# | order_id | customer_id | product   | amount | customer_id | customer_name | city      |
# +----------+-------------+-----------+--------+-------------+---------------+-----------+
# | 110      | 11          | Camera    | 40000  | NULL        | NULL          | NULL      |
# +----------+-------------+-----------+--------+-------------+---------------+-----------+

# ===============================
# Q6 Final orders with no matching customers
# ===============================
SELECT *
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

# +----------+-------------+---------+--------+-------------+---------------+------+
# | order_id | customer_id | product | amount | customer_id | customer_name | city |
# +----------+-------------+---------+--------+-------------+---------------+------+
# | 110      | 11          | Camera  | 40000  | NULL        | NULL          | NULL |
# +----------+-------------+---------+--------+-------------+---------------+------+

# ===============================
# Q7 Show all customers and all orders
# ===============================
SELECT *
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
UNION
SELECT *
FROM customers c
RIGHT JOIN orders o ON c.customer_id = o.customer_id;

# (Output preserved exactly as provided)

# ===============================
# Q8 Customers who placed at least one order
# ===============================
SELECT customer_name
FROM customers
WHERE customer_id IN (SELECT customer_id FROM orders);

# +---------------+
# | customer_name |
# +---------------+
# | Aman          |
# | Riya          |
# | Kabir         |
# | Arjun         |
# | Simran        |
# | Rahul         |
# +---------------+

# ===============================
# Q9 Customers who have NOT placed any order
# ===============================
SELECT customer_name
FROM customers
WHERE customer_id NOT IN (SELECT customer_id FROM orders);

# +---------------+
# | customer_name |
# +---------------+
# | Neha          |
# | Pooja         |
# | Vikas         |
# | Anita         |
# +---------------+

# ===============================
# Q10 Customers with orders above average amount
# ===============================
SELECT customer_name
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
    WHERE amount > (SELECT AVG(amount) FROM orders)
);

# +---------------+
# | customer_name |
# +---------------+
# | Aman          |
# | Riya          |
# | Simran        |
# | Rahul         |
# +---------------+
