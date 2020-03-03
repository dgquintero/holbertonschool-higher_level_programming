--  script that creates the database hbtn_0d_usa and the table states
-- states description: id INT unique, auto generated,
-- can’t be null and is a primary key name VARCHAR(256) can’t be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_GENERATED UNIQUE PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
