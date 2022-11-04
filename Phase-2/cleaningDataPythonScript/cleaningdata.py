import pandas as pd
import os

#------add "type" column to indicate what show is from what stream site 
#netflix = 1, hulu = 2, prime = 3, disney = 4

#add 'type' = 1 to neflix data sets
data2 = pd.read_csv('netflix_raw/netflixtitles.csv', sep=',')
data2['stream'] = pd.Series([1 for x in range(len(data2.index))])
data2.to_csv('netflixtitlesNEW.csv', index=False)
data2 = pd.read_csv('netflix_raw/netflixcredits.csv', sep=',')
data2['stream'] = pd.Series([1 for x in range(len(data2.index))])
data2.to_csv('netflixcreditsNEW.csv', index=False)

#add 'type' = 2 to hulu data sets
data2 = pd.read_csv('hulu_raw/hulutitles.csv', sep=',')
data2['stream'] = pd.Series([2 for x in range(len(data2.index))])
data2.to_csv('hulutitlesNEW.csv', index=False)
data2 = pd.read_csv('hulu_raw/hulucredits.csv', sep=',')
data2['stream'] = pd.Series([2 for x in range(len(data2.index))])
data2.to_csv('hulucreditsNEW.csv', index=False)

#add 'type' = 3 to prime data sets
data2 = pd.read_csv('prime_raw/amazontitles.csv', sep=',')
data2['stream'] = pd.Series([3 for x in range(len(data2.index))])
data2.to_csv('amazontitlesNEW.csv', index=False)
data2 = pd.read_csv('prime_raw/amazoncredits.csv', sep=',')
data2['stream'] = pd.Series([3 for x in range(len(data2.index))])
data2.to_csv('amazoncreditsNEW.csv', index=False)

#add 'type' = 4 to prime data sets
data2 = pd.read_csv('disney_raw/disneyplustitles.csv', sep=',')
data2['stream'] = pd.Series([4 for x in range(len(data2.index))])
data2.to_csv('disneyplustitlesNEW.csv', index=False)
data2 = pd.read_csv('disney_raw/disneypluscredits.csv', sep=',')
data2['stream'] = pd.Series([4 for x in range(len(data2.index))])
data2.to_csv('disneypluscreditsNEW.csv', index=False)



#----merging of netflixtitlesNEW.csv, hulutitlesNEW.csv,,,,etc. data sets, then do same with credits data sets

#merging of tables which have basic movie related data
data1 = pd.read_csv('netflixtitlesNEW.csv')
data1.head()
data2 = pd.read_csv('hulutitlesNEW.csv')
data2.head()
data3 = pd.read_csv('amazontitlesNEW.csv')
data3.head()
data4 = pd.read_csv('disneyplustitlesNEW.csv')
data4.head()
concate_data = pd.concat([data1,data2,data3,data4])
concate_data.head()
concate_data.to_csv('ALLtitlesNEW.csv', index=False)

#merging of tables which have credits related data pertaining to movies (who was involved in movie?)
data1 = pd.read_csv('netflixcreditsNEW.csv')
data1.head()
data2 = pd.read_csv('hulucreditsNEW.csv')
data2.head()
data3 = pd.read_csv('amazoncreditsNEW.csv')
data3.head()
data4 = pd.read_csv('disneypluscreditsNEW.csv')
data4.head()
concate_data = pd.concat([data1,data2,data3,data4])
concate_data.head()
concate_data.to_csv('ALLcreditsNEW.csv', index=False)

#delete un-needed csv files now that merge happened and we will further operate on only merged set
os.remove('netflixtitlesNEW.csv')
os.remove('hulutitlesNEW.csv')
os.remove('amazontitlesNEW.csv')
os.remove('disneyplustitlesNEW.csv')
os.remove('netflixcreditsNEW.csv')
os.remove('hulucreditsNEW.csv')
os.remove('amazoncreditsNEW.csv')
os.remove('disneypluscreditsNEW.csv')

#for 'ALLtitlesNEW.csv' ---> delete 'description, runtime, production_countries,seasons,imdb_id, imdb_votes,tmdb_popularity' columns
#since those are not attributes anywhere in our schema
data = pd.read_csv('ALLtitlesNEW.csv', sep=',')
data.pop('description')
data.pop('runtime')
data.pop('production_countries')
data.pop('seasons')
data.pop('imdb_id')
data.pop('imdb_votes')
data.pop('tmdb_popularity')
data.to_csv('ALLtitlesREFINED.csv', index=False)

#remove 'character' column in 'ALLcreditsNEW.csv' since that's not an attribute anywhere in our schema
data = pd.read_csv('ALLcreditsNEW.csv', sep=',')
data.pop('character')
data.to_csv('ALLcreditsREFINED.csv', index=False)


#Now I Have:
#------------
#ALLcreditsREFINED.csv ---> columns: person_id,id,name,role,type
#ALLtitlesREFINED.csv --> columns: id,title,type,release_year,age_certification,genres,imdb_score,tmdb_score

#remove 'type' column in 'ALLtitlesREFINED.csv' before merging two datasets, since we only need 'type' in one data set to identify movie w/ streaming site
data = pd.read_csv('ALLtitlesREFINED.csv', sep=',')
data.pop('stream')
data.to_csv('ALLtitlesREFINED_NO_TYPE.csv', index=False) #note, blank values are NaN

#convert genre list to string of genres for visual purposes
data = pd.read_csv('ALLtitlesREFINED_NO_TYPE.csv', sep=',')
data["genres"]=data["genres"].str.replace(r']','', regex=True).astype(str)
data["genres"]=data["genres"].str.replace(r'[','', regex=True).astype(str)
data["genres"]=data["genres"].str.replace(r"'",'', regex=True).astype(str)
data.to_csv('ALLtitlesREFINED_NO_TYPE_NO_SET.csv', index=False)

