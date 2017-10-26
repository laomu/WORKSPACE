/*
SQLyog  v12.2.6 (64 bit)
MySQL - 5.7.14 
*********************************************************************
*/
/*!40101 SET NAMES utf8 */;

create table `myshopping_goods` (
	`id` int (11),
	`name` varchar (150),
	`price` double ,
	`stock` int (11),
	`desc` text ,
	`type_id` int (11)
); 
insert into `myshopping_goods` (`id`, `name`, `price`, `stock`, `desc`, `type_id`) values('1','alienware m14 r3','8999','100','14英寸外星人笔记本','5');
insert into `myshopping_goods` (`id`, `name`, `price`, `stock`, `desc`, `type_id`) values('2','alienware m17 r3','14999','120','17英寸外星人笔记本','5');
insert into `myshopping_goods` (`id`, `name`, `price`, `stock`, `desc`, `type_id`) values('3','alienware 2017','18999','10','18英寸外星人笔记本','5');
insert into `myshopping_goods` (`id`, `name`, `price`, `stock`, `desc`, `type_id`) values('4','macbook pro 2016','11000','20','13英寸MAC','6');
insert into `myshopping_goods` (`id`, `name`, `price`, `stock`, `desc`, `type_id`) values('5','macbook pro 2017','15000','18','新款13英寸MAC','6');
insert into `myshopping_goods` (`id`, `name`, `price`, `stock`, `desc`, `type_id`) values('6','华硕ASUS_飞行堡垒','12000','18','新款游戏本','7');
