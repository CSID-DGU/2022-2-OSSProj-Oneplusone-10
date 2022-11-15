create table if not exists easy_mode (
    user_id integer primary key autoincrement,
    username string not null,
    score string not null
);

create table if not exists hard_mode (
    user_id integer primary key autoincrement,
    username string not null,
    score string not null
);

create table if not exists character (
    id integer primary key autoincrement,
    name string not null,
    is_paid integer default 0,
    is_apply integer default 0,
    price integer default 0
);

insert or ignore into character (id, name, is_paid, is_apply, price)
                            values(1, "Purple", 0,  0,  500);
insert or ignore into character (id, name, is_paid, is_apply, price)
                            values(2, "Red", 0, 0, 500);
insert or ignore into character (id, name, is_paid, is_apply, price)
                            values(3, "Yellow", 0, 0, 500);
insert or ignore into character (id, name, is_paid, is_apply, price)
                            values(4, "Tux", 0, 0, 3000);