-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: dbofsaffron
-- ------------------------------------------------------
-- Server version	8.0.31-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `FormativeAssessment00100SPS`
--

DROP TABLE IF EXISTS `FormativeAssessment00100SPS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `FormativeAssessment00100SPS` (
  `StudentID010` varchar(250) NOT NULL,
  `English` varchar(250) NOT NULL,
  `Hindi` varchar(250) NOT NULL,
  `Sanskrit` varchar(250) NOT NULL,
  `Mathematics` varchar(250) NOT NULL,
  `Science` varchar(250) NOT NULL,
  `SocialScience` varchar(250) NOT NULL,
  `Computer` varchar(250) NOT NULL,
  `GeneralKnowledge` varchar(250) NOT NULL,
  PRIMARY KEY (`StudentID010`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FormativeAssessment00100SPS`
--

LOCK TABLES `FormativeAssessment00100SPS` WRITE;
/*!40000 ALTER TABLE `FormativeAssessment00100SPS` DISABLE KEYS */;
INSERT INTO `FormativeAssessment00100SPS` VALUES ('1','100','100','100','100','100','100','100','100'),('10','20','30','40','50','60','70','80','90'),('100','200','300','400','500','600','700','800','900'),('1000','2000','3000','4000','50000','6000','7000','8000','9000'),('11','220','330','440','550','660','770','880','990'),('50','100','100','100','100','100','100','100','100'),('88','88            88            88            88            88            88','','','','','','',''),('88               88               88               88               88','88               88               88               88               88','88               88               88               88               88','88               88               88               88               88','88               88               88               88               88','88               88               88               88               88','88               88               88               88               88','88               88               88               88               88','88               88               88               88               88'),('qwertyqwertyqwerty','0','0','0','0','0','0','0','0'),('sps05','888','888','888','888','888','888','888','888'),('sps10','88','88','88','88','88','88','88','88');
/*!40000 ALTER TABLE `FormativeAssessment00100SPS` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-07  1:13:27
