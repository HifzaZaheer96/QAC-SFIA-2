BEGIN;

-- Database: `partythemegenerator_db`
--
-- --------------------------------------------------------
--
-- Table structure for table `USER`
--
DROP DATABASE IF EXISTS partythemegenerator;
CREATE DATABASE partythemegenerator;
use partythemegenerator;


CREATE TABLE `USER` (
  `user_id` int(6) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(30) NOT NULL,
  `second_name` varchar(30) NOT NULL,
  `username` varchar(30) NOT NULL,
  `email` varchar(100) NOT NULL,
  `message` varchar(100) NOT NULL,
  PRIMARY KEY(user_id)
);


-- Table structure for table `themesentence`
--
CREATE TABLE `themesentence` (
  `theme_id` int(6) NOT NULL AUTO_INCREMENT,
  `theme_sentence` varchar(500) NOT NULL,
  PRIMARY KEY(theme_id)
);





-- --------------------------------------------------------

-- ----------

COMMIT;
