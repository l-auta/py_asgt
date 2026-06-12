import sqlite3

conn = sqlite3.connect('bookstore.db')
cursor = conn.cursor()

# start by creating the table books in the initalised database 
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
''')
conn.commit()
print("Database created successfully.")
# add athe book to the db 
def add_book_db(title, author, price, quantity):
    cursor.execute('''
    INSERT INTO books (title, author, price, quantity)
    VALUES (?, ?, ?, ?)
    ''', (title, author, price, quantity))
    conn.commit()
    print(f"Book '{title}' added successfully.")

# update our book in the db 
def update_book_db(title, new_title, new_author, new_price, new_quantity):
    cursor.execute('''
    UPDATE books
    SET title = ?, author = ?, price = ?, quantity = ?
    WHERE title = ?
    ''', (new_title, new_author, new_price, new_quantity, title))
    conn.commit()
    print(f"Book '{title}' updated successfully.")

# delete the book from the db 
def delete_book_db(title):
    cursor.execute('''
    DELETE FROM books
    WHERE title = ?
    ''', (title,))
    conn.commit()
    print(f"Book '{title}' deleted successfully.")

# fetch to see all books in the db
def view_books_db():
    cursor.execute('''
    SELECT * FROM books
    ''')
    books = cursor.fetchall()
    if not books:
        print("No books available.")
        return
    for book in books:
        print(f"Title: {book[1]}, Author: {book[2]}, Price: {book[3]}, Quantity: {book[4]}")
        print("-" * 20)