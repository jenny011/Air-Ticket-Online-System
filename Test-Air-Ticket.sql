-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Jun 30, 2019 at 10:13 AM
-- Server version: 5.7.25
-- PHP Version: 7.3.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Test-Air-Ticket`
--

-- --------------------------------------------------------

--
-- Table structure for table `airline`
--

CREATE TABLE `airline` (
  `airline_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `airline`
--

INSERT INTO `airline` (`airline_name`) VALUES
('Air China');

-- --------------------------------------------------------

--
-- Table structure for table `airline_staff`
--

CREATE TABLE `airline_staff` (
  `user_name` varchar(50) NOT NULL,
  `airline_name` varchar(50) DEFAULT NULL,
  `password` varchar(100) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `airline_staff`
--

INSERT INTO `airline_staff` (`user_name`, `airline_name`, `password`, `first_name`, `last_name`, `date_of_birth`) VALUES
('admin', 'Air China', 'e2fc714c4727ee9395f324cd2e7f331f', 'Roe', 'Zhang', '1978-05-25');

-- --------------------------------------------------------

--
-- Table structure for table `airplane`
--

CREATE TABLE `airplane` (
  `airline_name` varchar(50) NOT NULL,
  `id` varchar(50) NOT NULL,
  `amount_of_seats` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `airplane`
--

INSERT INTO `airplane` (`airline_name`, `id`, `amount_of_seats`) VALUES
('Air China', '1', 4),
('Air China', '2', 4),
('Air China', '3', 50);

-- --------------------------------------------------------

--
-- Table structure for table `airport`
--

CREATE TABLE `airport` (
  `airport_name` varchar(50) NOT NULL,
  `city` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `airport`
--

INSERT INTO `airport` (`airport_name`, `city`) VALUES
('BEI', 'Beijing'),
('BOS', 'Boston'),
('HKA', 'Hong Kong'),
('JFK', 'NYC'),
('LAX', 'Los Angles'),
('PVG', 'Shanghai'),
('SFO', 'San Francisco'),
('SHEN', 'Shenzhen');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `email` varchar(50) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `password` varchar(100) NOT NULL,
  `building_number` varchar(20) DEFAULT NULL,
  `street` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  `passport_number` varchar(50) DEFAULT NULL,
  `passport_expiration` date DEFAULT NULL,
  `passport_country` varchar(50) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`email`, `name`, `password`, `building_number`, `street`, `city`, `state`, `phone_number`, `passport_number`, `passport_expiration`, `passport_country`, `date_of_birth`) VALUES
('testcustomer@nyu.edu', 'Test Customer 1', '81dc9bdb52d04dc20036dbd8313ed055', '1555', 'Century Avenue', 'Pudong', 'Shanghai', '123-4321-4321', '54321', '2025-12-24', 'China', '1999-12-19'),
('user1@nyu.edu', 'User 1', '81dc9bdb52d04dc20036dbd8313ed055', '1555', 'Century Avenue', 'Pudong', 'Shanghai', '123-4322-4322', '54322', '2025-12-25', 'China', '1999-11-19'),
('user2@nyu.edu', 'User 2', '81dc9bdb52d04dc20036dbd8313ed055', '1702', 'Century Avenue', 'Pudong', 'Shanghai', '123-4323-4323', '54324', '2025-10-24', 'China', '1999-10-19'),
('user3@nyu.edu', 'User 3', '81dc9bdb52d04dc20036dbd8313ed055', '1890', 'Century Avenue', 'Pudong', 'Shanghai', '123-4324-4324', '54324', '2025-09-24', 'China', '1999-09-19');

-- --------------------------------------------------------

--
-- Table structure for table `flight`
--

CREATE TABLE `flight` (
  `airline_name` varchar(50) NOT NULL,
  `flight_number` varchar(20) NOT NULL,
  `departure_date` date NOT NULL,
  `departure_time` time NOT NULL,
  `arrival_date` date DEFAULT NULL,
  `arrival_time` time DEFAULT NULL,
  `departure_airport` varchar(50) DEFAULT NULL,
  `arrival_airport` varchar(50) DEFAULT NULL,
  `base_price` float DEFAULT NULL,
  `status` varchar(20) DEFAULT 'on-time',
  `id` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `flight`
--

INSERT INTO `flight` (`airline_name`, `flight_number`, `departure_date`, `departure_time`, `arrival_date`, `arrival_time`, `departure_airport`, `arrival_airport`, `base_price`, `status`, `id`) VALUES
('Air China', '102', '2019-04-12', '13:25:25', '2019-04-12', '16:50:25', 'SFO', 'LAX', 300, 'on-time', '3'),
('Air China', '104', '2019-05-12', '13:25:25', '2019-05-12', '16:50:25', 'PVG', 'BEI', 300, 'on-time', '3'),
('Air China', '106', '2019-03-12', '12:07:20', '2019-07-12', '16:50:25', 'SFO', 'LAX', 500, 'delayed', '2'),
('Air China', '134', '2019-01-12', '13:25:25', '2019-01-12', '16:50:25', 'JFK', 'BOS', 300, 'delayed', '3'),
('Air China', '206', '2019-07-12', '13:25:25', '2019-07-12', '16:50:25', 'SFO', 'LAX', 500, 'on-time', '2'),
('Air China', '207', '2019-08-12', '13:25:25', '2019-08-12', '16:50:25', 'LAX', 'SFO', 300, 'on-time', '2'),
('Air China', '296', '2019-07-01', '13:25:25', '2019-07-01', '16:50:25', 'PVG', 'SFO', 2000, 'on-time', '1'),
('Air China', '715', '2019-04-28', '10:25:25', '2019-04-28', '13:50:25', 'PVG', 'BEI', 500, 'delayed', '1'),
('Air China', '839', '2018-10-12', '13:25:25', '2018-10-12', '16:50:25', 'SHEN', 'BEI', 300, 'on-time', '3');

-- --------------------------------------------------------

--
-- Stand-in structure for view `flight_price`
-- (See below for the actual view)
--
CREATE TABLE `flight_price` (
`airline_name` varchar(50)
,`flight_number` varchar(20)
,`departure_date` date
,`departure_time` time
,`arrival_date` date
,`arrival_time` time
,`departure_airport` varchar(50)
,`arrival_airport` varchar(50)
,`price` double
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `flight_seats_sold`
-- (See below for the actual view)
--
CREATE TABLE `flight_seats_sold` (
`airline_name` varchar(50)
,`flight_number` varchar(20)
,`departure_date` date
,`departure_time` time
,`amount_of_seats` int(11)
,`tickets_sold` bigint(21)
);

-- --------------------------------------------------------

--
-- Table structure for table `purchase`
--

CREATE TABLE `purchase` (
  `ticket_id` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `purchase_date` date DEFAULT NULL,
  `purchase_time` time DEFAULT NULL,
  `sold_price` float NOT NULL,
  `card_type` varchar(50) DEFAULT NULL,
  `card_number` varchar(50) DEFAULT NULL,
  `name_on_card` varchar(50) DEFAULT NULL,
  `expiraton_date` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `purchase`
--

INSERT INTO `purchase` (`ticket_id`, `email`, `purchase_date`, `purchase_time`, `sold_price`, `card_type`, `card_number`, `name_on_card`, `expiraton_date`) VALUES
('1', 'testcustomer@nyu.edu', '2019-03-12', '11:55:55', 300, 'credit card', '111-222-333-444', 'Test Customer 1', '2023-03'),
('11', 'user3@nyu.edu', '2018-10-23', '11:55:55', 300, 'credit card', '1111-2222-3333-5555', 'User 3', '2023-03'),
('12', 'testcustomer@nyu.edu', '2019-04-05', '11:55:55', 500, 'credit card', '1111-2222-3333-4444', 'Test Customer 1', '2023-03'),
('14', 'user3@nyu.edu', '2019-05-12', '11:55:55', 400, 'credit card', '1111-2222-3333-5555', 'User 3', '2023-03'),
('15', 'user1@nyu.edu', '2019-05-13', '11:55:55', 400, 'credit card', '1111-2222-3333-5555', 'User 1', '2023-03'),
('16', 'user2@nyu.edu', '2019-04-19', '11:55:55', 400, 'credit card', '1111-2222-3333-5555', 'User 2', '2023-03'),
('17', 'user1@nyu.edu', '2019-03-11', '11:55:55', 300, 'credit card', '1111-2222-3333-5555', 'User 1', '2023-03'),
('18', 'testcustomer@nyu.edu', '2019-04-25', '11:55:55', 300, 'credit card', '1111-2222-3333-4444', 'Test Customer 1', '2023-03'),
('19', 'user1@nyu.edu', '2019-05-04', '11:55:55', 3000, 'credit card', '1111-2222-3333-5555', 'User 1', '2023-03'),
('2', 'user1@nyu.edu', '2019-03-11', '11:55:55', 300, 'credit card', '1111-2222-3333-5555', 'User 1', '2023-03'),
('20', 'testcustomer@nyu.edu', '2019-02-12', '11:55:55', 3000, 'credit card', '1111-2222-3333-4444', 'Test Customer 1', '2023-03'),
('3', 'user2@nyu.edu', '2019-04-11', '11:55:55', 300, 'credit card', '1111-2222-3333-5555', 'User 2', '2023-03'),
('4', 'user1@nyu.edu', '2019-03-21', '11:55:55', 300, 'credit card', '1111-2222-3333-5555', 'User 1', '2023-03'),
('5', 'testcustomer@nyu.edu', '2019-04-28', '11:55:55', 300, 'credit card', '1111-2222-3333-4444', 'Test Customer 1', '2023-03'),
('6', 'user1@nyu.edu', '2019-03-05', '11:55:55', 350, 'credit card', '1111-2222-3333-4444', 'Test Customer 1', '2023-03'),
('7', 'user3@nyu.edu', '2019-02-03', '11:55:55', 350, 'credit card', '1111-2222-3333-5555', 'User 3', '2023-03'),
('8', 'user3@nyu.edu', '2018-10-03', '11:55:55', 300, 'credit card', '1111-2222-3333-5555', 'User 3', '2023-03'),
('9', 'user3@nyu.edu', '2019-02-03', '11:55:55', 360, 'credit card', '1111-2222-3333-5555', 'User 3', '2023-03');

-- --------------------------------------------------------

--
-- Table structure for table `rates`
--

CREATE TABLE `rates` (
  `email` varchar(50) NOT NULL,
  `airline_name` varchar(50) NOT NULL,
  `flight_number` varchar(20) NOT NULL,
  `departure_date` date NOT NULL,
  `departure_time` time NOT NULL,
  `rating` int(11) DEFAULT NULL,
  `comments` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `rates`
--

INSERT INTO `rates` (`email`, `airline_name`, `flight_number`, `departure_date`, `departure_time`, `rating`, `comments`) VALUES
('testcustomer@nyu.edu', 'Air China', '102', '2019-04-12', '13:25:25', 4, 'Very Comfortable'),
('testcustomer@nyu.edu', 'Air China', '104', '2019-05-12', '13:25:25', 1, 'Customer Care services are not good'),
('user1@nyu.edu', 'Air China', '102', '2019-04-12', '13:25:25', 5, 'Relaxing, check-in and onboarding very professional'),
('user1@nyu.edu', 'Air China', '104', '2019-05-12', '13:25:25', 5, 'Comfortable journey and Professional'),
('user2@nyu.edu', 'Air China', '102', '2019-04-12', '13:25:25', 3, 'Satisfies and will use the same flight again');

-- --------------------------------------------------------

--
-- Table structure for table `staff_phone`
--

CREATE TABLE `staff_phone` (
  `user_name` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `staff_phone`
--

INSERT INTO `staff_phone` (`user_name`, `phone`) VALUES
('admin', '111-2222-3333'),
('admin', '444-5555-6666');

-- --------------------------------------------------------

--
-- Table structure for table `ticket`
--

CREATE TABLE `ticket` (
  `ticket_id` varchar(50) NOT NULL,
  `airline_name` varchar(50) DEFAULT NULL,
  `flight_number` varchar(20) DEFAULT NULL,
  `departure_date` date DEFAULT NULL,
  `departure_time` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `ticket`
--

INSERT INTO `ticket` (`ticket_id`, `airline_name`, `flight_number`, `departure_date`, `departure_time`) VALUES
('1', 'Air China', '102', '2019-04-12', '13:25:25'),
('2', 'Air China', '102', '2019-04-12', '13:25:25'),
('3', 'Air China', '102', '2019-04-12', '13:25:25'),
('9', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340004', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340005', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340006', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340007', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340008', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340009', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340010', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340011', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340012', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340013', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340014', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340015', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340016', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340017', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340018', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340019', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340020', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340021', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340022', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340023', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340024', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340025', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340026', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340027', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340028', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340029', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340030', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340031', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340032', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340033', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340034', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340035', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340036', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340037', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340038', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340039', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340040', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340041', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340042', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340043', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340044', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340045', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340046', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340047', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340048', 'Air China', '102', '2019-04-12', '13:25:25'),
('AC10230389340049', 'Air China', '102', '2019-04-12', '13:25:25'),
('4', 'Air China', '104', '2019-05-12', '13:25:25'),
('5', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100002', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100003', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100004', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100005', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100006', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100007', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100008', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100009', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100010', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100011', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100012', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100013', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100014', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100015', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100016', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100017', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100018', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100019', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100020', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100021', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100022', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100023', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100024', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100025', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100026', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100027', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100028', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100029', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100030', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100031', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100032', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100033', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100034', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100035', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100036', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100037', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100038', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100039', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100040', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100041', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100042', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100043', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100044', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100045', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100046', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100047', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100048', 'Air China', '104', '2019-05-12', '13:25:25'),
('AC10436254100049', 'Air China', '104', '2019-05-12', '13:25:25'),
('6', 'Air China', '106', '2019-03-12', '12:07:20'),
('7', 'Air China', '106', '2019-03-12', '12:07:20'),
('AC10640946930002', 'Air China', '106', '2019-03-12', '12:07:20'),
('AC10640946930003', 'Air China', '106', '2019-03-12', '12:07:20'),
('11', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280001', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280002', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280003', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280004', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280005', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280006', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280007', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280008', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280009', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280010', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280011', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280012', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280013', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280014', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280015', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280016', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280017', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280018', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280019', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280020', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280021', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280022', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280023', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280024', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280025', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280026', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280027', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280028', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280029', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280030', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280031', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280032', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280033', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280034', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280035', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280036', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280037', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280038', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280039', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280040', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280041', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280042', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280043', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280044', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280045', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280046', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280047', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280048', 'Air China', '134', '2019-01-12', '13:25:25'),
('AC13414794280049', 'Air China', '134', '2019-01-12', '13:25:25'),
('14', 'Air China', '206', '2019-07-12', '13:25:25'),
('15', 'Air China', '206', '2019-07-12', '13:25:25'),
('16', 'Air China', '206', '2019-07-12', '13:25:25'),
('AC20686270030003', 'Air China', '206', '2019-07-12', '13:25:25'),
('17', 'Air China', '207', '2019-08-12', '13:25:25'),
('18', 'Air China', '207', '2019-08-12', '13:25:25'),
('AC20776454470002', 'Air China', '207', '2019-08-12', '13:25:25'),
('AC20776454470003', 'Air China', '207', '2019-08-12', '13:25:25'),
('19', 'Air China', '296', '2019-07-01', '13:25:25'),
('20', 'Air China', '296', '2019-07-01', '13:25:25'),
('AC29631585370002', 'Air China', '296', '2019-07-01', '13:25:25'),
('AC29631585370003', 'Air China', '296', '2019-07-01', '13:25:25'),
('12', 'Air China', '715', '2019-04-28', '10:25:25'),
('AC71570024330001', 'Air China', '715', '2019-04-28', '10:25:25'),
('AC71570024330002', 'Air China', '715', '2019-04-28', '10:25:25'),
('AC71570024330003', 'Air China', '715', '2019-04-28', '10:25:25'),
('8', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850001', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850002', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850003', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850004', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850005', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850006', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850007', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850008', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850009', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850010', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850011', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850012', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850013', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850014', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850015', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850016', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850017', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850018', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850019', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850020', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850021', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850022', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850023', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850024', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850025', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850026', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850027', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850028', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850029', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850030', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850031', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850032', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850033', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850034', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850035', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850036', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850037', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850038', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850039', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850040', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850041', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850042', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850043', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850044', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850045', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850046', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850047', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850048', 'Air China', '839', '2018-10-12', '13:25:25'),
('AC83921280850049', 'Air China', '839', '2018-10-12', '13:25:25');

-- --------------------------------------------------------

--
-- Structure for view `flight_price`
--
DROP TABLE IF EXISTS `flight_price`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `flight_price`  AS  select `flight`.`airline_name` AS `airline_name`,`flight`.`flight_number` AS `flight_number`,`flight`.`departure_date` AS `departure_date`,`flight`.`departure_time` AS `departure_time`,`flight`.`arrival_date` AS `arrival_date`,`flight`.`arrival_time` AS `arrival_time`,`flight`.`departure_airport` AS `departure_airport`,`flight`.`arrival_airport` AS `arrival_airport`,(case when (`flight_seats_sold`.`tickets_sold` >= (0.7 * `flight_seats_sold`.`amount_of_seats`)) then (`flight`.`base_price` * 1.2) else `flight`.`base_price` end) AS `price` from (`flight` left join `flight_seats_sold` on(((`flight`.`airline_name` = `flight_seats_sold`.`airline_name`) and (`flight`.`flight_number` = `flight_seats_sold`.`flight_number`) and (`flight`.`departure_date` = `flight_seats_sold`.`departure_date`) and (`flight`.`departure_time` = `flight_seats_sold`.`departure_time`)))) ;

-- --------------------------------------------------------

--
-- Structure for view `flight_seats_sold`
--
DROP TABLE IF EXISTS `flight_seats_sold`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `flight_seats_sold`  AS  select `flight`.`airline_name` AS `airline_name`,`flight`.`flight_number` AS `flight_number`,`flight`.`departure_date` AS `departure_date`,`flight`.`departure_time` AS `departure_time`,`airplane`.`amount_of_seats` AS `amount_of_seats`,count(`purchase`.`ticket_id`) AS `tickets_sold` from (((`flight` join `airplane` on(((`flight`.`airline_name` = `airplane`.`airline_name`) and (`flight`.`id` = `airplane`.`id`)))) join `ticket` on(((`flight`.`airline_name` = `ticket`.`airline_name`) and (`flight`.`flight_number` = `ticket`.`flight_number`) and (`flight`.`departure_date` = `ticket`.`departure_date`) and (`flight`.`departure_time` = `ticket`.`departure_time`)))) left join `purchase` on((`ticket`.`ticket_id` = `purchase`.`ticket_id`))) group by `flight`.`airline_name`,`flight`.`flight_number`,`flight`.`departure_date`,`flight`.`departure_time` ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `airline`
--
ALTER TABLE `airline`
  ADD PRIMARY KEY (`airline_name`);

--
-- Indexes for table `airline_staff`
--
ALTER TABLE `airline_staff`
  ADD PRIMARY KEY (`user_name`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Indexes for table `airplane`
--
ALTER TABLE `airplane`
  ADD PRIMARY KEY (`airline_name`,`id`);

--
-- Indexes for table `airport`
--
ALTER TABLE `airport`
  ADD PRIMARY KEY (`airport_name`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `flight`
--
ALTER TABLE `flight`
  ADD PRIMARY KEY (`airline_name`,`flight_number`,`departure_date`,`departure_time`),
  ADD KEY `airline_name` (`airline_name`,`id`),
  ADD KEY `departure_airport` (`departure_airport`),
  ADD KEY `arrival_airport` (`arrival_airport`);

--
-- Indexes for table `purchase`
--
ALTER TABLE `purchase`
  ADD PRIMARY KEY (`ticket_id`,`email`),
  ADD KEY `email` (`email`);

--
-- Indexes for table `rates`
--
ALTER TABLE `rates`
  ADD PRIMARY KEY (`email`,`airline_name`,`flight_number`,`departure_date`,`departure_time`),
  ADD KEY `airline_name` (`airline_name`,`flight_number`,`departure_date`,`departure_time`);

--
-- Indexes for table `staff_phone`
--
ALTER TABLE `staff_phone`
  ADD PRIMARY KEY (`user_name`,`phone`);

--
-- Indexes for table `ticket`
--
ALTER TABLE `ticket`
  ADD PRIMARY KEY (`ticket_id`),
  ADD KEY `airline_name` (`airline_name`,`flight_number`,`departure_date`,`departure_time`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `airline_staff`
--
ALTER TABLE `airline_staff`
  ADD CONSTRAINT `airline_staff_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`airline_name`) ON UPDATE CASCADE;

--
-- Constraints for table `airplane`
--
ALTER TABLE `airplane`
  ADD CONSTRAINT `airplane_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`airline_name`) ON UPDATE CASCADE;

--
-- Constraints for table `flight`
--
ALTER TABLE `flight`
  ADD CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`airline_name`) ON UPDATE CASCADE,
  ADD CONSTRAINT `flight_ibfk_2` FOREIGN KEY (`airline_name`,`id`) REFERENCES `airplane` (`airline_name`, `id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `flight_ibfk_3` FOREIGN KEY (`departure_airport`) REFERENCES `airport` (`airport_name`) ON UPDATE CASCADE,
  ADD CONSTRAINT `flight_ibfk_4` FOREIGN KEY (`arrival_airport`) REFERENCES `airport` (`airport_name`) ON UPDATE CASCADE;

--
-- Constraints for table `purchase`
--
ALTER TABLE `purchase`
  ADD CONSTRAINT `purchase_ibfk_1` FOREIGN KEY (`ticket_id`) REFERENCES `ticket` (`ticket_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `purchase_ibfk_2` FOREIGN KEY (`email`) REFERENCES `customer` (`email`) ON UPDATE CASCADE;

--
-- Constraints for table `rates`
--
ALTER TABLE `rates`
  ADD CONSTRAINT `rates_ibfk_1` FOREIGN KEY (`email`) REFERENCES `customer` (`email`) ON UPDATE CASCADE,
  ADD CONSTRAINT `rates_ibfk_2` FOREIGN KEY (`airline_name`,`flight_number`,`departure_date`,`departure_time`) REFERENCES `flight` (`airline_name`, `flight_number`, `departure_date`, `departure_time`) ON UPDATE CASCADE;

--
-- Constraints for table `staff_phone`
--
ALTER TABLE `staff_phone`
  ADD CONSTRAINT `staff_phone_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `airline_staff` (`user_name`) ON UPDATE CASCADE;

--
-- Constraints for table `ticket`
--
ALTER TABLE `ticket`
  ADD CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`airline_name`,`flight_number`,`departure_date`,`departure_time`) REFERENCES `flight` (`airline_name`, `flight_number`, `departure_date`, `departure_time`) ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
