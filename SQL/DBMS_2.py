# Create database
CREATE DATABASE employees;

# Use the database
USE employees;

# Create employees table
CREATE TABLE employees (
    emp_id INT,
    emp_name VARCHAR(50),
    department VARCHAR(30),
    gender VARCHAR(10),
    city VARCHAR(30),
    salary INT,
    experience INT
);

# Insert records into employees table
INSERT INTO employees VALUES
(1, 'Rahul', 'IT', 'Male', 'Delhi', 70000, 5),
(2, 'Anita', 'HR', 'Female', 'Mumbai', 50000, 4),
(3, 'Aman', 'IT', 'Male', 'Delhi', 90000, 8),
(4, 'Neha', 'Finance', 'Female', 'Pune', 60000, 6),
(5, 'Rohit', 'IT', 'Male', 'Mumbai', 75000, 5),
(6, 'Priya', 'HR', 'Female', 'Delhi', 48000, 3),
(7, 'Vikas', 'Finance', 'Male', 'Pune', 65000, 7),
(8, 'Sneha', 'IT', 'Female', 'Bangalore', 85000, 6),
(9, 'Arjun', 'HR', 'Male', 'Mumbai', 52000, 4),
(10,'Kavya', 'Finance', 'Female', 'Delhi', 72000, 8);

# Display all employee records
SELECT * FROM employees;

# Average salary department-wise
SELECT department, AVG(salary)
FROM employees
GROUP BY department;

# Average salary department-wise where avg salary > 60000
SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;

# Total salary city-wise
SELECT city, SUM(salary)
FROM employees
GROUP BY city;

# Count of employees with salary > 60000 in each department
SELECT department, COUNT(*)
FROM employees
WHERE salary > 60000
GROUP BY department;

# Maximum salary gender-wise
SELECT gender, MAX(salary)
FROM employees
GROUP BY gender;

# Average salary by department and city
SELECT department, city, AVG(salary)
FROM employees
GROUP BY department, city;

# Count of male employees in each department
SELECT department, COUNT(*) AS male_count
FROM employees
WHERE gender = 'Male'
GROUP BY department;

# Maximum salary by department and gender
SELECT department, gender, MAX(salary)
FROM employees
GROUP BY department, gender;
