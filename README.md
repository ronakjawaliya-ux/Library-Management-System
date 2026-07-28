# 📚 Library Management System (Python)

A simple **Library Management System** built using **Python** that allows users to manage books through a command-line interface (CLI). Book records are stored permanently using **JSON**, ensuring data remains available even after the program is closed.

---

## 📌 Features

### 📖 Book Management

- ✅ Add New Book
- ✅ View All Books
- ✅ Search Book by ID
- ✅ Update Book Details
- ✅ Delete Book Record
- ✅ Display Total Number of Books

### 💾 Data Management

- ✅ Automatic JSON Data Saving
- ✅ Automatic JSON Data Loading

### 🛡️ Validation & Error Handling

- ✅ Book ID Validation
- ✅ Duplicate Book ID Prevention
- ✅ Title Validation
- ✅ Author Validation
- ✅ Quantity Validation
- ✅ Exception Handling using `try-except`
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
5. Delete Book
6. Total Books
7. Exit
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

### 📚 View Books

- Displays all books available in the library.
- Shows:
  - Book ID
  - Title
  - Author
  - Quantity

### 🔍 Search Book

- Search a book using its Book ID.
- Displays complete book information.

### ✏️ Update Book

- Update existing book information.
- Editable fields:
  - Title
  - Author
  - Quantity
- Saves updated information automatically.

### 🗑️ Delete Book

- Deletes a book using its Book ID.
- Automatically updates the JSON file.

### 📊 Total Books

Displays the total number of books currently stored.

---

## ⚠️ Input Validation

The application validates:

- Book ID
- Duplicate Book IDs
- Book Title
- Author Name
- Book Quantity

The application prevents:

- Invalid numeric inputs
- Empty titles
- Empty author names
- Negative quantities
- Duplicate Book IDs
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
    }
]
```

---

## 📷 Sample Output

```text
Book Details

-----------------------------------
Book ID   : 101
Title     : Atomic Habits
Author    : James Clear
Quantity  : 5
-----------------------------------
```

---

## 📸 Screenshots

Application screenshots are available in the **screenshots/** folder.

- Main Menu
- Add Book
- View Books
- Search Book
- Update Book
- Delete Book

---

## 🎯 Future Improvements

- 📖 Issue Book Feature
- 📥 Return Book Feature
- 👤 Member Management
- 📅 Due Date Tracking
- 💰 Fine Calculation
- 📄 Borrowing History
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

If you found this project helpful or interesting, consider giving it a ⭐ on GitHub. It motivates me to keep learning, improve my programming skills, and build more exciting projects.