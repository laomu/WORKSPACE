use mysite;

select * from commons_users;

select * from myshopping_goodstype;

insert into myshopping_goodstype
    values(null, '键盘', '神锋无敌，江湖谁的刀快谁有理');
insert into myshopping_goodstype
    values(null, '鼠标', '指尖的舞蹈..');
insert into myshopping_goodstype
    values(null, 'PC', '从未如此的简单，一方世界尽在掌握..')

select * from myshopping_goodsdetailtype;

insert into myshopping_goodsdetailtype
    values(null, '罗技', '罗技无敌', 1);
insert into myshopping_goodsdetailtype
    values(null, '双飞燕', '天下武功唯快不破', 1);
insert into myshopping_goodsdetailtype
    values(null, '赛钛客', '述说鼠标那场机械革命', 2);
insert into myshopping_goodsdetailtype
    values(null, '罗技', '鼠标之王者归来', 2);
insert into myshopping_goodsdetailtype
    values(null, '外星人', '最强游戏本', 3);
insert into myshopping_goodsdetailtype
    values(null, 'mac pro', '商务本首选', 3);
insert into myshopping_goodsdetailtype
    values(null, '华硕', '华硕品质，坚若磐石', 3);

