
def get_library_summary(books, members, transactions):
    total_books = len(books)
    available_books = sum(1 for book in books if book.availability)
    issued_books = total_books - available_books

    return {
        "total_books": total_books,
        "available_books": available_books,
        "issued_books": issued_books,
        "total_members": len(members),
        "total_transactions": len(transactions)
    }


def show_dashboard(books, members, transactions):
    summary = get_library_summary(books, members, transactions)

    print("\n========== LIBRARY DASHBOARD ==========")
    print(f"Total Books       : {summary['total_books']}")
    print(f"Available Books   : {summary['available_books']}")
    print(f"Issued Books      : {summary['issued_books']}")
    print(f"Total Members     : {summary['total_members']}")
    print(f"Transactions      : {summary['total_transactions']}")
    print("=======================================")


def show_available_books(books):
    print("\n========== AVAILABLE BOOKS ==========")

    available = [book for book in books if book.availability]

    if not available:
        print("No books are currently available.")
        return

    for book in available:
        print(f"{book.book_id} | {book.title} | {book.author}")


def show_issued_books(books):
    print("\n========== ISSUED BOOKS ==========")

    issued = [book for book in books if not book.availability]

    if not issued:
        print("No books are currently issued.")
        return

    for book in issued:
        print(f"{book.book_id} | {book.title} | {book.author}")
