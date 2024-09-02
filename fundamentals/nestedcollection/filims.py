movies = [
    # Malayalam Movies
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    }
]

#q1 total numberof movies

movies_count=len(movies)
print("movie_count",movies_count)

#q2 movies with genre drama

genre_filter=[mov.get("title")for mov in movies if "Drama"in mov.get("genres")]
print(genre_filter)

#q3 latest movie

def get_year(mov):

    return mov.get("year")

latest_movie=max(movies,key=get_year)

latest_movies=[mov.get("title")for mov in movies if mov.get("year")==latest_movie.get("year")]

print(latest_movies)

#q4 top movie(movie with highest rating)

def get_rating(mov):

    return mov.get("rating")

top_movie=max(movies,key=get_rating)

top_rating_movies=[mov.get("title")for mov in movies if mov.get("rating")==top_movie.get("rating")]
print(top_rating_movies)

#q5 movie with language malayalam

malayalam_movie=[mov.get("title")for mov in movies if mov.get("language")=="Malayalam"]
print(malayalam_movie)

#q6 movie released after year 2016

year_filter=[mov.get("title")for mov in movies if mov.get("year")>2016]
print(year_filter)

#q7 movie with lowest rating

def get_rating(mov):

    return mov.get("rating")

lowest_rating=min(movies,key=get_rating)


lowest_rating_movies=[mov.get("title")for mov in movies if mov.get("rating")==lowest_rating.get("rating")]

print(lowest_rating_movies)

#q9 oldest movie

def get_year(mov):

    return mov.get("year")
old_movie=min(movies,key=get_year)

oldest_movies=[mov.get("title")for mov in movies if mov.get("year")==old_movie.get("year")]
print(oldest_movies)

#q10 movie name with generes either drama or comedy

genres_filter=[mov.get("title")for mov in movies if "Comedy"in mov.get("genres")]

print(genres_filter)

#q11 malayalam movies with genere action

malayalam_action_movie=[mov.get("title")for mov in movies if "Drama"in mov.get("genres")and mov.get("language")=="Malayalam"]
print(malayalam_action_movie)

#q12 movie released in same years
movie_dictionary={}

for mov in movies:

    release_year=mov.get("year")

    if release_year in movie_dictionary:

        movie_dictionary.get(release_year).append(mov.get("title"))     # or movie_dictionary.get[release_year]+=1

    else:
        movie_dictionary[release_year]=[mov.get("title")]               # or movie_dictionary[release_year]=1
print(movie_dictionary)


#year count

years=[mov.get("year")for mov in movies]

years_count={y:years.count(y)for y in years}
print(years_count)

#genres list

genres_list={g for mov in movies for g in mov.get("genres")}

print(genres_list)

#action: drama:

genres=[g for mov in movies for g in mov.get("genres")]

genres_count={g:genres.count(g)for g in genres }
print(genres_count)

#sorting movies

def get_title(mov):

    return mov.get("title")

sorted_movies=sorted(movies,key=get_title)

sorted_movie_title=[mov.get("title")for mov in sorted_movies]

print(sorted_movie_title)

#            OR(using lambda function)
sorted_movies=sorted(movies,key=lambda mov:mov.get("title"))

sorted_movie_title=[mov.get("title")for mov in sorted_movies]
print(sorted_movie_title)
