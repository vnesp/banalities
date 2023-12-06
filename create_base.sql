CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    nick_name TEXT
);


CREATE TABLE IF NOT EXISTS state (
    id INTEGER PRIMARY KEY AUTO AUTOINCREMENT,
    descr VARCHAR(20) NOT NULL
);


INSERT INTO state (descr)
VALUES
    ('created'),
    ('in progress'),
    ('finished');


CREATE TABLE IF NOT EXISTS game (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gm_id INTEGER NOT NULL,
    round_count INTEGER DEFAULT 5,
    state_id INTEGER NOT NULL,
        FOREIGN KEY (gm_id) REFERENCES user(id),
        FOREIGN KEY (state_id) REFERENCES state(id)
);


CREATE TABLE IF NOT EXISTS participation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    score INTEGER DEFAULT 0,
    user_id INTEGER NOT NULL,
    game_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user(id),
        FOREIGN KEY (game_id) REFERENCES game(id)
);


CREATE TABLE IF NOT EXISTS task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descr VARCHAR(50) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS turn (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    num INTEGER NOT NULL,
    words_count INTEGER DEFAULT 10,
    game_id INTEGER NOT NULL,
    task_id INTEGER,
    state_id INTEGER NOT NULL,
        FOREIGN KEY (game_id) REFERENCES game(id),
        FOREIGN KEY (task_id) REFERENCES task(id),
        FOREIGN KEY (state_id) REFERENCES state(id)
);


CREATE TABLE IF NOT EXISTS word (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word VARCHAR(30) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS word_list (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    score INTEGER DEFAULT 0,
    participation_id INTEGER NOT NULL,
    turn_id INTEGER NOT NULL,
    state_id INTEGER NOT NULL,
        FOREIGN KEY (participation_id) REFERENCES participation(id),
        FOREIGN KEY (turn_id) REFERENCES turn(id),
        FOREIGN KEY (state_id) REFERENCES state(id)
);


CREATE TABLE IF NOT EXISTS list_position (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word_list_id INTEGER NOT NULL,
    word_id INTEGER NOT NULL,
        FOREIGN KEY (word_list_id) REFERENCES word_list(id),
        FOREIGN KEY (word_id) REFERENCES word(id)
);


CREATE TABLE IF NOT EXISTS ban_list_position (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER,
    word_id INTEGER,
        FOREIGN KEY (task_id) REFERENCES task(id),
        FOREIGN KEY (word_id) REFERENCES word(id)
);
