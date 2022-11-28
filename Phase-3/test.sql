select p_pictureid, p_name, p_agerating, p_genre, p_type, p_releasedate
from Picture, Media_Cast_Member, Cast_Member
where p_pictureid = mcm_pictureid
    and mcm_personid = cm_personid
    and cm_name like '%Seth%'
group by p_pictureid