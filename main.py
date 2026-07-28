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
    print("4. Update Book")
    print('5. Issue Book')
    print('6. Return Book')
    print('7. Delete Book')
    print('8. Total Books')
    print('9. Exit')

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

    # 4. UPDATE BOOK
    elif choice == "4":

        if not books:
            print("No books found.")
            continue

        # Validate Book ID
        try:
            update_id = int(input("Enter Book ID to update: "))
        except ValueError:
            print("Book ID must be an integer.")
            continue

        found = False

        for book in books:
            if book["id"] == update_id:

                print("\nBook Details\n")
                print("-----------------------------------")
                print(f'Book ID   : {book["id"]}')
                print(f'Title     : {book["title"]}')
                print(f'Author    : {book["author"]}')
                print(f'Quantity  : {book["quantity"]}')
                print("-----------------------------------")

                # Validate Title
                title = input("Enter new title: ").strip()
                if not title:
                    print("Book title cannot be empty.")
                    continue

                # Validate Author
                author = input("Enter new author: ").strip()
                if not author:
                    print("Author name cannot be empty.")
                    continue

                # Validate Quantity
                try:
                    quantity = int(input("Enter new quantity: "))
                except ValueError:
                    print("Quantity must be an integer.")
                    continue

                if quantity < 0:
                    print("Quantity cannot be negative.")
                    continue

                # Update Book
                book["title"] = title
                book["author"] = author
                book["quantity"] = quantity

                save_books()

                print(f'Book ID {book["id"]} updated successfully!')
                found = True
                break

        if not found:
            print("Book not found.")


# 5. ISSUE BOOK:
    elif choice == "5":

        if not books:
            print('No books found')
            continue

        try:
           issue_book_id = int(input("Enter Book ID to Search: "))
        except ValueError:
            print('Book ID must be an integer')
            continue

        found = False

        for book in books:
            if book["id"] == issue_book_id:
                print('\nBook Found')
                print('------------------------------------')
                print(f'Book ID      : {book["id"]}')
                print(f'Title        : {book["title"]}')
                print(f'Author       : {book["author"]}')
                print(f'Quantity     : {book["quantity"]}')
                print("-------------------------------------")
                found = True

                if book["quantity"] == 0:
                    print("Book is Unavailable")
                    print("All copies of this book have been issued.")
                    break

                else:
                    book["quantity"] -= 1
                    save_books()
                    print(f'Book {book["title"]} has been issued successfully')
                    break

        if not found:
            print('\nBook not found')


# 6. RETURN BOOK:
    elif choice == "6":

        if not books:
            print('No books found')
            continue

        try:
            return_book_id = int(input("Enter Book ID to Return: "))
        except ValueError:
            print('Book ID must be an integer')
            continue

        found = False

        for book in books:
            if book["id"] == return_book_id:
                print('\nBook Found')
                print('------------------------------------')
                print(f'Book ID      : {book["id"]}')
                print(f'Title        : {book["title"]}')
                print(f'Author       : {book["author"]}')
                print(f'Quantity     : {book["quantity"]}')
                print("-------------------------------------")
                found = True

                book["quantity"] += 1
                save_books()
                print(f'Book {book["title"]} has been returned successfully')
                break

        if not found:
            print('\nBook not found')


# 7. DELETE BOOK:
    elif choice == "7":
        if not books:
            print('No books found')
            continue

        try:
            delete_book_id = int(input("Enter Book ID to delete: "))
        except ValueError:
            print('Book ID must be an integer')
            continue

        found = False

        for book in books:
            if book["id"] == delete_book_id:
                books.remove(book)
                print(f'Book {book["title"]} deleted successfully!')
                save_books()
                found = True
                break

        if not found:
            print("Book not found.")

# 8. TOTAL BOOKS:
    elif choice == "8":

        total_copies = 0

        for book in books:

            total_copies += book["quantity"]

        print("\n========== Library Statistics ==========\n")
        print("Total Book Copies: ", total_copies)
        print("Total Book Titles: ", len(books))
        print("\n========================================\n")


 # 9. EXIT
    elif choice == "9":
        print("Thank you for using Library Management System!")
        break
    else:
        print("Invalid choice.")
        print("Please enter a number between 1 and 9.")














