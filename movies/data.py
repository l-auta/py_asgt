
movies = []

# adding movies to the list 
def add_movie(title, genre, release_year):
    movie = {
        'title': title,
        'genre': genre,
        'release_year': release_year
    }
    movies.append(movie)
    print(f"\nMovie '{title}' added successfully.")

# add others when adding to a json file 