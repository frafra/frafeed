-- name: get_entries_all
select title, link, summary, published
  from entries
 order by published desc

-- name: get_entries_unread
select title, link, summary, published
  from entries
 where status = 'new'
 order by published desc

-- name: get_entries_all_short
select title, link, published
  from entries
 order by published desc

-- name: get_entries_unread_short
select title, link, published
  from entries
 where status = 'new'
 order by published desc
