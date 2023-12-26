
CREATE TABLE teachers
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    subject_id INTEGER,
    FOREIGN KEY(subject_id) REFERENCES subjects(id)
);


CREATE TABLE students
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    password_hash TEXT NOT NULL,
    name TEXT NOT NULL
);

CREATE TABLE subjects
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE students_grades
(
    student_id INTEGER,
    subject_id INTEGER,
    time TEXT NOT NULL,
    grade INTEGER NOT NULL,
    FOREIGN KEY(subject_id) REFERENCES subjects(id),
    FOREIGN KEY(student_id) REFERENCES students(id)
);



INSERT INTO subjects(name) VALUES ('math'),('english'),('phisics'),('computer sceince'),('history');
