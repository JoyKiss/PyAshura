/*
Navicat MySQL Data Transfer

Source Server         : 凌志
Source Server Version : 50720
Source Host           : 192.168.10.170:3306
Source Database       : private_dmp

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2018-05-08 14:19:07
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for p_segmentex_model
-- ----------------------------
DROP TABLE IF EXISTS `p_segmentex_model`;
CREATE TABLE `p_segmentex_model` (
  `SEGMENTEX_MODEL_ID` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '人群拓展模型ID',
  `MODEL_TYPE` smallint(6) NOT NULL COMMENT '模型构建类型 1.标签 2.人群。现在只有标签类型',
  `TAG_ID` bigint(20) DEFAULT NULL COMMENT '种子人群ID',
  `TAG_EXPRESSION` varchar(255) DEFAULT NULL COMMENT '标签表达式',
  `INSTENSITY_BEGIN` float DEFAULT NULL COMMENT '热度范围开始',
  `INSTENSITY_END` float DEFAULT NULL COMMENT '热度范围截止',
  `RECENCY` bigint(20) NOT NULL COMMENT '种子人群标签特征新近时间范围 精确到小时',
  `STATUS` smallint(6) NOT NULL DEFAULT '0' COMMENT '状态  0未训练，1训练中,2训练完成3,就绪 -1,训练失败',
  `ALGORITHM_ID` int(20) NOT NULL COMMENT '算法模型ID',
  `EXCEPT_TAGS` varchar(255) DEFAULT NULL COMMENT '不参与计算标签ID 多个用英文逗号分隔',
  `MODEL_NAME` varchar(255) DEFAULT NULL COMMENT '模型名称',
  `FETCH_PERCENT` float(255,0) NOT NULL DEFAULT '0' COMMENT '算法测试人群抽取比例 种子人群* /总人数',
  `CREATE_TIME` timestamp NULL DEFAULT NULL COMMENT '模型创建时间',
  `LAST_UPDATE` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '模型更新时间',
  `EXCEPT_TAGS_NAME` varchar(1000) DEFAULT NULL COMMENT '不参与计算的标签名称，单个标签名用中括号[]括起来，标签之间以英文逗号分隔',
  `ALGORITHM_ARGS` varchar(255) DEFAULT NULL COMMENT '算法默认参数，模型创建时从algo_info读取，用户可修改，例如：''alpha=1,beta=2''',
  `TRAIN_TIME` datetime DEFAULT NULL COMMENT '模型训练的时间',
  `SNP` bigint(20) DEFAULT NULL COMMENT '种子人群数量，系统抽取完成后更新',
  `TNP` bigint(20) DEFAULT NULL COMMENT '训练人群数量，系统抽取完成后更新',
  `SIGMA` float DEFAULT NULL COMMENT '测试数据在TG_RESULT的占比，由系统统计',
  `TMP_PARAM` varchar(255) DEFAULT NULL COMMENT '模型中间参数，由算法生成',
  `MODEL_DIR` varchar(255) DEFAULT NULL COMMENT '模型持久化保存地址，由系统生成',
  `ARGS` varchar(255) DEFAULT NULL COMMENT '模型参数，由系统生成，逗号分隔，例如：''a=1,b=2''',
  `DATA_CLEAR_FLAG` int(11) DEFAULT '0' COMMENT '数据清理标志。种子人群、训练数据、测试数据，清理完一种数据加1，三种数据清理都完成时，值为3',
  PRIMARY KEY (`SEGMENTEX_MODEL_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
