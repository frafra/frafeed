-- name: mark_all_as_read
update entries
   set status != 'new'
