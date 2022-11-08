--1 --> create new user in table 'User'
INSERT INTO User (u_id, u_username, u_passcode, u_email, u_firstname, u_lastname, u_preferredstreamsite) 
VALUES (5, 'Tom2345', 'gjdhdhdsds', 'tom2345@gmail.com', 'Tom', 'Bob', 'Netflix' );

--2 --> select passcode for user "Tom2345" (will be used for authentication)
SELECT u_passcode as Passcode
FROM User
WHERE
    u_username = 'Tom2345';

--3 --> change the passcode for user "Tom2345" (will be used for part of process in which user wants to change passcode)
UPDATE User
SET u_passcode = 'hfegegWwr@33'
WHERE 
    u_username = 'Tom2345';

--4 --> display specific user's watchlist (ex. user: jellybean)
SELECT p_name as PictureName, w_watchstatus as WatchStatus, w_completiondate as CompletionDate
FROM Media_Watch_List, User, Picture
WHERE 
    User.u_id = Media_Watch_List.u_id AND Media_Watch_List.p_id = Picture.p_id AND
    u_username = 'jellybean';

--5 --> display all picture entries in database with the two types of public ratings 
SELECT p_name as PictureName, pr_imdb as IMDbRating, pr_tmdb as TMDbRating
FROM Picture, Public_Ratings
WHERE 
    Picture.p_id = Public_Ratings.p_id;

--6 --> search picture by date released range of years (RANGE OF VALUES EXAMPLE all movies from 1091 - 1994)
SELECT p_name as PictureName, p_releasedate as ReleaseDate
FROM Picture
WHERE 
    p_releasedate < 1995 AND p_releasedate > 1990
ORDER BY p_releasedate DESC;

--7 --> search for all pictures starred by a specific actor (ex. Terry Jones), and list release date of picture
SELECT p_name as PictureName, p_releasedate as ReleaseDate
FROM Picture, Cast_Member, Media_Cast_Member
WHERE 
    Picture.p_id = Media_Cast_Member.p_id AND Media_Cast_Member.ca_id = Cast_Member.ca_id
    AND ca_name = 'Terry Jones';

--8 --> average rating between the two public ratings for all picture entries in database
SELECT p_name as PictureName, p_releasedate as ReleaseDate, (pr_imdb + pr_tmdb)/2 as AveragePublicRating
FROM Picture, Public_Ratings
WHERE 
    Picture.p_id = Public_Ratings.p_id;

--9 --> count how many pictures in each streaming site, and print counts for all four streaming services
SELECT sum(sa_neflix) as NetflixPicturesCount, sum(sa_hulu) as HuluPicturesCount, sum(sa_primevid) as PrimevidPicturesCount, sum(sa_disneyplus) as DisneyplusPicturesCount
FROM Picture, Streaming_Availibility
WHERE 
    Picture.p_id = Streaming_Availibility.p_id;

--10 --> create new user entry in 'Media Watch List' table
INSERT INTO Media_Watch_List(w_id, u_id, p_id, w_watchstatus, w_completiondate) 
VALUES (5, 5, 'tm98978', 'Watching', '' );

--11 --> delete user for User table
DELETE FROM User WHERE u_username = 'frenzzy';

--12 --> delete all entires in media watch list for a user, in case they delete their account (ex. user: frenzzy)
DELETE FROM Media_Watch_list WHERE u_id = 1;

--13 --> return reviews and picture name of all public reviews with keyword 'boring' and movie has action genre
SELECT p_name as PictureName, r_comment as Comment
FROM User_Review, Picture
WHERE User_Review.p_id = Picture.p_id
AND (r_comment LIKE '%boring%' OR r_comment LIKE '%bored%')
AND p_genre LIKE '%action%';

--14 --> count the pictures per agerating for media a cast member 'Terry Jones' has been part of (group no-age ratings together too as one row)
SELECT count(DISTINCT(p_name)) as PicturesCount, p_agerating as AgeRating
FROM Picture, Cast_Member, Media_Cast_Member
WHERE Cast_Member.ca_id = Media_Cast_Member.ca_id
AND Media_Cast_Member.p_id = Picture.p_id
AND ca_name = 'Terry Jones'
GROUP BY(p_agerating);

--15 --> view picture names and rating of those movies, with genre having action and age rating NOT being TV-MA or R 
SELECT p_name as PictureName, p_agerating as AgeRating
FROM Picture
WHERE p_agerating NOT IN ('TV-MA','R', '')
AND p_genre LIKE '%action%';

--16 --> getting comments for deleted users (also adding u_id to SELECT to check if deleted in User table)
SELECT u_id, r_comment as PictureComment
FROM User_Review
WHERE u_id NOT IN (SELECT u_id FROM User);

--17 --> the average review of movies a cast member (ex. 'Terry Jones') has been in
SELECT DISTINCT(p_name) as MovieName,(pr_imdb + pr_tmdb)/2 as MovieAvgRating
FROM Cast_Member, Media_Cast_Member, Picture, Public_Ratings
WHERE Cast_Member.ca_id = Media_Cast_Member.ca_id 
AND Media_Cast_Member.p_id = Picture.p_id AND Picture.p_id = Public_Ratings.p_id
AND ca_name = 'Terry Jones';

--18 --> selecting all pictures which streaming availibility match with user streaming preference
SELECT p_name as PictureName
FROM Streaming_Availibility, Picture
WHERE Picture.p_id = Streaming_Availibility.p_id
AND (sa_neflix = (SELECT 1 FROM User WHERE u_preferredstreamsite = 'Netflix' AND u_username = 'jellybean')
OR sa_disneyplus = (SELECT 1 FROM User WHERE u_preferredstreamsite = 'Disney+' AND u_username = 'frenzzy')
OR sa_primevid = (SELECT 1 FROM User WHERE u_preferredstreamsite = 'Amazon Prime' AND u_username = 'frenzzy')
OR sa_hulu = (SELECT 1 FROM User WHERE u_preferredstreamsite = 'Hulu' AND u_username = 'frenzzy'));

--19 --> count the pictures per agerating for media cast member (ex. Terry Jones) has been part of 
--(group no-age ratings together too as one row)
SELECT p_agerating as AgeRating, count(DISTINCT(p_name)) as PicturesCount
FROM Picture, Cast_Member, Media_Cast_Member
WHERE Cast_Member.ca_id = Media_Cast_Member.ca_id
AND Media_Cast_Member.p_id = Picture.p_id
AND ca_name = 'Terry Jones'
GROUP BY(p_agerating)
ORDER BY (p_agerating) DESC;

--20 --> display the director names of those who have directed more than 30 pictures, and count of pictures directed 
SELECT ca_name as DirectorName, count(p_name) as PictureCount
FROM Picture, Cast_Member, Media_Cast_Member
WHERE Cast_Member.ca_id = Media_Cast_Member.ca_id
AND Media_Cast_Member.p_id = Picture.p_id
AND mcm_role = 'DIRECTOR'
GROUP BY ca_name HAVING count(*) > 30;
