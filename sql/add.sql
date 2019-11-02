-- name: add_feed
insert or replace into entries
    select json_extract(value, "$.id"),
           json_extract(value, "$.title"),
           json_extract(value, "$.link"),
           json_extract(value, "$.summary"),
           parsed2date(coalesce(
             json_extract(value, "$.published_parsed"),
             json_extract(value, "$.created_parsed"),
             json_extract(value, "$.updated_parsed")
           ))
      from json_each(json_extract(json(feed(:url)), "$.entries"))
