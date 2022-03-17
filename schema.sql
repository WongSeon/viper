drop table if exists message;


create table message (
    id integer primary key autoincrement,
    name text unique not null,
    body text not null,
    created timestamp not null default current_timestamp
);
