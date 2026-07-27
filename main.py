#  Project--03 || Library Management System
#  using Python

import json


def save_books():
    with open('books.json', 'w') as f:
        json.dump(books, f, indent=4)


def load_books():
    try:
        with open('books.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


books = load_books()

while True:
    print('\n===== Library Management System =====\n')
    print('1. Add Book')
    print('2. View Books')
    print('3. Search Book')
    print('4. Issue Book')
    print('5. Return Book')
    print('6. Delete Book')
    print('7. Total Books')
    print('8. Exit')

    choice = input('Enter your choice: ')


# 1. ADD BOOK:
    if choice == '1':


        # Validate Book ID
        try:
            book_id = int(input('Enter Book ID: '))
        except ValueError:
            print('Book ID must be an integer')
            continue


        found = False
        for book in books:
            if book['id'] == book_id:
                found = True
                print(f'Book ID {book_id} already exists')
                break

        if not found:

            # Validate Title
             title = input('Enter Book Title: ').strip()
             if not title:
                 print('Book Title cannot be empty')
                 continue


             # Validate Author
             author = input('Enter Book Author: ').strip()
             if not author:
                 print('Book Author cannot be empty')
                 continue


             # Validate Quantity
             try:
                 quantity = int(input('Enter Book Quantity: '))
             except ValueError:
                 print(f"Please enter a valid number")
                 continue


             # Prevent zero or negative quantity
             if quantity <= 0:
                 print("Quantity must be greater than zero")
                 continue

             book = {
                 'id': book_id,
                 'title': title,
                 'author': author,
                 'quantity': quantity,
             }

             books.append(book)
             save_books()
             print(f'Book ID {book_id} has been added successfully')

# 2. VIEW BOOKS:
    elif choice == '2':
        if not books:
            print('No books found')
        else:
            print(f"\nTotal Books: {len(books)}")
            print("\nBooks List:\n")
            for book in books:
                print("------------------------------------")
                print(f'Book ID      : {book["id"]}')
                print(f'Title        : {book["title"]}')
                print(f'Author       : {book["author"]}')
                print(f'Quantity     : {book["quantity"]}')
                print("------------------------------------")

# 3. SEARCH BOOK:
    elif choice == '3':

        if not books:
            print('No books found')
            continue

        search_title = input("Enter Book Title to Search: ").strip().lower()

        found = False

        for book in books:
            if search_title in book["title"].lower():
                print("\nBook Found")
                print("-------------------------------------")
                print(f'Book ID      : {book["id"]}')
                print(f'Title        : {book["title"]}')
                print(f'Author       : {book["author"]}')
                print(f'Quantity     : {book["quantity"]}')
                print("-------------------------------------")
                found = True
                break

        if not found:
            print('Book not found')




