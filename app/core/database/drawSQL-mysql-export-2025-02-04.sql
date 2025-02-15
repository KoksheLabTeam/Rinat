CREATE TABLE `users`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(255) NOT NULL,
    `first_name` VARCHAR(255) NOT NULL,
    `last_name` VARCHAR(255) NOT NULL
);
CREATE TABLE `foods`(
    `id` BIGINT NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `price` INT NOT NULL,
    `description` VARCHAR(255) NOT NULL,
    `photo` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`id`)
);
CREATE TABLE `orders`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `user_id` BIGINT NOT NULL,
    `datetime` TIMESTAMP NOT NULL,
    `address` VARCHAR(255) NOT NULL,
    `full_name` VARCHAR(255) NOT NULL,
    `status` VARCHAR(255) NOT NULL,
    `phone_number` LINESTRING NOT NULL,
    `total_price` BIGINT NOT NULL
);
ALTER TABLE
    `orders` ADD CONSTRAINT `orders_user_id_foreign` FOREIGN KEY(`user_id`) REFERENCES `users`(`id`);