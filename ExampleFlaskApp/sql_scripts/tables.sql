-- resources Table:
CREATE TABLE IF NOT EXISTS resources (
    id int NOT NULL AUTO_INCREMENT,
    item varchar(50) NOT NULL,
    amount int NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO resources (item, amount)
VALUES 
    ('ham', 14),
    ('bread', 18),
    ('cheese', 24);

-- sandwiches table:
CREATE TABLE IF NOT EXISTS sandwiches (
	id int NOT NULL AUTO_INCREMENT,
    sandwich_size varchar(50) NOT NULL,
    price decimal(5,2) NOT NULL,
    PRIMARY KEY (id)
);
