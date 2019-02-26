/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50544
Source Host           : localhost:3306
Source Database       : dmzj

Target Server Type    : MYSQL
Target Server Version : 50544
File Encoding         : 65001

Date: 2018-05-08 01:05:15
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for YeInfo
-- ----------------------------
DROP TABLE IF EXISTS `YeInfo`;
CREATE TABLE `YeInfoTmp` (
  `yid` int(20) NOT NULL AUTO_INCREMENT,
  `jid` int(20) DEFAULT NULL,
  `index` varchar(255) DEFAULT NULL,
  `url` varchar(21111) DEFAULT NULL,
  `downFlag` varchar(255) DEFAULT '0',
  PRIMARY KEY (`yid`),
  KEY `index` (`yid`,`jid`),
  KEY `index2` (`yid`,`jid`,`index`,`url`(255))
) ENGINE=InnoDB AUTO_INCREMENT=395544 DEFAULT CHARSET=utf8;
