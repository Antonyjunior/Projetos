CREATE DATABASE tango;
show databases;
use tango;
show tables;
CREATE TABLE product (product_id int NOT NULL AUTO_INCREMENT Primary Key, product_name varchar(255) NOT NULL, product_description varchar(255));
select * from tango.product;
Insert into Product (product_name, product_description) Values ('Lapis', 'Grafite para escrever');
Insert into Product (product_name, product_description) Values ('Caneta', 'Esferografica para escrever');
