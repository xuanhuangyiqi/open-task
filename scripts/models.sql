create table if not exists `task`(
    `id` int(11) AUTO_INCREMENT, 
    `create_time` int(11),
    `ord` int(11),
    `title` varchar(20),
    `content` text,
    `done` int(1),
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET=utf8;
