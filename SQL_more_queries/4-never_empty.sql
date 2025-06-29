-- creates the table id_not_null with default value on id column
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT '1',
    name VARCHAR(256)
);