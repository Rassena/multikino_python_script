/* this script is run only once to initialize database */
/* it creates database with user root and user's password pdb_2021 */

CREATE database multikino;
USE multikino;
CREATE USER 'root'@'%' IDENTIFIED BY 'pdb_2021';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';
FLUSH PRIVILEGES;