
# Library Management System (OOP)

A command-line Library Management System built using Python and Object-Oriented Programming (OOP). It manages books, members, borrowing, returning, transactions, and data persistence using JSON files.

## Features

- Add, view, update, and delete books
- Add, view, update, and delete members
- Issue and return books
- Track borrowed books
- Prevent duplicate book IDs, member IDs, and email addresses
- Validate user input
- Store data using JSON files
- Create data backups
- Restore data from backups
- View library reports and dashboard
- Unit testing using Python unittest

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- Regular Expressions
- Unittest

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
├── test_library.py
│
├── data/
│   ├── books.json
│   ├── members.json
│   └── transactions.json
│
├── backups/
├── README.md
└── .gitignore
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/UzairIqbal-507/Library-Management-System-OOP.git
```

2. Open the project folder:

```bash
cd Library-Management-System-OOP
```

3. Run the application:

```bash
python main.py
```

## Run Unit Tests

Execute:

```bash
python -m unittest discover -s . -p "test_library.py" -v
```

## Learning Objectives

This project helped me practice:

- Classes and Objects
- Constructors and Instance Attributes
- Encapsulation
- Modular Programming
- Functions and Exception Handling
- File Handling
- JSON Data Persistence
- Input Validation
- Unit Testing

## Author

**Muhammad Uzair Iqbal**

BS Data Science Student

GitHub: [UzairIqbal-507](https://github.com/UzairIqbal-507)

---

*Built as a Python OOP learning project.*
