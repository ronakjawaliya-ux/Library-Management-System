# 📚 Library Management System (Python)

A simple yet powerful **Library Management System** built using **Python** that allows users to manage books through a command-line interface (CLI). The application supports complete book management operations including adding, updating, searching, issuing, returning, and deleting books. All data is stored permanently using **JSON**, ensuring records remain available even after the program is closed.

---

## 🌟 Project Highlights

- 🚀 Built entirely using Python
- 💻 Command-Line Interface (CLI)
- 💾 JSON-based persistent data storage
- 📚 Complete Book Management System
- 🔄 Book Issue & Return functionality
- ✅ Input Validation
- ⚠️ Exception Handling using `try-except`
- 📂 Clean and beginner-friendly code structure

---

## 📌 Features

### 📖 Book Management

- ✅ Add New Book
- ✅ View All Books
- ✅ Search Book by Title
- ✅ Update Book Details
- ✅ Issue Book
- ✅ Return Book
- ✅ Delete Book Record
- ✅ Display Total Book Titles
- ✅ Display Total Book Copies

### 💾 Data Management

- ✅ Automatic JSON Data Saving
- ✅ Automatic JSON Data Loading

### 🛡️ Validation & Error Handling

- ✅ Book ID Validation
- ✅ Duplicate Book ID Prevention
- ✅ Title Validation
- ✅ Author Validation
- ✅ Quantity Validation
- ✅ Input Validation using `try-except`
- ✅ Handles Missing or Corrupted JSON Files

---

## 🛠️ Technologies Used

- Python 3
- JSON (Data Storage)

---

## 📂 Project Structure

```text
Library-Management-System/
│
├── main.py              # Main application
├── books.json           # Stores book records
├── README.md            # Project documentation
├── FEATURES.md          # Project features
├── .gitignore           # Ignore unnecessary files
└── screenshots/         # Application screenshots
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/ronakjawaliya-ux/Library-Management-System.git
```

### 2. Open the project folder

```bash
cd Library-Management-System
```

### 3. Run the application

```bash
python main.py
```

---

## 📋 Menu Options

```text
===== Library Management System =====

1. Add Book
2. View Books
3. Search Book
4. Update Book
5. Issue Book
6. Return Book
7. Delete Book
8. Total Books
9. Exit
```

---

## 💡 Features Explained

### ➕ Add Book

- Adds a new book to the library.
- Prevents duplicate Book IDs.
- Validates:
  - Book ID
  - Title
  - Author
  - Quantity

---

### 📚 View Books

- Displays every book available in the library.
- Shows:
  - Book ID
  - Title
  - Author
  - Quantity

---

### 🔍 Search Book

- Searches books by title.
- Case-insensitive search.
- Displays complete book information.

---

### ✏️ Update Book

- Updates an existing book.
- Editable fields:
  - Title
  - Author
  - Quantity
- Saves changes automatically.

---

### 📖 Issue Book

- Issues one copy of the selected book.
- Automatically decreases the available quantity.
- Prevents issuing books that are out of stock.

---

### 📥 Return Book

- Returns one copy of a selected book.
- Automatically increases the available quantity.

---

### 🗑️ Delete Book

- Deletes a selected book permanently.
- Updates the JSON file automatically.

---

### 📊 Total Books

Displays:

- Total Book Titles
- Total Book Copies

---

## ⚠️ Input Validation

The application validates:

- Book ID
- Duplicate Book IDs
- Empty Book Titles
- Empty Author Names
- Invalid Numeric Inputs
- Invalid Book Quantity
- Book Availability
- Book Existence
- Missing or Corrupted JSON Files

The application prevents:

- Duplicate Book IDs
- Empty fields
- Invalid quantities
- Invalid numeric inputs
- Operations on non-existing books

---

## 📄 Sample JSON

```json
[
    {
        "id": 101,
        "title": "Atomic Habits",
        "author": "James Clear",
        "quantity": 5
    },
    {
        "id": 102,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "quantity": 3
    },
    {
        "id": 103,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "quantity": 7
    }
]
```

---

## 📷 Sample Output

```text
========== Library Statistics ==========

Total Book Titles : 3
Total Book Copies : 15

========================================
```

---

## 📸 Screenshots

Application screenshots are available in the **screenshots/** folder.

- Main Menu
- Add Book
- View Books
- Search Book
- Update Book
- Issue Book
- Return Book
- Delete Book
- Total Books

---

## 🎯 Future Improvements

- 👤 Member Management
- 📅 Due Date Tracking
- 💰 Late Fine Calculation
- 📄 Borrowing History
- 📤 Export Library Data to CSV
- 🔐 Login Authentication
- 🗄️ SQLite/MySQL Database Integration
- 🖥️ Graphical User Interface (Tkinter)
- 🌐 Web Version using Flask or Django

---

## 📚 What I Learned

This project helped me strengthen my understanding of:

- Python Fundamentals
- Functions
- Loops & Conditional Statements
- Lists & Dictionaries
- CRUD Operations
- JSON File Handling
- Exception Handling (`try-except`)
- Input Validation
- Data Persistence
- Inventory Management Logic
- Problem-Solving
- Building Complete CLI Applications

---

## 👨‍💻 Author

**Ronak Jawalia**

- B.Tech CSE (AI & ML)
- Python Developer
- Learning Data Structures & Algorithms
- Building projects to strengthen programming skills

### GitHub

- **Profile:** https://github.com/ronakjawaliya-ux
- **Repository:** https://github.com/ronakjawaliya-ux/Library-Management-System

---

## ⭐ Support

If you found this project helpful or interesting, consider giving it a ⭐ on GitHub. It motivates me to continue learning, improve my programming skills, and build more real-world software projects.