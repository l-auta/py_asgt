
books = []
# define function to add a book 
def add_book(title, author, price, quantity):
    book = {
        'title': title,
        'author': author,
        'price': price,
        'quantity': quantity
    }
    books.append(book)
    print(f"\nBook '{title}' added successfully.")

# function to view all books 
# already being done by the db 
# def view_books():
#     if not books:
#         print("No books available.")
#         return
#     for book in books:
#         print(f"Title: {book['title']}, Author: {book['author']}, Price: {book['price']}, Quantity: {book['quantity']}")
#         print("-" * 20)

# function to get a book by its title 
def search_books(title):
    found_books = [book for book in books if book['title'] == title]
    if not found_books:
        print(f"No books found with title '{title}'.")
    else:
        for book in found_books:
            print(f"Title: {book['title']}, Author: {book['author']}, Price: {book['price']}, Quantity: {book['quantity']}")

# delete a book 
def delete_book(title):
    for book in books:
        if title.lower() == book['title'].lower():
            books.remove(book)
            print(f"Book '{title}' deleted successfully.")
            return
    print(f"Book '{title}' not found.")

# changing the contents of a book function 
def update_book(title, new_title, new_author, new_price, new_quantity):
    for book in books:
        if title.lower() == book['title'].lower():
            book['title'] = new_title
            book['author'] = new_author
            book['price'] = new_price
            book['quantity'] = new_quantity
            print(f"Book '{title}' updated successfully.")
            return
    print(f"Book '{title}' not found.")