-- creates the table unique_id with unique value in id column
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT '1' UNIQUE,
    name VARCHAR(256)
);