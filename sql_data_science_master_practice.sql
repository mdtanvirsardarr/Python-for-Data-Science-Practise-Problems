PRAGMA foreign_keys = ON;

/*
SQL Data Science Master Practice Script
Dialect: SQLite
Purpose: Create a realistic multi-table academic dataset and practise core SQL
concepts used in analytics work.
*/

/* -------------------------------------------------------------------------- */
/* Section 1: Remove old objects                                               */
/* -------------------------------------------------------------------------- */
DROP TABLE IF EXISTS assessment_results;
DROP TABLE IF EXISTS attendance;
DROP TABLE IF EXISTS assessments;
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS instructors;
DROP TABLE IF EXISTS departments;

/* -------------------------------------------------------------------------- */
/* Section 2: Create tables                                                    */
/* -------------------------------------------------------------------------- */
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL UNIQUE,
    building TEXT NOT NULL,
    annual_budget REAL NOT NULL
);

CREATE TABLE instructors (
    instructor_id INTEGER PRIMARY KEY,
    department_id INTEGER NOT NULL,
    instructor_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    hire_date TEXT NOT NULL,
    salary REAL NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    department_id INTEGER NOT NULL,
    instructor_id INTEGER,
    course_name TEXT NOT NULL,
    level TEXT NOT NULL,
    credits INTEGER NOT NULL,
    fee REAL NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
);

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    department_id INTEGER,
    student_name TEXT NOT NULL,
    gender TEXT,
    age INTEGER NOT NULL,
    city TEXT,
    email TEXT,
    enrol_date TEXT NOT NULL,
    graduation_date TEXT,
    gpa REAL,
    scholarship_amount REAL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enroll_date TEXT NOT NULL,
    status TEXT NOT NULL,
    final_mark REAL,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE assessments (
    assessment_id INTEGER PRIMARY KEY,
    course_id INTEGER NOT NULL,
    assessment_name TEXT NOT NULL,
    assessment_type TEXT NOT NULL,
    max_score REAL NOT NULL,
    due_date TEXT NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE assessment_results (
    result_id INTEGER PRIMARY KEY,
    assessment_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    score REAL,
    submitted_at TEXT,
    FOREIGN KEY (assessment_id) REFERENCES assessments(assessment_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

CREATE TABLE attendance (
    attendance_id INTEGER PRIMARY KEY,
    enrollment_id INTEGER NOT NULL,
    session_date TEXT NOT NULL,
    attendance_status TEXT NOT NULL,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id)
);

/* -------------------------------------------------------------------------- */
/* Section 3: Insert sample data                                               */
/* -------------------------------------------------------------------------- */
INSERT INTO departments (department_id, department_name, building, annual_budget) VALUES
(1, 'Data Science', 'North Block', 250000),
(2, 'Computer Science', 'Innovation Centre', 310000),
(3, 'Business Analytics', 'South Block', 225000),
(4, 'Mathematics', 'Science Hall', 180000),
(5, 'Artificial Intelligence', 'Innovation Centre', 340000),
(6, 'Cyber Security', 'Tech Tower', 275000),
(7, 'Software Engineering', 'Tech Tower', 290000),
(8, 'Economics', 'Central House', 205000);

INSERT INTO instructors (instructor_id, department_id, instructor_name, email, hire_date, salary) VALUES
(1, 1, 'Dr Amina Rahman', 'amina.rahman@univ.edu', '2018-09-01', 62000),
(2, 2, 'Dr John Carter', 'john.carter@univ.edu', '2017-02-15', 65000),
(3, 3, 'Dr Sarah Lee', 'sarah.lee@univ.edu', '2019-01-10', 60000),
(4, 4, 'Dr Michael Brown', 'michael.brown@univ.edu', '2016-05-20', 64000),
(5, 5, 'Dr Priya Patel', 'priya.patel@univ.edu', '2020-08-17', 67000),
(6, 6, 'Dr David Kim', 'david.kim@univ.edu', '2021-03-11', 61000),
(7, 7, 'Dr Emma Wilson', 'emma.wilson@univ.edu', '2018-11-05', 63000),
(8, 8, 'Dr Omar Khan', 'omar.khan@univ.edu', '2022-01-12', 59000),
(9, 1, 'Dr Noor Ali', 'noor.ali@univ.edu', '2023-04-01', 57000),
(10, 5, 'Dr Helen Moore', 'helen.moore@univ.edu', '2015-09-07', 70000);

INSERT INTO courses (course_id, department_id, instructor_id, course_name, level, credits, fee, start_date, end_date) VALUES
(101, 1, 1, 'SQL for Analytics', 'PG', 20, 900, '2025-01-15', '2025-05-10'),
(102, 1, 9, 'Machine Learning Foundations', 'PG', 20, 1200, '2025-01-18', '2025-05-15'),
(103, 2, 2, 'Database Systems', 'UG', 20, 850, '2025-01-20', '2025-05-20'),
(104, 3, 3, 'Business Intelligence', 'PG', 15, 950, '2025-02-01', '2025-05-30'),
(105, 4, 4, 'Applied Statistics', 'UG', 20, 800, '2025-01-22', '2025-05-18'),
(106, 5, 5, 'Natural Language Processing', 'PG', 20, 1300, '2025-02-05', '2025-06-01'),
(107, 6, 6, 'Network Security', 'UG', 20, 990, '2025-01-25', '2025-05-25'),
(108, 7, 7, 'Software Project Management', 'UG', 15, 870, '2025-02-03', '2025-05-28'),
(109, 8, 8, 'Econometrics', 'PG', 20, 1100, '2025-01-28', '2025-05-22'),
(110, 5, 10, 'Deep Learning Applications', 'PG', 20, 1400, '2025-02-10', '2025-06-05'),
(111, 2, NULL, 'Cloud Data Engineering', 'PG', 20, 1250, '2025-02-12', '2025-06-08'),
(112, 1, 1, 'Data Visualisation', 'UG', 15, 780, '2025-01-30', '2025-05-26');

INSERT INTO students (student_id, department_id, student_name, gender, age, city, email, enrol_date, graduation_date, gpa, scholarship_amount) VALUES
(1, 1, 'Ali Hasan', 'M', 21, 'London', 'ali.hasan@mail.com', '2024-09-15', NULL, 3.45, 1000),
(2, 2, 'Sara Ahmed', 'F', 22, 'Manchester', 'sara.ahmed@mail.com', '2024-09-15', NULL, 3.78, NULL),
(3, 1, 'John Smith', 'M', 20, 'London', 'john.smith@mail.com', '2024-09-15', NULL, 3.10, 500),
(4, 5, 'Mina Roy', 'F', 23, 'Birmingham', 'mina.roy@mail.com', '2024-09-15', NULL, 3.92, 1500),
(5, 2, 'David Kim', 'M', 21, 'Leeds', 'david.student@mail.com', '2024-09-15', NULL, 2.95, NULL),
(6, 5, 'Emma Jones', 'F', 22, 'London', 'emma.jones@mail.com', '2024-09-15', NULL, 3.88, 1200),
(7, 1, 'Noah Ali', 'M', 20, 'Manchester', 'noah.ali@mail.com', '2024-09-15', NULL, 2.75, NULL),
(8, 3, 'Lily Chen', 'F', 23, 'Leeds', 'lily.chen@mail.com', '2024-09-15', NULL, 3.96, 1800),
(9, 1, 'Ayan Uddin', 'M', 21, 'London', 'ayan.uddin@mail.com', '2024-09-15', NULL, 3.52, 700),
(10, 4, 'Zara Khan', 'F', 22, 'Birmingham', 'zara.khan@mail.com', '2024-09-15', NULL, 3.40, NULL),
(11, 6, 'Omar Faruk', 'M', 24, 'Sheffield', 'omar.faruk@mail.com', '2024-09-15', NULL, 3.18, NULL),
(12, 7, 'Nadia Begum', 'F', 21, 'Liverpool', 'nadia.begum@mail.com', '2024-09-15', NULL, 3.61, 950),
(13, 8, 'Lucas Green', 'M', 22, 'Bristol', 'lucas.green@mail.com', '2024-09-15', '2025-07-01', 3.29, NULL),
(14, 3, 'Sophia Noor', 'F', 23, NULL, 'sophia.noor@mail.com', '2024-09-15', NULL, 3.70, 1100),
(15, 1, 'Ali Hasan', 'M', 22, 'London', 'ali.hasan2@mail.com', '2024-09-15', NULL, 2.98, NULL),
(16, NULL, 'Rina Das', 'F', 20, 'Leicester', NULL, '2025-01-10', NULL, NULL, NULL);

INSERT INTO enrollments (enrollment_id, student_id, course_id, enroll_date, status, final_mark) VALUES
(1, 1, 101, '2025-01-16', 'Completed', 81),
(2, 1, 105, '2025-01-23', 'Completed', 76),
(3, 2, 103, '2025-01-21', 'Completed', 84),
(4, 2, 111, '2025-02-13', 'Active', NULL),
(5, 3, 101, '2025-01-16', 'Completed', 68),
(6, 3, 112, '2025-01-31', 'Active', NULL),
(7, 4, 106, '2025-02-06', 'Completed', 91),
(8, 4, 110, '2025-02-11', 'Active', NULL),
(9, 5, 103, '2025-01-21', 'Completed', 72),
(10, 5, 107, '2025-01-26', 'Active', NULL),
(11, 6, 106, '2025-02-06', 'Completed', 89),
(12, 6, 102, '2025-01-19', 'Completed', 87),
(13, 7, 101, '2025-01-16', 'Completed', 59),
(14, 7, 102, '2025-01-19', 'Active', NULL),
(15, 8, 104, '2025-02-02', 'Completed', 94),
(16, 8, 109, '2025-01-29', 'Completed', 90),
(17, 9, 101, '2025-01-16', 'Completed', 80),
(18, 9, 112, '2025-01-31', 'Completed', 83),
(19, 10, 105, '2025-01-23', 'Completed', 74),
(20, 10, 104, '2025-02-02', 'Completed', 79),
(21, 11, 107, '2025-01-26', 'Completed', 77),
(22, 11, 111, '2025-02-13', 'Active', NULL),
(23, 12, 108, '2025-02-04', 'Completed', 82),
(24, 12, 103, '2025-01-21', 'Completed', 75),
(25, 13, 109, '2025-01-29', 'Completed', 71),
(26, 13, 104, '2025-02-02', 'Completed', 69),
(27, 14, 104, '2025-02-02', 'Active', NULL),
(28, 14, 109, '2025-01-29', 'Completed', 88),
(29, 15, 101, '2025-01-16', 'Completed', 64),
(30, 16, 112, '2025-01-31', 'Active', NULL);

INSERT INTO assessments (assessment_id, course_id, assessment_name, assessment_type, max_score, due_date) VALUES
(1, 101, 'SQL Coursework', 'Coursework', 100, '2025-03-10'),
(2, 101, 'SQL Final Exam', 'Exam', 100, '2025-05-05'),
(3, 102, 'ML Assignment', 'Coursework', 100, '2025-03-18'),
(4, 103, 'Database Midterm', 'Exam', 100, '2025-03-20'),
(5, 104, 'Dashboard Report', 'Coursework', 100, '2025-04-01'),
(6, 105, 'Statistics Test', 'Exam', 100, '2025-03-25'),
(7, 106, 'NLP Project', 'Coursework', 100, '2025-04-10'),
(8, 107, 'Security Lab', 'Coursework', 100, '2025-03-28'),
(9, 108, 'Project Plan', 'Coursework', 100, '2025-04-05'),
(10, 109, 'Econometrics Exam', 'Exam', 100, '2025-05-02'),
(11, 110, 'Deep Learning Project', 'Coursework', 100, '2025-04-20'),
(12, 112, 'Visualisation Presentation', 'Coursework', 100, '2025-03-30');

INSERT INTO assessment_results (result_id, assessment_id, student_id, score, submitted_at) VALUES
(1, 1, 1, 84, '2025-03-09 10:30:00'),
(2, 2, 1, 79, '2025-05-05 14:00:00'),
(3, 4, 2, 86, '2025-03-20 09:00:00'),
(4, 1, 3, 70, '2025-03-10 11:15:00'),
(5, 7, 4, 93, '2025-04-09 16:00:00'),
(6, 7, 6, 90, '2025-04-10 13:30:00'),
(7, 3, 6, 88, '2025-03-18 12:40:00'),
(8, 1, 7, 60, '2025-03-10 08:55:00'),
(9, 5, 8, 95, '2025-03-31 17:10:00'),
(10, 10, 8, 92, '2025-05-02 15:00:00'),
(11, 1, 9, 82, '2025-03-10 10:45:00'),
(12, 12, 9, 85, '2025-03-30 11:00:00'),
(13, 6, 10, 76, '2025-03-25 10:00:00'),
(14, 8, 11, 79, '2025-03-28 09:30:00'),
(15, 9, 12, 83, '2025-04-05 14:10:00'),
(16, 10, 13, 73, '2025-05-02 14:20:00'),
(17, 5, 14, NULL, NULL),
(18, 1, 15, 66, '2025-03-10 12:00:00'),
(19, 12, 16, NULL, NULL),
(20, 11, 4, NULL, NULL);

INSERT INTO attendance (attendance_id, enrollment_id, session_date, attendance_status) VALUES
(1, 1, '2025-02-01', 'Present'),
(2, 1, '2025-02-08', 'Present'),
(3, 1, '2025-02-15', 'Absent'),
(4, 3, '2025-02-01', 'Present'),
(5, 3, '2025-02-08', 'Present'),
(6, 5, '2025-02-01', 'Late'),
(7, 5, '2025-02-08', 'Present'),
(8, 7, '2025-02-10', 'Present'),
(9, 7, '2025-02-17', 'Present'),
(10, 9, '2025-02-01', 'Absent'),
(11, 11, '2025-02-10', 'Present'),
(12, 11, '2025-02-17', 'Present'),
(13, 12, '2025-02-03', 'Present'),
(14, 13, '2025-02-01', 'Absent'),
(15, 15, '2025-02-06', 'Present'),
(16, 16, '2025-02-03', 'Present'),
(17, 17, '2025-02-01', 'Present'),
(18, 18, '2025-02-07', 'Late'),
(19, 19, '2025-02-04', 'Present'),
(20, 20, '2025-02-09', 'Present'),
(21, 21, '2025-02-02', 'Present'),
(22, 23, '2025-02-11', 'Present'),
(23, 24, '2025-02-01', 'Late'),
(24, 25, '2025-02-05', 'Present'),
(25, 26, '2025-02-09', 'Absent'),
(26, 28, '2025-02-05', 'Present'),
(27, 29, '2025-02-01', 'Absent'),
(28, 30, '2025-02-12', 'Present');

/* -------------------------------------------------------------------------- */
/* Section 4: Basic review queries                                             */
/* -------------------------------------------------------------------------- */

-- Question 1: Show all students.
SELECT * FROM students;

-- Question 2: Show student names and cities only.
SELECT student_name, city
FROM students;

-- Question 3: Show students from London.
SELECT student_name, city
FROM students
WHERE city = 'London';

-- Question 4: Show students aged 22 or above.
SELECT student_name, age
FROM students
WHERE age >= 22;

-- Question 5: Show students ordered by GPA from highest to lowest.
SELECT student_name, gpa
FROM students
ORDER BY gpa DESC;

-- Question 6: Show the first five students after sorting by name.
SELECT student_name, city
FROM students
ORDER BY student_name ASC
LIMIT 5;

/* -------------------------------------------------------------------------- */
/* Section 5: Missing filtering concepts                                       */
/* -------------------------------------------------------------------------- */

-- Question 7: Show students with GPA not equal to 3.45.
SELECT student_name, gpa
FROM students
WHERE gpa <> 3.45;

-- Question 8: Show students whose age is between 21 and 23.
SELECT student_name, age
FROM students
WHERE age BETWEEN 21 AND 23;

-- Question 9: Show courses with fees between 900 and 1300.
SELECT course_name, fee
FROM courses
WHERE fee BETWEEN 900 AND 1300
ORDER BY fee;

-- Question 10: Show students who live in London, Leeds, or Manchester.
SELECT student_name, city
FROM students
WHERE city IN ('London', 'Leeds', 'Manchester');

-- Question 11: Show students whose names start with A.
SELECT student_name
FROM students
WHERE student_name LIKE 'A%';

-- Question 12: Show students with missing city values.
SELECT student_id, student_name, city
FROM students
WHERE city IS NULL;

-- Question 13: Show students with missing email values.
SELECT student_id, student_name, email
FROM students
WHERE email IS NULL;

/* -------------------------------------------------------------------------- */
/* Section 6: Aggregate functions                                              */
/* -------------------------------------------------------------------------- */

-- Question 14: Count all students.
SELECT COUNT(*) AS total_students
FROM students;

-- Question 15: Count students with known scholarship amounts.
SELECT COUNT(scholarship_amount) AS students_with_scholarship_value
FROM students;

-- Question 16: Find the minimum and maximum GPA.
SELECT MIN(gpa) AS min_gpa,
       MAX(gpa) AS max_gpa
FROM students;

-- Question 17: Find the average GPA rounded to two decimal places.
SELECT ROUND(AVG(gpa), 2) AS average_gpa
FROM students;

-- Question 18: Find the total scholarship amount.
SELECT SUM(COALESCE(scholarship_amount, 0)) AS total_scholarship
FROM students;

/* -------------------------------------------------------------------------- */
/* Section 7: GROUP BY and HAVING                                              */
/* -------------------------------------------------------------------------- */

-- Question 19: Count students by city.
SELECT city, COUNT(*) AS total_students
FROM students
GROUP BY city
ORDER BY total_students DESC;

-- Question 20: Find average GPA by department.
SELECT department_id, ROUND(AVG(gpa), 2) AS average_gpa
FROM students
GROUP BY department_id
ORDER BY average_gpa DESC;

-- Question 21: Count students by city and gender.
SELECT city, gender, COUNT(*) AS total_students
FROM students
GROUP BY city, gender
ORDER BY city, gender;

-- Question 22: Show cities with at least two students.
SELECT city, COUNT(*) AS total_students
FROM students
GROUP BY city
HAVING COUNT(*) >= 2;

-- Question 23: Show departments where average GPA is above 3.5.
SELECT department_id, ROUND(AVG(gpa), 2) AS average_gpa
FROM students
GROUP BY department_id
HAVING AVG(gpa) > 3.5;

-- Question 24: Show cities where at least one student has a scholarship.
SELECT city,
       COUNT(*) AS total_students,
       SUM(CASE WHEN scholarship_amount IS NOT NULL THEN 1 ELSE 0 END) AS scholarship_holders
FROM students
GROUP BY city
HAVING SUM(CASE WHEN scholarship_amount IS NOT NULL THEN 1 ELSE 0 END) >= 1;

/* -------------------------------------------------------------------------- */
/* Section 8: JOINs and aliases                                                */
/* -------------------------------------------------------------------------- */

-- Question 25: Show student names with their department names.
SELECT s.student_name,
       d.department_name
FROM students AS s
INNER JOIN departments AS d
    ON s.department_id = d.department_id
ORDER BY s.student_name;

-- Question 26: Show course names with instructor names.
SELECT c.course_name,
       i.instructor_name
FROM courses AS c
LEFT JOIN instructors AS i
    ON c.instructor_id = i.instructor_id
ORDER BY c.course_name;

-- Question 27: Show each enrollment with student name, course name, and final mark.
SELECT e.enrollment_id,
       s.student_name,
       c.course_name,
       e.final_mark
FROM enrollments AS e
INNER JOIN students AS s
    ON e.student_id = s.student_id
INNER JOIN courses AS c
    ON e.course_id = c.course_id
ORDER BY e.enrollment_id;

-- Question 28: Show students who do not have a department.
SELECT s.student_name,
       d.department_name
FROM students AS s
LEFT JOIN departments AS d
    ON s.department_id = d.department_id
WHERE d.department_id IS NULL;

-- Question 29: Show departments and the number of courses in each department.
SELECT d.department_name,
       COUNT(c.course_id) AS total_courses
FROM departments AS d
LEFT JOIN courses AS c
    ON d.department_id = c.department_id
GROUP BY d.department_name
ORDER BY total_courses DESC;

-- Question 30: Self join example. Show pairs of students from the same city.
SELECT s1.student_name AS student_one,
       s2.student_name AS student_two,
       s1.city
FROM students AS s1
INNER JOIN students AS s2
    ON s1.city = s2.city
   AND s1.student_id < s2.student_id
WHERE s1.city IS NOT NULL
ORDER BY s1.city, s1.student_name, s2.student_name;

/* -------------------------------------------------------------------------- */
/* Section 9: NULL handling and CASE WHEN                                      */
/* -------------------------------------------------------------------------- */

-- Question 31: Replace missing city values with the word Unknown.
SELECT student_name,
       COALESCE(city, 'Unknown') AS city_cleaned
FROM students;

-- Question 32: Convert scholarship amount 0 to NULL using NULLIF.
SELECT student_name,
       scholarship_amount,
       NULLIF(scholarship_amount, 0) AS scholarship_nullif
FROM students;

-- Question 33: Classify students by GPA band.
SELECT student_name,
       gpa,
       CASE
           WHEN gpa >= 3.7 THEN 'Excellent'
           WHEN gpa >= 3.3 THEN 'Good'
           WHEN gpa >= 3.0 THEN 'Average'
           WHEN gpa IS NULL THEN 'Missing'
           ELSE 'Needs Support'
       END AS gpa_band
FROM students
ORDER BY gpa DESC;

-- Question 34: Count high performing students in each city.
SELECT COALESCE(city, 'Unknown') AS city,
       SUM(CASE WHEN gpa >= 3.5 THEN 1 ELSE 0 END) AS high_performing_students
FROM students
GROUP BY COALESCE(city, 'Unknown')
ORDER BY high_performing_students DESC;

/* -------------------------------------------------------------------------- */
/* Section 10: Subqueries                                                      */
/* -------------------------------------------------------------------------- */

-- Question 35: Show students whose GPA is above the overall average GPA.
SELECT student_name,
       gpa
FROM students
WHERE gpa > (
    SELECT AVG(gpa)
    FROM students
);

-- Question 36: Show students enrolled in courses taught by instructors from department 1.
SELECT student_name
FROM students
WHERE student_id IN (
    SELECT e.student_id
    FROM enrollments AS e
    INNER JOIN courses AS c
        ON e.course_id = c.course_id
    WHERE c.department_id = 1
);

-- Question 37: EXISTS example. Show students who have at least one enrollment.
SELECT s.student_name
FROM students AS s
WHERE EXISTS (
    SELECT 1
    FROM enrollments AS e
    WHERE e.student_id = s.student_id
);

-- Question 38: NOT EXISTS example. Show students with no assessment result yet.
SELECT s.student_name
FROM students AS s
WHERE NOT EXISTS (
    SELECT 1
    FROM assessment_results AS ar
    WHERE ar.student_id = s.student_id
);

-- Question 39: Correlated subquery. Show students whose GPA is above the average GPA of their own department.
SELECT s.student_name,
       s.department_id,
       s.gpa
FROM students AS s
WHERE s.gpa > (
    SELECT AVG(s2.gpa)
    FROM students AS s2
    WHERE s2.department_id = s.department_id
);

/* -------------------------------------------------------------------------- */
/* Section 11: CTEs                                                            */
/* -------------------------------------------------------------------------- */

-- Question 40: Use a CTE to find average final marks by course.
WITH course_average AS (
    SELECT c.course_name,
           ROUND(AVG(e.final_mark), 2) AS average_final_mark
    FROM courses AS c
    LEFT JOIN enrollments AS e
        ON c.course_id = e.course_id
    GROUP BY c.course_name
)
SELECT *
FROM course_average
ORDER BY average_final_mark DESC;

-- Question 41: Use two CTEs to find departments with the highest student counts.
WITH student_count AS (
    SELECT department_id,
           COUNT(*) AS total_students
    FROM students
    GROUP BY department_id
),
labelled_departments AS (
    SELECT d.department_name,
           sc.total_students
    FROM student_count AS sc
    LEFT JOIN departments AS d
        ON sc.department_id = d.department_id
)
SELECT *
FROM labelled_departments
ORDER BY total_students DESC;

-- Question 42: Recursive CTE example. Generate numbers from 1 to 10.
WITH RECURSIVE numbers(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1
    FROM numbers
    WHERE n < 10
)
SELECT *
FROM numbers;

/* -------------------------------------------------------------------------- */
/* Section 12: Window functions                                                */
/* -------------------------------------------------------------------------- */

-- Question 43: Assign a row number to students ordered by GPA.
SELECT student_name,
       gpa,
       ROW_NUMBER() OVER (ORDER BY gpa DESC) AS row_num
FROM students
WHERE gpa IS NOT NULL;

-- Question 44: Rank students by GPA with ties.
SELECT student_name,
       gpa,
       RANK() OVER (ORDER BY gpa DESC) AS gpa_rank
FROM students
WHERE gpa IS NOT NULL;

-- Question 45: Dense rank students by GPA with ties.
SELECT student_name,
       gpa,
       DENSE_RANK() OVER (ORDER BY gpa DESC) AS gpa_dense_rank
FROM students
WHERE gpa IS NOT NULL;

-- Question 46: Rank students within each city.
SELECT student_name,
       city,
       gpa,
       RANK() OVER (PARTITION BY city ORDER BY gpa DESC) AS city_rank
FROM students
WHERE gpa IS NOT NULL
ORDER BY city, city_rank;

-- Question 47: Show previous and next GPA values after ordering by GPA.
SELECT student_name,
       gpa,
       LAG(gpa) OVER (ORDER BY gpa) AS previous_gpa,
       LEAD(gpa) OVER (ORDER BY gpa) AS next_gpa
FROM students
WHERE gpa IS NOT NULL;

-- Question 48: Calculate running fee total by course start date.
SELECT course_name,
       start_date,
       fee,
       SUM(fee) OVER (
           ORDER BY start_date
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_fee_total
FROM courses
ORDER BY start_date;

-- Question 49: Show first and last GPA within each city.
SELECT student_name,
       city,
       gpa,
       FIRST_VALUE(gpa) OVER (
           PARTITION BY city
           ORDER BY gpa DESC
       ) AS highest_city_gpa,
       LAST_VALUE(gpa) OVER (
           PARTITION BY city
           ORDER BY gpa DESC
           ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
       ) AS lowest_city_gpa
FROM students
WHERE city IS NOT NULL AND gpa IS NOT NULL
ORDER BY city, gpa DESC;

/* -------------------------------------------------------------------------- */
/* Section 13: Date and time functions                                         */
/* -------------------------------------------------------------------------- */

-- Question 50: Show the current date.
SELECT DATE('now') AS current_date;

-- Question 51: Extract year and month from course start dates.
SELECT course_name,
       start_date,
       strftime('%Y', start_date) AS start_year,
       strftime('%m', start_date) AS start_month
FROM courses;

-- Question 52: Find the number of days each course runs.
SELECT course_name,
       start_date,
       end_date,
       CAST(julianday(end_date) - julianday(start_date) AS INTEGER) AS duration_days
FROM courses;

-- Question 53: Show enrollments made in February 2025.
SELECT enrollment_id,
       student_id,
       course_id,
       enroll_date
FROM enrollments
WHERE strftime('%Y-%m', enroll_date) = '2025-02';

-- Question 54: Show assessments due in March or April 2025.
SELECT assessment_name,
       due_date
FROM assessments
WHERE due_date BETWEEN '2025-03-01' AND '2025-04-30'
ORDER BY due_date;

/* -------------------------------------------------------------------------- */
/* Section 14: CAST, string functions, and cleaning                            */
/* -------------------------------------------------------------------------- */

-- Question 55: Cast GPA to text.
SELECT student_name,
       gpa,
       CAST(gpa AS TEXT) AS gpa_text
FROM students;

-- Question 56: Round final marks to whole numbers.
SELECT enrollment_id,
       final_mark,
       ROUND(final_mark, 0) AS rounded_mark
FROM enrollments
WHERE final_mark IS NOT NULL;

-- Question 57: Convert student names to uppercase and lowercase.
SELECT student_name,
       UPPER(student_name) AS student_name_upper,
       LOWER(student_name) AS student_name_lower
FROM students;

-- Question 58: Trim spaces and measure string length.
SELECT '   SQL Practice   ' AS raw_text,
       TRIM('   SQL Practice   ') AS trimmed_text,
       LENGTH(TRIM('   SQL Practice   ')) AS trimmed_length;

-- Question 59: Extract the first four letters of each course name.
SELECT course_name,
       SUBSTR(course_name, 1, 4) AS first_four_letters
FROM courses;

/* -------------------------------------------------------------------------- */
/* Section 15: Set operations                                                  */
/* -------------------------------------------------------------------------- */

-- Question 60: UNION example. Show distinct cities from students and department buildings.
SELECT city AS place
FROM students
WHERE city IS NOT NULL
UNION
SELECT building AS place
FROM departments;

-- Question 61: UNION ALL example. Keep duplicates while combining places.
SELECT city AS place
FROM students
WHERE city IS NOT NULL
UNION ALL
SELECT building AS place
FROM departments;

-- Question 62: INTERSECT example. Show names that appear in both students and instructors.
SELECT student_name AS person_name
FROM students
INTERSECT
SELECT instructor_name AS person_name
FROM instructors;

-- Question 63: EXCEPT example. Show student cities that are not used as department buildings.
SELECT city AS value_name
FROM students
WHERE city IS NOT NULL
EXCEPT
SELECT building AS value_name
FROM departments;

/* -------------------------------------------------------------------------- */
/* Section 16: Duplicate checking                                              */
/* -------------------------------------------------------------------------- */

-- Question 64: Check duplicate student names.
SELECT student_name,
       COUNT(*) AS duplicate_count
FROM students
GROUP BY student_name
HAVING COUNT(*) > 1;

-- Question 65: Check whether one student appears in many course enrollments.
SELECT student_id,
       COUNT(*) AS total_enrollments
FROM enrollments
GROUP BY student_id
HAVING COUNT(*) > 1
ORDER BY total_enrollments DESC;

/* -------------------------------------------------------------------------- */
/* Section 17: DDL and DML practice                                            */
/* -------------------------------------------------------------------------- */

-- Question 66: Create a view for completed enrollments.
DROP VIEW IF EXISTS completed_enrollments_view;
CREATE VIEW completed_enrollments_view AS
SELECT e.enrollment_id,
       s.student_name,
       c.course_name,
       e.final_mark
FROM enrollments AS e
INNER JOIN students AS s
    ON e.student_id = s.student_id
INNER JOIN courses AS c
    ON e.course_id = c.course_id
WHERE e.status = 'Completed';

SELECT *
FROM completed_enrollments_view
ORDER BY final_mark DESC;

-- Question 67: Update missing city for Sophia Noor.
UPDATE students
SET city = 'Not Provided'
WHERE student_name = 'Sophia Noor'
  AND city IS NULL;

SELECT student_name, city
FROM students
WHERE student_name = 'Sophia Noor';

-- Question 68: Demonstrate ALTER TABLE by adding a phone column.
ALTER TABLE students ADD COLUMN phone TEXT;

UPDATE students
SET phone = CASE
    WHEN student_id IN (1, 2, 3) THEN '07000000001'
    WHEN student_id IN (4, 5, 6) THEN '07000000002'
    ELSE NULL
END;

SELECT student_id, student_name, phone
FROM students
ORDER BY student_id;

-- Question 69: Insert a new student record.
INSERT INTO students (
    student_id, department_id, student_name, gender, age, city, email,
    enrol_date, graduation_date, gpa, scholarship_amount, phone
) VALUES (
    17, 2, 'Farhan Malik', 'M', 22, 'Bradford', 'farhan.malik@mail.com',
    '2025-01-15', NULL, 3.22, NULL, '07000000003'
);

SELECT student_id, student_name, city, gpa
FROM students
WHERE student_id = 17;

-- Question 70: Delete the temporary inserted student record.
DELETE FROM students
WHERE student_id = 17;

SELECT student_id, student_name
FROM students
WHERE student_id = 17;

/* -------------------------------------------------------------------------- */
/* Section 18: Indexes and query plans                                         */
/* -------------------------------------------------------------------------- */

-- Question 71: Create indexes on common filter columns.
CREATE INDEX IF NOT EXISTS idx_students_city ON students(city);
CREATE INDEX IF NOT EXISTS idx_students_department_id ON students(department_id);
CREATE INDEX IF NOT EXISTS idx_enrollments_student_id ON enrollments(student_id);
CREATE INDEX IF NOT EXISTS idx_courses_department_id ON courses(department_id);
CREATE INDEX IF NOT EXISTS idx_assessment_results_student_id ON assessment_results(student_id);

-- Question 72: Review the query plan for filtering by city.
EXPLAIN QUERY PLAN
SELECT student_name, city
FROM students
WHERE city = 'London';

-- Question 73: Review the query plan for joining enrollments and students.
EXPLAIN QUERY PLAN
SELECT e.enrollment_id,
       s.student_name
FROM enrollments AS e
INNER JOIN students AS s
    ON e.student_id = s.student_id
WHERE e.student_id = 1;

/* -------------------------------------------------------------------------- */
/* Section 19: Dialect difference notes                                        */
/* -------------------------------------------------------------------------- */

/*
Question 74: How does row limiting differ by dialect?
SQLite answer:
SELECT * FROM students LIMIT 5;

PostgreSQL answer:
SELECT * FROM students LIMIT 5;

SQL Server answer:
SELECT TOP 5 * FROM students;

Question 75: How do date functions differ by dialect?
SQLite answer:
SELECT strftime('%Y', start_date) FROM courses;

PostgreSQL answer:
SELECT EXTRACT(YEAR FROM start_date) FROM courses;

SQL Server answer:
SELECT YEAR(start_date) FROM courses;

Question 76: How do null replacement functions differ by dialect?
SQLite answer:
SELECT COALESCE(city, 'Unknown') FROM students;

PostgreSQL answer:
SELECT COALESCE(city, 'Unknown') FROM students;

SQL Server answer:
SELECT ISNULL(city, 'Unknown') FROM students;
*/

/* -------------------------------------------------------------------------- */
/* Section 20: Mini business style tasks                                       */
/* -------------------------------------------------------------------------- */

-- Question 77: Show the top three students by GPA in each city.
WITH ranked_students AS (
    SELECT student_name,
           city,
           gpa,
           ROW_NUMBER() OVER (PARTITION BY city ORDER BY gpa DESC) AS city_position
    FROM students
    WHERE city IS NOT NULL AND gpa IS NOT NULL
)
SELECT *
FROM ranked_students
WHERE city_position <= 3
ORDER BY city, city_position;

-- Question 78: Show the latest submitted assessment for each student.
WITH latest_submission AS (
    SELECT student_id,
           assessment_id,
           score,
           submitted_at,
           ROW_NUMBER() OVER (
               PARTITION BY student_id
               ORDER BY submitted_at DESC
           ) AS rn
    FROM assessment_results
    WHERE submitted_at IS NOT NULL
)
SELECT ls.student_id,
       s.student_name,
       ls.assessment_id,
       ls.score,
       ls.submitted_at
FROM latest_submission AS ls
INNER JOIN students AS s
    ON ls.student_id = s.student_id
WHERE ls.rn = 1
ORDER BY ls.student_id;

-- Question 79: Show each department with total students, average GPA, and average scholarship amount.
SELECT d.department_name,
       COUNT(s.student_id) AS total_students,
       ROUND(AVG(s.gpa), 2) AS average_gpa,
       ROUND(AVG(s.scholarship_amount), 2) AS average_scholarship
FROM departments AS d
LEFT JOIN students AS s
    ON d.department_id = s.department_id
GROUP BY d.department_name
ORDER BY total_students DESC;

-- Question 80: Show students at risk based on GPA below 3.0 or missing GPA.
SELECT student_name,
       gpa,
       CASE
           WHEN gpa IS NULL THEN 'Missing GPA'
           WHEN gpa < 3.0 THEN 'At Risk'
           ELSE 'Not At Risk'
       END AS risk_status
FROM students
ORDER BY gpa ASC;
