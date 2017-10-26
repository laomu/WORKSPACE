/*
SQLyog  v12.2.6 (64 bit)
MySQL - 5.7.14 
*********************************************************************
*/
/*!40101 SET NAMES utf8 */;

create table `myshopping_goodsdetailtype` (
	`id` int (11),
	`name` varchar (150),
	`desc` text ,
	`type_id` int (11)
); 
insert into `myshopping_goodsdetailtype` (`id`, `name`, `desc`, `type_id`) values('1','罗技','罗技无敌','1');
insert into `myshopping_goodsdetailtype` (`id`, `name`, `desc`, `type_id`) values('2','双飞燕','天下武功唯快不破','1');
insert into `myshopping_goodsdetailtype` (`id`, `name`, `desc`, `type_id`) values('3','赛钛客','述说鼠标那场机械革命','2');
insert into `myshopping_goodsdetailtype` (`id`, `name`, `desc`, `type_id`) values('4','罗技','鼠标之王者归来','2');
insert into `myshopping_goodsdetailtype` (`id`, `name`, `desc`, `type_id`) values('5','外星人','最强游戏本','3');
insert into `myshopping_goodsdetailtype` (`id`, `name`, `desc`, `type_id`) values('6','mac pro','商务本首选','3');
insert into `myshopping_goodsdetailtype` (`id`, `name`, `desc`, `type_id`) values('7','华硕','华硕品质，坚若磐石','3');
