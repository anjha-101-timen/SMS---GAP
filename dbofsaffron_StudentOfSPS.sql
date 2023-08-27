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
-- Table structure for table `StudentOfSPS`
--

DROP TABLE IF EXISTS `StudentOfSPS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `StudentOfSPS` (
  `StudentID` varchar(250) NOT NULL,
  `StudentName` varchar(250) NOT NULL,
  `DateOfBirth` varchar(250) NOT NULL,
  `Class` varchar(250) NOT NULL,
  `Section` varchar(250) NOT NULL,
  `RollNo` varchar(250) NOT NULL,
  `FatherName` varchar(250) NOT NULL,
  `MotherName` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `Telephone` varchar(250) NOT NULL,
  PRIMARY KEY (`StudentID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `StudentOfSPS`
--

LOCK TABLES `StudentOfSPS` WRITE;
/*!40000 ALTER TABLE `StudentOfSPS` DISABLE KEYS */;
INSERT INTO `StudentOfSPS` VALUES ('123','234','345','456','567','678','789','901','012','123'),('41','42','43','44','45','46','47','48','49','50'),('51','52','53','54','55','56','57','58','59','60'),('sps555','Harry','01-01-2005','12','B0','20','Mr.Robert Paper','Mrs.Stephen Wood','Apple,New-York,America','9995423178');
/*!40000 ALTER TABLE `StudentOfSPS` ENABLE KEYS */;
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
