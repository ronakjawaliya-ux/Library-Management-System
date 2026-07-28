# 📚 Library Management System - Features

This project is a **menu-driven Library Management System** developed using **Python**. It allows users to manage library books efficiently while storing data permanently in a JSON file.

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
- Saves data automatically to `books.json`.

---

## 📚 View All Books

- Displays all books available in the library.
- Shows:
  - Book ID
  - Title
  - Author
  - Quantity
- Displays the total number of books.

---

## 🔍 Search Book

- Search for a book using its Book ID.
- Displays complete book information.
- Shows an appropriate message if the book is not found.

---

## ✏️ Update Book

- Update existing book information.
- Editable fields:
  - Title
  - Author
  - Quantity
- Saves updated information automatically.

---

## 🗑️ Delete Book

- Delete a book using its Book ID.
- Automatically updates the JSON file.
- Displays a success message after deletion.

---

## 📊 Total Books

Displays:

- Total number of books currently stored.

---

# 💾 Data Storage

- Permanent data storage using **JSON**.
- Automatically loads book records when the application starts.
- Automatically saves every change.
- Handles missing or corrupted JSON files gracefully.

---

# 🛡️ Input Validation

The application validates:

- Book ID must be numeric.
- Book Title cannot be empty.
- Author Name cannot be empty.
- Quantity must be zero or greater.
- Duplicate Book IDs are not allowed.

---

# ⚠️ Error Handling

The system handles:

- Invalid numeric inputs
- Missing book records
- Duplicate Book IDs
- Empty fields
- Negative quantities
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
- Exception Handling (`try-except`)
- Input Validation
- File Handling

---

# 🚀 Future Enhancements

- 📖 Book Issue System
- 📥 Book Return System
- 👤 Member Management
- 📅 Due Date Tracking
- 💰 Fine Calculation
- 📄 Borrowing History
- 🔍 Search by Title or Author
- 🗄️ SQLite/MySQL Database Integration
- 🖥️ GUI using Tkinter
- 🌐 Web Version using Flask or Django

---

# ✅ Project Highlights

- Menu-Driven CLI Application
- Beginner-Friendly Python Project
- Persistent JSON Data Storage
- CRUD Functionality
- Strong Input Validation
- Exception Handling
- Clean and Readable Code
- Easy to Extend and Maintain