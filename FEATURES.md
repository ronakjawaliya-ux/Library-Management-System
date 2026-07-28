# 📚 Library Management System - Features

This project is a **menu-driven Library Management System** developed using **Python**. It enables users to efficiently manage library books through a Command-Line Interface (CLI). All book records are stored permanently in a **JSON** file, ensuring data is retained even after the application is closed.

---

# 📖 Book Management Features

## ➕ Add Book

- Add a new book to the library.
- Stores:
  - Book ID
  - Book Title
  - Author Name
  - Quantity
- Prevents duplicate Book IDs.
- Validates all user inputs.
- Automatically saves data to `books.json`.

---

## 📚 View All Books

- Displays all books available in the library.
- Shows:
  - Book ID
  - Title
  - Author
  - Quantity
- Displays the total number of book titles.

---

## 🔍 Search Book

- Search books using the **Book Title**.
- Case-insensitive search.
- Displays complete book information.
- Shows an appropriate message if no matching book is found.

---

## ✏️ Update Book

- Update existing book information.
- Editable fields:
  - Book Title
  - Author Name
  - Quantity
- Automatically saves updated information.

---

## 📖 Issue Book

- Issue a book from the library.
- Reduces the available quantity by one.
- Prevents issuing books that are out of stock.
- Automatically updates the JSON file.

---

## 📥 Return Book

- Return an issued book.
- Increases the available quantity by one.
- Automatically updates the JSON file.

---

## 🗑️ Delete Book

- Delete a book using its Book ID.
- Removes the book permanently from the library.
- Automatically updates the JSON file.
- Displays a success message after deletion.

---

## 📊 Library Statistics

Displays:

- Total Book Titles
- Total Book Copies Available

---

# 💾 Data Storage

- Permanent data storage using **JSON**.
- Automatically loads book records when the application starts.
- Automatically saves every modification.
- Handles missing or corrupted JSON files gracefully.

---

# 🛡️ Input Validation

The application validates:

- Book ID must be numeric.
- Duplicate Book IDs are not allowed.
- Book Title cannot be empty.
- Author Name cannot be empty.
- Quantity must be a valid integer.
- Quantity cannot be negative.
- Book availability before issuing.
- Book existence before updating, deleting, issuing, or returning.

---

# ⚠️ Error Handling

The system handles:

- Invalid numeric inputs
- Duplicate Book IDs
- Missing book records
- Empty book titles
- Empty author names
- Invalid quantities
- Negative quantities
- Book out of stock
- Missing JSON file
- Corrupted JSON file

---

# 🧠 Python Concepts Used

- Functions
- Loops
- Conditional Statements
- Lists
- Dictionaries
- CRUD Operations
- JSON File Handling
- File Handling
- Exception Handling (`try-except`)
- Input Validation
- Search Algorithms
- Inventory Management Logic

---

# 🚀 Future Enhancements

- 👤 Member Management System
- 📅 Due Date Tracking
- 💰 Late Fine Calculation
- 📄 Borrowing History
- 🔐 User Login Authentication
- 📤 Export Library Records to CSV
- 📊 Book Availability Reports
- 🗄️ SQLite/MySQL Database Integration
- 🖥️ Graphical User Interface (Tkinter)
- 🌐 Web Version using Flask or Django

---

# ✅ Project Highlights

- 📚 Complete Library Management System
- 💻 Menu-Driven CLI Application
- 💾 Persistent JSON Data Storage
- 🔄 Full CRUD Functionality
- 📖 Book Issue & Return Management
- 📊 Library Statistics
- 🛡️ Strong Input Validation
- ⚠️ Exception Handling
- 🧹 Clean & Readable Code
- 🚀 Beginner-Friendly and Easy to Extend