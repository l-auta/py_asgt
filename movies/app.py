from database import add_movie_db, view_movies_db, update_movie_db, search_movie_db, delete_movie_db

def main():
    while True:
        print("\nMovie Management System")
        print("1. Add Movie")
        print("2. View Movies")
        print("3. Search Movie")
        print("4. Update Movie")
        print("5. Delete Movie")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter movie title: ")
            genre = input("Enter movie genre: ")
            release_year = int(input("Enter movie release year: "))
            add_movie_db(title, genre, release_year)

        elif choice == '2':
            view_movies_db()

        elif choice == '3':
            title = input("Enter movie title to search: ")
            search_movie_db(title)

        elif choice == '4':
            title = input("Enter movie title to update: ")
            new_title = input("Enter new movie title: ")
            new_genre = input("Enter new movie genre: ")
            new_release_year = int(input("Enter new movie release year: "))
            update_movie_db(title, new_title, new_genre, new_release_year)

        elif choice == '5':
            title = input("Enter movie title to delete: ")
            delete_movie_db(title)

        elif choice == '6':
            print("Goodbye 🤗")
            break

        else:
            print("Invalid choice. Please try again.")

main()