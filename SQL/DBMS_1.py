# Login to MySQL
mysql -u root -p

# Create database
CREATE DATABASE school;

# Use the database
USE school;

# Create students table
CREATE TABLE students (
    id INT,
    name VARCHAR(50),
    rollno INT
);

# Insert data into students table
INSERT INTO students VALUES (1, "rollno", 21);

# Display all students
SELECT * FROM students;

# Display student with id = 1
SELECT * FROM students WHERE id = 1;

# Create a new table called class
CREATE TABLE class (
    id INT,
    name VARCHAR(50),
    age INT,
    course VARCHAR(50),
    marks INT
);

# Insert single record
INSERT INTO class VALUES (1, "Manish", 18, "SQL", 78);

# Insert multiple records
INSERT INTO class VALUES
(2, "Shivashish", 20, "SQL", 98),
(3, "Srijan", 20, "SQL", 95),
(4, "Ayush", 20, "SQL", 92);

# Display all records
SELECT * FROM class;

# Display name and marks only
SELECT name, marks FROM class;

# Order records by marks (descending)
SELECT * FROM class ORDER BY marks DESC;

# Order records by marks (ascending)
SELECT * FROM class ORDER BY marks ASC;

# Get students with marks greater than 90
SELECT * FROM class WHERE marks > 90;

# Calculate average marks
SELECT AVG(marks) FROM class;

# Find minimum marks
SELECT MIN(marks) FROM class;

# Count total number of records
SELECT COUNT(*) FROM class;

# AND condition example
SELECT marks FROM class WHERE id = 2 AND marks = 98;

# Delete record with id = 3
DELETE FROM class WHERE id = 3;

# Display top 2 records with lowest marks
SELECT * FROM class ORDER BY marks ASC LIMIT 2;

# Update marks for id = 1
UPDATE class SET marks = 33 WHERE id = 1;

# Display updated table
SELECT * FROM class;

# Average marks course-wise
SELECT course, AVG(marks) FROM class GROUP BY course;

# Update course names based on marks
UPDATE class SET course = "python" WHERE marks = 98;
UPDATE class SET course = "java" WHERE marks = 92;
UPDATE class SET course = "c++" WHERE marks = 75;
UPDATE class SET course = "DSA" WHERE marks = 50;

# Average marks after updates
SELECT course, AVG(marks) FROM class GROUP BY course;

# Average and maximum marks age-wise
SELECT age, AVG(marks), MAX(marks)
FROM class
GROUP BY age;

# Average and maximum marks by age and course
SELECT age, course, AVG(marks), MAX(marks)
FROM class
GROUP BY age, course;

# Average age and minimum marks by name and id
SELECT name, id, AVG(age) AS avg_age, MIN(marks) AS min_marks
FROM class
GROUP BY name, id;
