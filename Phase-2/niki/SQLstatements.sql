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
SELECT p_name as MovieName, w_watchstatus as WatchStatus, w_completiondate as CompletionDate
FROM Media_Watch_List, User, Picture
WHERE 
    User.u_id = Media_Watch_List.u_id AND Media_Watch_List.p_id = Picture.p_id AND
    u_username = 'jellybean';

--5 --> display all picture entries in database with the two types of public ratings 
SELECT p_name as MovieName, pr_imdb as IMDbRating, pr_tmdb as TMDbRating
FROM Picture, Public_Ratings
WHERE 
    Picture.p_id = Public_Ratings.p_id;

--6 --> search movie by date released range of years (RANGE OF VALUES EXAMPLE)
SELECT p_name as Movie, p_releasedate as ReleaseDate
FROM Picture
WHERE 
    p_releasedate < 1995 AND p_releasedate > 1990
ORDER BY p_releasedate DESC;

--7 --> search for all movies starred by a specific actor (ex. Terry Jones)
SELECT p_name as MovieName, p_releasedate as ReleaseDate
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


