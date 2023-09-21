-- schema
create table student (
    student_id      INT PRIMARY KEY,
    student_name    VARCHAR(100),
    student_birth   DATE,
    student_gender  SMALLINT,

    year_of_enrollment  INT,
    major               VARCHAR(100)
);
COMMENT ON TABLE student IS '学生信息表';
COMMENT ON COLUMN student.student_name IS '学生姓名';
COMMENT ON COLUMN student.student_birth IS '出生日期';
COMMENT ON COLUMN student.student_gender IS '性别 1.男 2.女';
COMMENT ON COLUMN student.major IS '专业';
COMMENT ON COLUMN student.year_of_enrollment IS '入学年份';


CREATE TABLE course (
    course_id    INT PRIMARY KEY,
    course_name  VARCHAR(100),
    credit       FLOAT
);
COMMENT ON TABLE course IS '课程信息表';
COMMENT ON COLUMN course.course_name IS '课程名称';
COMMENT ON COLUMN course.credit IS '学分';


CREATE TABLE score (
    student_id INT,
    course_id  INT,
    score      INT,
    semester   VARCHAR(50),
    PRIMARY KEY (student_id, course_id)
);
COMMENT ON TABLE score IS '学生成绩表';
COMMENT ON COLUMN score.score IS '得分';
COMMENT ON COLUMN score.semester IS '学期，取值例子如：2021年春季，2020年秋季等';


-- sample data
INSERT INTO student (student_id, student_name, student_birth, student_gender, year_of_enrollment, major) VALUES
(1, '张三', '1995-07-08', 1, 2020, '计算机科学'),
(2, '李四', '1996-01-11', 1, 2021, '计算机科学'),
(3, '王五', '1992-02-10', 1, 2021, '物理学'),
(4, '赵六', '1991-06-18', 2, 2021, '数学'),
(5, '周七', '1994-11-20', 1, 2021, '计算机科学'),
(6, '吴八', '1995-09-13', 1, 2021, '物理学'),
(7, '郑九', '1993-03-29', 2, 2021, '数学'),
(8, '孙十', '1991-06-04', 1, 2021, '计算机科学'),
(9, '刘十一', '1992-05-11', 2, 2021, '物理学'),
(10, '陈十二', '1994-12-21', 1, 2021, '数学');

INSERT INTO course (course_id, course_name, credit) VALUES
(1, '计算机基础', 3),
(2, '数据结构', 4),
(3, '高等物理', 3),
(4, '线性代数', 4),
(5, '微积分', 5),
(6, '编程语言', 4),
(7, '量子力学', 3),
(8, '概率论', 4),
(9, '数据库系统', 4),
(10, '计算机网络', 4);

INSERT INTO score (student_id, course_id, score, semester) VALUES
(1, 1, 90, '2020年秋季'),
(1, 2, 85, '2021年春季'),
(2, 1, 88, '2021年秋季'),
(2, 2, 90, '2022年春季'),
(3, 3, 92, '2020年秋季'),
(3, 4, 85, '2021年春季'),
(4, 3, 88, '2021年秋季'),
(4, 4, 86, '2022年春季'),
(5, 1, 90, '2022年秋季'),
(5, 2, 87, '2023年春季');
