-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 11, 2022 at 02:41 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_mahasiswa`
--

-- --------------------------------------------------------

--
-- Table structure for table `datamahasiswa`
--

CREATE TABLE `datamahasiswa` (
  `id_mahasiswa` int(11) NOT NULL,
  `nim` int(10) NOT NULL,
  `nama_mahasiswa` varchar(100) NOT NULL,
  `fakultas` varchar(20) DEFAULT NULL,
  `prodi` varchar(20) DEFAULT NULL,
  `phone` int(20) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `alamat` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `datamahasiswa`
--

INSERT INTO `datamahasiswa` (`id_mahasiswa`, `nim`, `nama_mahasiswa`, `fakultas`, `prodi`, `phone`, `email`, `alamat`) VALUES
(1, 44368734, 'FIKRI HADI NUGRAHA', 'Sains dan Teknologi', 'Sistem Informasi', 08121842, 'fikri123@gmail.com', 'SERANG'),
(2, 44368735, 'MUHAMMAD IQBAL', 'Sains dan Teknologi', 'Sistem Informasi', 08121843, 'iqbal@gmail.com', 'PAMARAYAN'),
(3, 44368735, 'SAEFULLAH', 'Sains dan Teknologi', 'Sistem Informasi', 08121841, 'saef@gmail.com', 'PONTANG');

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
