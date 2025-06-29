-- creates the database hbtn_0d_usa and the table cities, with column state_id, foreign key, ref id in table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
    USE hbtn_0d_usa;
    CREATE TABLE IF NOT EXISTS cities (
        id int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
        state_id int NOT NULL FOREIGN KEY REFERENCES states (id),
        name varchar(256) NOT NULL
    );