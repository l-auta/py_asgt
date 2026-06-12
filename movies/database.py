import sqlite3

conn = sqlite3.connect('moviestore.db')
cursor = conn.cursor()

# initialise the db 
cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,  
    genre TEXT NOT NULL,
    release_year INTEGER NOT NULL
)
''')
conn.commit()
print("Database created successfully.")

# function to add movies to the db 
def add_movie_db(title, genre, release_year):
    cursor.execute('''
    INSERT INTO movies (title, genre, release_year)
    VALUES (?, ?, ?)
    ''', (title, genre, release_year))
    conn.commit()
    print(f"\nMovie '{title}' added successfully to the database.")

# searching for a movie 
def search_movie_db(title):
    cursor.execute('''
    SELECT * FROM movies
    WHERE title = ?
    ''', (title,))
    movie = cursor.fetchone()
    if movie:
        print(f"Title: {movie[1]}, Genre: {movie[2]}, Release Year: {movie[3]}")
    else:
        print(f"No movie found with title '{title}'.")

# viewing movies 
def view_movies_db():
    cursor.execute('''
    SELECT * FROM movies
    ''')
    movies = cursor.fetchall()
    if not movies:
        print("No movies available.")
        return
    for movie in movies:
        print(f"Title: {movie[1]}, Genre: {movie[2]}, Release Year: {movie[3]}")
        print("-" * 20)

# update a movie 
def update_movie_db(title, new_title, new_genre, new_release_year):
    cursor.execute('''
    UPDATE movies
    SET title = ?, genre = ?, release_year = ?
    WHERE title = ?
    ''', (new_title, new_genre, new_release_year, title))
    conn.commit()
    print(f"Movie '{title}' updated successfully in the database.")

# delete a movie
def delete_movie_db(title):
    cursor.execute('''
    DELETE FROM movies
    WHERE title = ?
    ''', (title,))
    conn.commit()
    print(f"Movie '{title}' deleted successfully from the database.")