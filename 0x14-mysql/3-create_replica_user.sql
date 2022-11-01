CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replica';
GRANT REPLICATION SLAVE on *.* TO 'replica_user'@'%';
GRANT SELECT on mysql.user TO 'holberton_user'@'localhost';
SELECT user, Repl_slave_priv FROM mysql.user;
