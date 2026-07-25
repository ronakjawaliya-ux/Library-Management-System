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