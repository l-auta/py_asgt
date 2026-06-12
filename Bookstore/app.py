from data import add_book, delete_book, update_book
from database import add_book_db, view_books_db, delete_book_db, update_book_db, search_books_db

def main():
    while True:
        print("\nBookstore Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            price = float(input("Enter book price: "))
            quantity = int(input("Enter book quantity: "))
            add_book(title, author, price, quantity)
            add_book_db(title, author, price, quantity)

        elif choice == '2':
            view_books_db()

        elif choice == '3':
            title = input("Enter book title to search: ")
            search_books_db(title)

        elif choice == '4':
            title = input("Enter book title to update: ")
            new_title = input("Enter new book title: ")
            new_author = input("Enter new book author: ")
            new_price = float(input("Enter new book price: "))
            new_quantity = int(input("Enter new book quantity: "))
            # update_book(title, new_title, new_author, new_price, new_quantity)
            update_book_db(title, new_title, new_author, new_price, new_quantity)

        elif choice == '5':
            title = input("Enter book title to delete: ")
            # delete_book(title)
            delete_book_db(title)

        elif choice == '6':
            print("Goodbye 🤗")
            break

        else:
            print("Invalid choice. Please try again.")

main()