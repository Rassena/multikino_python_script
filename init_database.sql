CREATE database multikino;
USE multikino;
CREATE USER 'root'@'%' IDENTIFIED BY 'pdb_2021';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';
FLUSH PRIVILEGES;