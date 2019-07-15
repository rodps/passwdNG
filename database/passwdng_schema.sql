DROP TABLE passwords;
DROP TABLE conf;

CREATE TABLE IF NOT EXISTS passwords (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    username INTEGER NOT NULL,
    pass VARCHAR(90),
    pass_level VARCHAR(10),
    created_at DATE
);

CREATE TABLE IF NOT EXISTS conf (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    uppercase INTEGER,
    lowercase INTEGER,
    numbers INTEGER,
    special INTEGER,
    total INTEGER,
    period INTEGER,
    created_at DATE
);