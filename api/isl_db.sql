-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 25, 2021 at 09:06 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `isl_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `admin_nik` varchar(15) NOT NULL,
  `admin_name` varchar(50) NOT NULL,
  `adress` text NOT NULL,
  `phone` int(15) NOT NULL,
  `created_date` datetime NOT NULL,
  `last_access` datetime NOT NULL,
  `email` varchar(20) NOT NULL,
  `username` varchar(15) NOT NULL,
  `password` text NOT NULL,
  `workspace_id` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `admin_nik`, `admin_name`, `adress`, `phone`, `created_date`, `last_access`, `email`, `username`, `password`, `workspace_id`) VALUES
(3, '1234', 'achmad fathoni', 'jl.bata kuli', 2147483647, '2020-09-14 00:00:00', '2020-09-27 20:57:56', 'sr@.com', 'usr37', 'd404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db', 1);

-- --------------------------------------------------------

--
-- Table structure for table `container`
--

CREATE TABLE `container` (
  `container_id` int(11) NOT NULL,
  `container_type` varchar(15) NOT NULL,
  `container_size` varchar(15) NOT NULL,
  `container_color` varchar(15) NOT NULL,
  `container_cost` varchar(15) NOT NULL,
  `importer_id` int(2) NOT NULL,
  `customer_id` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `container`
--

INSERT INTO `container` (`container_id`, `container_type`, `container_size`, `container_color`, `container_cost`, `importer_id`, `customer_id`) VALUES
(1, 'small', '10', 'black', '10000', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL,
  `customer_name` varchar(20) NOT NULL,
  `customer_description` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customer_id`, `customer_name`, `customer_description`) VALUES
(1, 'unilever', 'food'),
(3, 'wings', 'food beverages');

-- --------------------------------------------------------

--
-- Table structure for table `importer`
--

CREATE TABLE `importer` (
  `importer_id` int(11) NOT NULL,
  `importer_name` varchar(15) NOT NULL,
  `importer_description` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `importer`
--

INSERT INTO `importer` (`importer_id`, `importer_name`, `importer_description`) VALUES
(1, 'jne', 'logistic');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle`
--

CREATE TABLE `vehicle` (
  `vehicle_id` int(11) NOT NULL,
  `vehicle_driver` varchar(15) NOT NULL,
  `vehicle_type` varchar(15) NOT NULL,
  `vehicle_size` varchar(15) NOT NULL,
  `vehicle_logistic_schema` varchar(15) NOT NULL,
  `vehicle_cost` varchar(15) NOT NULL,
  `customer_id` int(2) NOT NULL,
  `importer_id` int(2) NOT NULL,
  `container_id` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicle`
--

INSERT INTO `vehicle` (`vehicle_id`, `vehicle_driver`, `vehicle_type`, `vehicle_size`, `vehicle_logistic_schema`, `vehicle_cost`, `customer_id`, `importer_id`, `container_id`) VALUES
(1, 'slamet', 'fuso', '5', '2', '20000', 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `workspace`
--

CREATE TABLE `workspace` (
  `workspace_id` int(2) NOT NULL,
  `admin` int(2) NOT NULL,
  `logging` int(2) NOT NULL,
  `transaction` int(2) NOT NULL,
  `vehicle` int(2) NOT NULL,
  `container` int(2) NOT NULL,
  `importer` int(2) NOT NULL,
  `customer` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `workspace`
--

INSERT INTO `workspace` (`workspace_id`, `admin`, `logging`, `transaction`, `vehicle`, `container`, `importer`, `customer`) VALUES
(2, 1, 0, 0, 0, 0, 0, 0),
(3, 0, 1, 0, 0, 0, 0, 0),
(4, 0, 0, 1, 0, 0, 0, 0),
(5, 0, 0, 0, 1, 0, 0, 0),
(6, 0, 0, 0, 0, 1, 0, 0),
(7, 0, 0, 0, 0, 0, 1, 0),
(8, 0, 0, 0, 0, 0, 0, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `admin_nik` (`admin_nik`);

--
-- Indexes for table `container`
--
ALTER TABLE `container`
  ADD PRIMARY KEY (`container_id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customer_id`),
  ADD UNIQUE KEY `customer_name` (`customer_name`);

--
-- Indexes for table `importer`
--
ALTER TABLE `importer`
  ADD PRIMARY KEY (`importer_id`),
  ADD UNIQUE KEY `importer_name` (`importer_name`);

--
-- Indexes for table `vehicle`
--
ALTER TABLE `vehicle`
  ADD PRIMARY KEY (`vehicle_id`);

--
-- Indexes for table `workspace`
--
ALTER TABLE `workspace`
  ADD UNIQUE KEY `workspace_id` (`workspace_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `container`
--
ALTER TABLE `container`
  MODIFY `container_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `importer`
--
ALTER TABLE `importer`
  MODIFY `importer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `vehicle`
--
ALTER TABLE `vehicle`
  MODIFY `vehicle_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `workspace`
--
ALTER TABLE `workspace`
  MODIFY `workspace_id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
