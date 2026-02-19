# =========================
# DATABASE & CONSTRAINTS
# =========================

# Create database
CREATE DATABASE sqlconstraints;

# Use database
USE sqlconstraints;

# =========================
# NOT NULL & PRIMARY KEY
# =========================

# Create Employees table with NOT NULL constraint
CREATE TABLE Employees (
    ID INT PRIMARY KEY,
    LastName VARCHAR(255) NOT NULL,   # Must have value
    FirstName VARCHAR(255),           # Can be NULL
    Age INT
);

# =========================
# UNIQUE CONSTRAINT
# =========================

# Create Persons table with UNIQUE constraint
CREATE TABLE Persons (
    ID INT NOT NULL UNIQUE,
    LastName VARCHAR(255) NOT NULL,
    FirstName VARCHAR(255),
    Age INT,
    CONSTRAINT UC_Person UNIQUE (LastName, FirstName)
);

# =========================
# CHECK CONSTRAINT
# =========================

# Create students table with CHECK constraint
CREATE TABLE students (
    id INT PRIMARY KEY,               # Primary key
    name VARCHAR(20) NOT NULL,         # NOT NULL
    PHNO BIGINT UNIQUE,                # UNIQUE
    marks INT CHECK (marks >= 0 AND marks <= 100)  # Valid range
);

# =========================
# DEFAULT CONSTRAINT
# =========================

# Set default value for marks
ALTER TABLE students
ALTER COLUMN marks SET DEFAULT 0;

# Insert sample data
INSERT INTO students (id, name, PHNO) VALUES
(1, 'Shiv', 987654321),
(2, 'Naman', 876543210),
(3, 'Pranit', 765432109);

# Update marks using CASE
UPDATE students
SET marks = CASE
    WHEN id = 1 THEN 85
    WHEN id = 2 THEN 92
    WHEN id = 3 THEN 78
END
WHERE id IN (1, 2, 3);

# Display students table
SELECT * FROM students;

# =========================
# PRIMARY KEY & FOREIGN KEY
# =========================

# Create Table1 (Parent table)
CREATE TABLE Table1 (
    student_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT
);

# Insert data into Table1
INSERT INTO Table1 VALUES
(101, 'Shivashish', 20),
(102, 'Srijan', 21);

# Create Table2 with FOREIGN KEY
CREATE TABLE Table2 (
    student_id INT,
    name VARCHAR(50) NOT NULL,
    age INT,
    FOREIGN KEY (student_id) REFERENCES Table1(student_id)
);

# Insert data into Table2
INSERT INTO Table2 VALUES
(101, 'Shivashish_Record', 20),
(102, 'Srijan_Record', 21);

# =========================
# MULTIPLE TABLE RELATION
# =========================

# Create courses table
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50) NOT NULL
);

# Insert courses
INSERT INTO courses VALUES
(101, 'Data Science'),
(102, 'Web Development');

# Create enrollments table with 2 foreign keys
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

# Insert valid enrollment records
INSERT INTO enrollments VALUES
(1, 1, 101),
(2, 2, 102);

# =========================
# TABLE 3 & TABLE 4
# =========================

# Create Table3
CREATE TABLE Table3 (
    student_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT
);

# Insert data into Table3
INSERT INTO Table3 VALUES
(101, 'Shivashish', 20),
(102, 'Srijan', 21);

# Create Table4 with foreign key
CREATE TABLE Table4 (
    subject_id INT PRIMARY KEY,
    student_id INT,
    subject VARCHAR(50),
    marks INT,
    FOREIGN KEY (student_id) REFERENCES Table3(student_id)
);

# Insert subject records
INSERT INTO Table4 VALUES
(1, 101, 'SQL', 98),
(2, 102, 'Python', 95);

# =========================
# TABLE 5 & TABLE 6
# =========================

# Create Table5
CREATE TABLE Table5 (
    EmpId INT PRIMARY KEY,
    Emp_name VARCHAR(50) UNIQUE,
    Emp_city VARCHAR(50) NOT NULL
);

# Insert data into Table5
INSERT INTO Table5 VALUES
(1001, 'Shivashish', 'Delhi'),
(1002, 'Srijan', 'Mumbai');

# Create Table6 with foreign key & CHECK
CREATE TABLE Table6 (
    department_id INT PRIMARY KEY,
    EmpId INT,
    department VARCHAR(50) NOT NULL,
    Salary INT CHECK (Salary IN (50000, 100000)),
    FOREIGN KEY (EmpId) REFERENCES Table5(EmpId)
);

# Insert department records
INSERT INTO Table6 VALUES
(1, 1001, 'Engineering', 100000),
(2, 1002, 'Marketing', 50000);

# Display final tables
SELECT * FROM Table5;
SELECT * FROM Table6;


# Employees table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,      # employee id
    emp_name VARCHAR(50),        # employee name
    department VARCHAR(50)       # department
);

# Insert employees data
INSERT INTO employees VALUES
(1,'Rahul','IT'),
(2,'Neha','HR'),
(3,'Amit','IT'),
(4,'Priya','Finance'),
(5,'Karan','HR');


# Projects table
CREATE TABLE projects (
    project_id INT PRIMARY KEY,  # project id
    project_name VARCHAR(50),    # project name
    budget INT                   # project budget
);

# Insert projects data
INSERT INTO projects VALUES
(101,'Website Revamp',100000),
(102,'Mobile App',150000),
(103,'Payroll System',80000);


# Employee–Project mapping table
CREATE TABLE employee_projects (
    emp_id INT,                  # employee id
    project_id INT,              # project id
    hours_worked INT,            # hours worked
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

# Insert employee-project data
INSERT INTO employee_projects VALUES
(1,101,40),
(1,102,30),
(2,103,20),
(3,101,50),
(3,102,25),
(4,103,35),
(5,103,30);


# Q1: Total hours worked by each employee
SELECT e.emp_id, e.emp_name, SUM(ep.hours_worked) AS total_hours FROM employees e JOIN employee_projects ep ON e.emp_id = ep.emp_id GROUP BY e.emp_id, e.emp_name;


# Q2: Total hours spent on each project
SELECT p.project_id, p.project_name, SUM(ep.hours_worked) AS total_hours FROM projects p JOIN employee_projects ep ON p.project_id = ep.project_id GROUP BY p.project_id, p.project_name;


# Q3: Department-wise total working hours
SELECT e.department, SUM(ep.hours_worked) AS total_hours FROM employees e JOIN employee_projects ep ON e.emp_id = ep.emp_id GROUP BY e.department;