#delete un-needed csv files that won't further be modified upon
os.remove('ALLcreditsNEW.csv')
os.remove('ALLtitlesNEW.csv')
os.remove('ALLtitlesREFINED_NO_TYPE.csv')

#merging the two data sets on movie ID
data = pd.read_csv('ALLtitlesREFINED_NO_TYPE_NO_SET.csv', sep=',')
data2 = pd.read_csv('ALLcreditsREFINED.csv', sep=',')
result = data.merge(data2, left_on='id', right_on='id')

#final set which has every movie and cast members of that movie, with other relevent movie related data
result.to_csv('FINALSET.csv', index=False) 

#we need the below csv data files for filtering our table schema data, which is done farther below
#-----------------------------------------------------------------------------
#'ALLtitlesREFINED_NO_TYPE_NO_SET.csv' --> for Picture, Public_Ratings tables
#'ALLtitlesREFINED.csv' --> Streaming_Availibility table (since we need stream column)
#'ALLcreditsREFINED.csv' --> for Cast_Member, Media_Cast_Member tables




# --------------------------TABLE SCHEMA DATA RETRIEVAL INTO CSV FILES --------------------------------

#PICTURE TABLE DATA
#------------------ need to extract data to idividual tables, add keys, and rename columns
#get 'picture' set from 'ALLtitlesREFINED_NO_TYPE_NO_SET.csv' by deleting rows and renaming columns
#columns from set: id,title,type,release_year,age_certification,genres,imdb_score,tmdb_score
#columns i need: id,title,type,release_year,age_certification,genres
#rename columns: p_id, p_name, p_type, p_releasedate, p_agerating, p_genre
data = pd.read_csv('ALLtitlesREFINED_NO_TYPE_NO_SET.csv', sep=',')
data.pop('imdb_score')
data.pop('tmdb_score')
data2 = data.rename(columns={"id":"p_id", "title":"p_name", "type":"p_type", "release_year":"p_releasedate", "age_certification":"p_agerating", "genres":"p_genre" })
data2.to_csv('picture.csv', index=False) 


#PUBLIC RATINGS DATA
#---------------
#Using: 'ALLtitlesREFINED_NO_TYPE_NO_SET.csv'
#columns from set: id,title,type,release_year,age_certification,genres,imdb_score,tmdb_score
#columns i need from set: id, imdb_score,tmdb_score    (+ add key for review set per movie)
#rename columns: pr_id, p_id, pr_imdb, pr_tmdb
data = pd.read_csv('ALLtitlesREFINED_NO_TYPE_NO_SET.csv', sep=',')
data.pop('title')
data.pop('type')
data.pop('release_year')
data.pop('age_certification')
data.pop('genres')
data.index.name = 'pr_id'
data2 = data.rename(columns={"id":"p_id", "imdb_score":"pr_imdb", "tmdb_score":"pr_tmdb" })
data2.to_csv('public_ratings.csv') 


#CAST MEMBER DATA
#-----------------
#Using: 'ALLcreditsREFINED.csv'
#columns from set: person_id,id,name,role,stream
#columns i need from set: person_id, name
#rename columns: ca_id, ca_name
data = pd.read_csv('ALLcreditsREFINED.csv', sep=',')
data.pop('id')
data.pop('role')
data.pop('stream')
data2 = data.rename(columns={"person_id":"ca_id", "name":"ca_name" })
data2.to_csv('cast_member.csv', index=False)

#MEDIA CAST MEMBER DATA
#----------------------
#Using: 'ALLcreditsREFINED.csv'
#columns from set: person_id,id,name,role,stream
#columns i need from set: person_id,id,role  (+ add primary key for each entry)
#rename columns: ca_id, p_id, mcm_role
data = pd.read_csv('ALLcreditsREFINED.csv', sep=',')
data.pop('stream')
data.pop('name')
data.index.name = 'mcm_id'
data2 = data.rename(columns={"person_id":"ca_id","id":"p_id", "role":"mcm_role" })
data2.to_csv('media_cast_member.csv')


#STREAMING AVAILIBILITY DATA
#Using: 'ALLtitlesREFINED_NO_TYPE_NO_SET.csv'
#columns from set: id,title,type,release_year,age_certification,genres,imdb_score,tmdb_score, stream
#columns i need from set: id, stream    (+ add primary key for stream availibity for every movie )
#rename columns: p_id, sa_hulu, sa_netflix, sa_primevid, sa_disney
#----------------------
data = pd.read_csv('ALLtitlesREFINED.csv', sep=',')
data.pop('title')
data.pop('type')
data.pop('release_year')
data.pop('age_certification')
data.pop('imdb_score')
data.pop('tmdb_score')
data.pop('genres')
data.index.name = 'sa_id'
data2 = data.rename(columns={"id":"p_id" })
data2[["sa_netflix", "sa_hulu", "sa_primevid", "sa_disney"]] = 0


#where stream = 1, set sa_netflix = 1, others to 0
data2.loc[data2['stream'] == 1, 'sa_netflix'] = 1
#where stream = 2, set sa_hulu = 1, others to 0
data2.loc[data2['stream'] == 2, 'sa_hulu'] = 1
#where prime = 3, set sa_prime = 1, others to 0
data2.loc[data2['stream'] == 3, 'sa_primevid'] = 1
#where disney = 4, set sa_disney = 1, others to 0
data2.loc[data2['stream'] == 4, 'sa_disney'] = 1
data2.pop('stream')

data2.to_csv('streaming_availability.csv')
