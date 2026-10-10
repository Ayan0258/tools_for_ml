CREATE TABLE student (
    student_id INT,
    name VARCHAR(20),
    major VARCHAR(20),
    PRIMARY KEY (student_id)
);

SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'student';

DROP TABLE student;

ALTER TABLE student ADD gpa decimal(3, 2);
