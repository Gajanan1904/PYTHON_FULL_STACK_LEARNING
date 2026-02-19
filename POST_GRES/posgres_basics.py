# Check PostgreSQL version
psql --version


# Login to PostgreSQL
psql -U postgres


# Create a new database
CREATE DATABASE psq1;


# Connect to database psq1
\c psq1


# Create students table
CREATE TABLE students (
    id INT,
    name VARCHAR(50),
    age INT
);


# Show list of tables
\dt
# Schema |   Name   | Type  |  Owner
# public | students | table | postgres


# Insert initial records
INSERT INTO students VALUES (1, 'RAM', 50);
INSERT INTO students VALUES (2, 'OM', 21);


# Display all records
SELECT * FROM students;


# Insert another record
INSERT INTO students VALUES (3, 'RAVI', 22);


# View updated table
SELECT * FROM students;
# id | name | age
# 1  | RAM  | 50
# 2  | OM   | 21
# 3  | RAVI | 22


# Update age where name is OM
UPDATE students
SET age = 23
WHERE name = 'OM';


# Check updated records
SELECT * FROM students;
# id | name | age
# 1  | RAM  | 50
# 3  | RAVI | 22
# 2  | OM   | 23


# Delete record with id = 1
DELETE FROM students
WHERE id = 1;


# Verify deletion
SELECT * FROM students;
# id | name | age
# 3  | RAVI | 22
# 2  | OM   | 23


# Start transaction
BEGIN;


# Insert inside transaction
INSERT INTO students VALUES (4, 'ANITA', 20);


# Create savepoint
SAVEPOINT sp1;


# Update after savepoint
UPDATE students
SET age = 25
WHERE id = 2;


# Rollback update only
ROLLBACK TO sp1;


# Rollback entire transaction
ROLLBACK;


# Final table state
SELECT * FROM students;
# id | name | age
# 3  | RAVI | 22
# 2  | OM   | 23
