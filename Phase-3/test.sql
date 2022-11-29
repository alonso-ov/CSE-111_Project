--select p_name, mwl_watchstatus, mwl_completitiondate
select p_pictureid, p_name, mwl_watchstatus, mwl_completitiondate
from picture, media_watchlist
where p_pictureid = mwl_pictureid
    and mwl_userid = 2

select *
from picture
where p_pictureid = 'ts9'


select *, rowid
from picture
where p_pictureid = 'ts9'


--delete duplicates
delete from Picture
where rowid not in (
    select min(rowid)
    from Picture
    group by p_pictureid
)