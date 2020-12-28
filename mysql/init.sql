DROP DATABASE IF EXISTS `sys`;

CREATE DATABASE IF NOT EXISTS `stock_news`;

CREATE TABLE `stock_news`.`title_rating_results` (
    `title_rating_results_pk` int(11) unsigned NOT NULL AUTO_INCREMENT,
    `title` TEXT,
    `rating` int(11) unsigned NOT NULL,
    `record_date_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `record_date_last_modified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`title_rating_results_pk`),
    INDEX `record_date_created` (`record_date_created`),
    INDEX `record_date_last_modified` (`record_date_last_modified`)
    ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4;
