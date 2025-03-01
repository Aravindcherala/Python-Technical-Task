CREATE TABLE employees (
    id INT PRIMARY KEY,  
    name VARCHAR(100),
    age INT,
    email VARCHAR(100) UNIQUE,
    department VARCHAR(50),
    salary DECIMAL(10,2)
);