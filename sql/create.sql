-- name: create_tables#
create table if not exists sources (
    url         text primary key
);
create table if not exists entries (
    id          text primary key,
    title       text,
    link        text,
    summary     text,
    published   text,
    status      text,
    source      url references sources
);
