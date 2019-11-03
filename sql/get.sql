-- name: get_entries
select *
  from entries
 order by published desc

-- name: get_entries_unread
select *
  from entries
 where read = 0
 order by published desc
