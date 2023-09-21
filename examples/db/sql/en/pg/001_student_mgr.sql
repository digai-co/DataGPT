-- schema
create table student (
    student_id      INT PRIMARY KEY,
    student_name    VARCHAR(100),
    student_birth   DATE,
    student_gender  SMALLINT,

    year_of_enrollment  INT,
    major               VARCHAR(100)
);
COMMENT ON TABLE student IS 'Student Information';
COMMENT ON COLUMN student.student_name IS 'Student Name';
COMMENT ON COLUMN student.student_birth IS 'Date of Birth';
COMMENT ON COLUMN student.student_gender IS 'Gender 1. Male 2. Female';
COMMENT ON COLUMN student.major IS 'Major';
COMMENT ON COLUMN student.year_of_enrollment IS 'Year of Enrollment';


CREATE TABLE course (
    course_id    INT PRIMARY KEY,
    course_name  VARCHAR(100),
    credit       FLOAT
);
COMMENT ON TABLE course IS 'Course Information';
COMMENT ON COLUMN course.course_name IS 'Course Name';
COMMENT ON COLUMN course.credit IS 'Credit';


CREATE TABLE score (
    student_id INT,
    course_id  INT,
    score      INT,
    semester   VARCHAR(50),
    PRIMARY KEY (student_id, course_id)
);
COMMENT ON TABLE score IS 'Student Score';
COMMENT ON COLUMN score.score IS 'Score';
COMMENT ON COLUMN score.semester IS 'Semester;e.g., Spring 2021, Fall 2020, etc.';


-- sample data
INSERT INTO student (student_id, student_name, student_birth, student_gender, year_of_enrollment, major) VALUES
(1, 'John Smith', '1995-07-08', 1, 2020, 'Computer Science'),
(2, 'Jane Doe', '1996-01-11', 1, 2021, 'Computer Science'),
(3, 'David Wang', '1992-02-10', 1, 2021, 'Physics'),
(4, 'Linda Zhao', '1991-06-18', 2, 2021, 'Mathematics'),
(5, 'Michael Zhou', '1994-11-20', 1, 2021, 'Computer Science'),
(6, 'Emily Wu', '1995-09-13', 1, 2021, 'Physics'),
(7, 'Brian Zheng', '1993-03-29', 2, 2021, 'Mathematics'),
(8, 'Sarah Sun', '1991-06-04', 1, 2021, 'Computer Science'),
(9, 'Lisa Liu', '1992-05-11', 2, 2021, 'Physics'),
(10, 'Chris Chen', '1994-12-21', 1, 2021, 'Mathematics');


INSERT INTO course (course_id, course_name, credit) VALUES
(1, 'Computer Fundamentals', 3),
(2, 'Data Structures', 4),
(3, 'Advanced Physics', 3),
(4, 'Linear Algebra', 4),
(5, 'Calculus', 5),
(6, 'Programming Languages', 4),
(7, 'Quantum Mechanics', 3),
(8, 'Probability Theory', 4),
(9, 'Database Systems', 4),
(10, 'Computer Networking', 4);


INSERT INTO score (student_id, course_id, score, semester) VALUES
(1, 1, 90, 'Fall 2020'),
(1, 2, 85, 'Spring 2021'),
(2, 1, 88, 'Fall 2021'),
(2, 2, 90, 'Spring 2022'),
(3, 3, 92, 'Fall 2020'),
(3, 4, 85, 'Spring 2021'),
(4, 3, 88, 'Fall 2021'),
(4, 4, 86, 'Spring 2022'),
(5, 1, 90, 'Fall 2022'),
(5, 2, 87, 'Spring 2023');
