/*
SQLyog  v12.2.6 (64 bit)
MySQL - 5.7.14 
*********************************************************************
*/
/*!40101 SET NAMES utf8 */;

create table `myshopping_goodstype` (
	`id` int (11),
	`name` varchar (150),
	`desc` text 
); 
insert into `myshopping_goodstype` (`id`, `name`, `desc`) values('1','键盘','神锋无敌，江湖谁的刀快谁有理');
insert into `myshopping_goodstype` (`id`, `name`, `desc`) values('2','鼠标','指尖的舞蹈..');
insert into `myshopping_goodstype` (`id`, `name`, `desc`) values('3','PC','从未如此的简单，一方世界尽在掌握..');
