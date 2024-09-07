CREATE DATABASE IF NOT EXISTS gestion_ecole;
USE gestion_ecole;

CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    matricule VARCHAR(50) NOT NULL,
    nom VARCHAR(100) NOT NULL,
    post_nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    promotion VARCHAR(50) NOT NULL,
    faculte VARCHAR(100) NOT NULL
);


CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    intitule VARCHAR(100) NOT NULL,
    code VARCHAR(50) NOT NULL,
    credit INT NOT NULL,
    category VARCHAR(50),
    semestre VARCHAR(50)
);


CREATE TABLE IF NOT EXISTS school_years (
    school_year_id INT AUTO_INCREMENT PRIMARY KEY,
    intitule VARCHAR(100) NOT NULL,
    date_debut DATE NOT NULL,
    date_fin DATE NOT NULL
);


CREATE TABLE IF NOT EXISTS sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(50) NOT NULL,
    note DECIMAL(5, 2) NOT NULL
);
