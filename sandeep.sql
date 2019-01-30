-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 30, 2019 at 11:24 PM
-- Server version: 5.7.24-0ubuntu0.18.04.1
-- PHP Version: 7.0.30-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sandeep`
--

-- --------------------------------------------------------

--
-- Table structure for table `portfolios`
--

CREATE TABLE `portfolios` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `project_id` int(11) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `about` text,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--

CREATE TABLE `projects` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `about` text,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `projects`
--

INSERT INTO `projects` (`id`, `name`, `user_id`, `image`, `about`, `start_date`, `end_date`, `created_at`) VALUES
(2, 'Arya Natural Farming', 1, '/projects/Firefox_Screenshot_2018-05-15T17-44-26.974Z.png', 'Its my own website to sell organic products. includes all process of selling and booking.', '2017-07-12', '2017-08-24', '2019-01-29 16:52:27'),
(3, 'Exploring Himachal', 1, '/projects/Firefox_Screenshot_2019-01-07T17-25-07.291Z.png', 'Its is a travel agency, catering to everyone from backpackers to luxury travelers and love to share the beauty and culture of Himalaya with the world.', '2018-02-01', '2018-03-07', '2019-01-29 18:23:00'),
(4, 'Civil Academy', 1, '/projects/civil.png', 'One stop solution of Affordable courses for Learner’s Driving, Defensive Driving , Fire Fighting\r\nTraining, First Aid, Occupational Health & Safety and Vocational Training programs.', '2018-07-04', '2018-08-15', '2019-01-30 17:24:53'),
(5, 'Findurguru', 1, '/projects/Firefox_Screenshot_2018-10-17T16-23-30.462Z.png', 'Its a market place to allow customers at a click of a button to source out the best and most cost effective service provider fit for their specific needs seamlessly exceeding their expectations.', '2018-08-23', '2018-10-26', '2019-01-30 17:26:23');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `about` text,
  `password` varchar(200) NOT NULL,
  `address` text,
  `phone` varchar(100) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `image`, `about`, `password`, `address`, `phone`, `created_at`) VALUES
(1, 'Sandeep Bangarh', 'sanbangarh309@gmail.com', '/profile/11025231_861471627243487_7326334804074004060_n.jpg', 'I am a full stack developer. I have an experience of web application development with LAMP stack(Linux, Apache, MySQL and PHP) using laravel-framework,slim framework,Django framework,Code-igniter and MERN stack(MongoDB, Express Js, React and Node Js). I also have an experience with other web technologies like AJAX, HTML, CSS, XML, WordPress Plugin Development, Bootstrap, Materialize.', 'pbkdf2:sha256:50000$qRSjB5bQ$45e0865655d84e932702151bf5c31b9d0a66ef74c21f34e4cf224b87fb2d5943', 'village mehra , block ladwa , dist kurukshetra', '+919896747812', '2019-01-13 08:08:47');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `portfolios`
--
ALTER TABLE `portfolios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `project_id` (`project_id`);

--
-- Indexes for table `projects`
--
ALTER TABLE `projects`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `portfolios`
--
ALTER TABLE `portfolios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `portfolios`
--
ALTER TABLE `portfolios`
  ADD CONSTRAINT `portfolios_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `portfolios_ibfk_2` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`);

--
-- Constraints for table `projects`
--
ALTER TABLE `projects`
  ADD CONSTRAINT `projects_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
