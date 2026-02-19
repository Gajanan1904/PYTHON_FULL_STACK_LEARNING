# Indexting:it helps sql find data faster,just like a book index or page number
# without index:
# 	start from page 1
# 	read every page
# 	very slow
# with index:
# 	go to index
# 	directly jump there
#  Drawbacks of indexing:
# 	Don't use when the table is small
# 	It occupies some space
# 	Insert,Update,Delete becomes slow after indexing


CREATE  database customer;
use customer;

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

#Generate indexing
create INDEX idx_name on customers(customer_name);

select * from customers where customer_name="anita";
# +-------------+---------------+-----------+
# | customer_id | customer_name | city      |
# +-------------+---------------+-----------+
# |          10 | Anita         | Bangalore |
# +-------------+---------------+-----------+

select * from customers where customer_id=6;
# +-------------+---------------+--------+
# | customer_id | customer_name | city   |
# +-------------+---------------+--------+
# |           6 | Simran        | Mumbai |
# +-------------+---------------+--------+

select product from orders where product="earphones";
# +-----------+
# | product   |
# +-----------+
# | Earphones |
# +-----------+

#ALTER COMMAND:used to add columns
ALTER TABLE orders ADD age int;
# +----------+-------------+-----------+--------+------+
# | order_id | customer_id | product   | amount | age  |
# +----------+-------------+-----------+--------+------+
# |      101 |           1 | Laptop    |  60000 | NULL |
# |      102 |           1 | Mouse     |   1500 | NULL |
# |      103 |           2 | Mobile    |  30000 | NULL |
# |      104 |           3 | Keyboard  |   2500 | NULL |
# |      105 |           3 | Monitor   |  12000 | NULL |
# |      106 |           5 | Tablet    |  20000 | NULL |
# |      107 |           6 | Laptop    |  65000 | NULL |
# |      108 |           7 | Mobile    |  28000 | NULL |
# |      109 |           7 | Earphones |   2000 | NULL |
# |      110 |          11 | Camera    |  40000 | NULL |
# +----------+-------------+-----------+--------+------+
