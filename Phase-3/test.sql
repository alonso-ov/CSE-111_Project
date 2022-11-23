select mcm_role, cm_name
from Media_Cast_Member, Cast_Member
where mcm_personid = cm_personid
    and mcm_pictureid = 'tm154986'
group by mcm_role, cm_name