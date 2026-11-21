
# Library Management System (OOP)

A Python-based Library Management System built using Object-Oriented Programming (OOP). This project provides a command-line interface (CLI) to manage books, members, borrowing, returning, transactions, and library records.

## Features

- Add, view, search, update, and delete books.
- Register, view, search, update, and delete members.
- Issue books to registered members.
- Return borrowed books.
- Prevent duplicate book and member IDs.
- Validate member email addresses.
- Track borrowed books for each member.
- Maintain transaction history with date and time.
- Search transaction records.
- Store data using JSON files.
- Automatically load and save library data.
- Create timestamped automatic backups.
- Restore data from the latest backups.
- Display library dashboard and reports.
- Show available and issued books.

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- File Handling
- Regular Expressions
- Python Standard Library

## Project Structure

```text
Library Management System (OOP)/
│
├── main.py
├── book.py
├── member.py
├── library.py
├── validation.py
├── storage.py
├── reports.py
│
├── data/
│   ├── books.json
│   ├── members.json
│   └── transactions.json
│
├── backups/
│
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/UzairIqbal-507/Library-Management-System-OOP.git
```

### 2. Navigate to the project directory

```bash
cd Library-Management-System-OOP
```

### 3. Run the application

```bash
python main.py
```

No external Python packages are required.

## Main Menu

The application provides the following operations:

1. Add Book
2. View All Books
3. Search Books
4. Update Book
5. Delete Book
6. Add Member
7. View All Members
8. Search Members
9. Update Member
10. Delete Member
11. Issue Book
12. Return Book
13. Transaction History
14. Search Transactions
15. Dashboard
16. Available Books
17. Issued Books
18. Restore Backup
0. Exit

## Data Storage

Library records are stored in JSON files:

- `books.json` — Book information.
- `members.json` — Member information and borrowed books.
- `transactions.json` — Issue and return history.

The application automatically saves changes and loads existing records when restarted.

## Backup and Recovery

The system automatically creates timestamped backups before saving updated records.

Users can restore the latest available backups through the Restore Backup menu option.

## Learning Objectives

This project demonstrates practical implementation of:

- Classes and Objects
- Constructors and Instance Attributes
- Encapsulation and Modular Programming
- Lists and Dictionaries
- Functions and Methods
- File Handling
- JSON Serialization and Deserialization
- Input Validation
- Exception Handling
- Basic Data Management

## Future Improvements

- Graphical User Interface (GUI)
- PostgreSQL database integration
- Admin and librarian authentication
- Book issue and return due dates
- Fine calculation system
- Advanced reporting

## Author

Muhammad Uzair Iqbal

**BS Data Science Student**

---

If you find this project useful, feel free to explore and improve it.
