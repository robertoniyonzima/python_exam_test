-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 10, 2024 at 07:50 PM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `exam_python`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
CREATE TABLE IF NOT EXISTS `admins` (
  `id_admin` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `role` varchar(200) NOT NULL,
  `gender` varchar(200) NOT NULL,
  `password_admin` varchar(200) NOT NULL,
  PRIMARY KEY (`id_admin`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`id_admin`, `name`, `role`, `gender`, `password_admin`) VALUES
(1, 'BARANSEGETA', 'teacher', 'male', '123456'),
(2, 'GIRITEKA', 'headmaster', 'female', '654321'),
(3, 'IHORAHO', 'admin', 'male', '123456'),
(4, 'masumbuko', 'System Admin', 'male', '123456'),
(5, 'eliona', 'Teacher', 'female', '123456'),
(6, 'esperance', 'System Admin', 'female', '123456'),
(7, 'edidja', 'System Admin', 'female', '123456'),
(8, 'king', 'System Admin', 'male', '123456');

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
CREATE TABLE IF NOT EXISTS `courses` (
  `id_course` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `credits` int NOT NULL,
  PRIMARY KEY (`id_course`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`id_course`, `name`, `credits`) VALUES
(4, 'chemistry', 10),
(3, 'biology', 5);

-- --------------------------------------------------------

--
-- Table structure for table `grades`
--

DROP TABLE IF EXISTS `grades`;
CREATE TABLE IF NOT EXISTS `grades` (
  `id_grade` int NOT NULL AUTO_INCREMENT,
  `student_name` varchar(200) NOT NULL,
  `course_name` varchar(200) NOT NULL,
  `grades` int NOT NULL,
  PRIMARY KEY (`id_grade`),
  KEY `fk_student` (`student_name`),
  KEY `fk_cours` (`course_name`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `grades`
--

INSERT INTO `grades` (`id_grade`, `student_name`, `course_name`, `grades`) VALUES
(1, 'orly', 'biology', 5),
(2, 'cherissa', 'biology', 3),
(3, 'Gressy', 'biology', 4);

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
CREATE TABLE IF NOT EXISTS `students` (
  `id_student` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `age` int NOT NULL,
  `enrollment_number` int NOT NULL,
  `enrolled_course` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  PRIMARY KEY (`id_student`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id_student`, `name`, `age`, `enrollment_number`, `enrolled_course`, `password`) VALUES
(6, 'elvis', 21, 227542, '', ''),
(9, 'esperance', 12, 132680, 'Chemistry', '123456'),
(4, 'cresso', 12, 100970, 'Physics', '12345'),
(8, '', 0, 0, 'camping', '');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
