
from datetime import datetime

from validation import (
    is_duplicate_book_id,
    is_duplicate_member_id,
    is_valid_text,
    is_valid_email
)

from storage import (
    setup_storage,
    save_books,
    save_members,
    save_transactions,
    load_books,
    load_members,
    load_transactions,
    backup_file,
    restore_all_files,
    BOOKS_FILE,
    MEMBERS_FILE,
    TRANSACTIONS_FILE
)


class Library:
    def __init__(self):
        setup_storage()

        self.books = load_books()
        self.members = load_members()
        self.transactions = load_transactions()

    def save_data(self):
        backup_file(BOOKS_FILE)
        backup_file(MEMBERS_FILE)
        backup_file(TRANSACTIONS_FILE)

        save_books(self.books)
        save_members(self.members)
        save_transactions(self.transactions)

    # BOOK METHODS

    def add_book(self, book):
        if not all([
            is_valid_text(book.book_id),
            is_valid_text(book.title),
            is_valid_text(book.author),
            is_valid_text(book.category)
        ]):
            print("Error: Invalid book information.")
            return

        if is_duplicate_book_id(self.books, book.book_id):
            print("Error: Duplicate book ID.")
            return

        self.books.append(book)
        self.save_data()
        print("Book added successfully!")

    def show_books(self):
        print("\n========== ALL BOOKS ==========")

        if not self.books:
            print("No books found.")
            return

        for book in self.books:
            book.display_book()

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id.lower() == book_id.strip().lower():
                return book

        return None

    def search_books(self, keyword):
        keyword = keyword.strip().lower()

        if not keyword:
            print("Search keyword cannot be empty.")
            return

        found = False

        for book in self.books:
            if (
                keyword in book.title.lower()
                or keyword in book.author.lower()
                or keyword in book.category.lower()
                or keyword in book.book_id.lower()
            ):
                book.display_book()
                found = True

        if not found:
            print("No matching books found.")

    def update_book(self, book_id):
        book = self.find_book(book_id)

        if not book:
            print("Book not found.")
            return

        title = input("Enter new title: ").strip()
        author = input("Enter new author: ").strip()
        category = input("Enter new category: ").strip()

        if not all(map(is_valid_text, [title, author, category])):
            print("Invalid information. Update cancelled.")
            return

        book.title = title
        book.author = author
        book.category = category

        self.save_data()
        print("Book updated successfully!")

    def delete_book(self, book_id):
        book = self.find_book(book_id)

        if not book:
            print("Book not found.")
            return

        if not book.availability:
            print("Cannot delete an issued book.")
            return

        self.books.remove(book)
        self.save_data()
        print("Book deleted successfully!")

    # MEMBER METHODS

    def add_member(self, member):
        if not all([
            is_valid_text(member.member_id),
            is_valid_text(member.name),
            is_valid_email(member.email)
        ]):
            print("Error: Invalid member information.")
            return

        if is_duplicate_member_id(self.members, member.member_id):
            print("Error: Duplicate member ID.")
            return

        for existing_member in self.members:
            if existing_member.email.strip().lower() == member.email.strip().lower():
                print("Error: This email is already registered.")
                return

        self.members.append(member)
        self.save_data()
        print("Member added successfully!")

    def show_members(self):
        print("\n========== ALL MEMBERS ==========")

        if not self.members:
            print("No members found.")
            return

        for member in self.members:
            member.display_member()

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id.lower() == member_id.strip().lower():
                return member

        return None

    def search_members(self, keyword):
        keyword = keyword.strip().lower()

        if not keyword:
            print("Search keyword cannot be empty.")
            return

        found = False

        for member in self.members:
            if (
                keyword in member.member_id.lower()
                or keyword in member.name.lower()
                or keyword in member.email.lower()
            ):
                member.display_member()
                found = True

        if not found:
            print("No matching members found.")

    def update_member(self, member_id):
        member = self.find_member(member_id)

        if not member:
            print("Member not found.")
            return

        name = input("Enter new name: ").strip()
        email = input("Enter new email: ").strip()

        if not is_valid_text(name) or not is_valid_email(email):
            print("Invalid information. Update cancelled.")
            return

        for other in self.members:
            if (
                other is not member
                and other.email.strip().lower() == email.strip().lower()
            ):
                print("This email is already registered.")
                return

        member.name = name
        member.email = email

        self.save_data()
        print("Member updated successfully!")

    def delete_member(self, member_id):
        member = self.find_member(member_id)

        if not member:
            print("Member not found.")
            return

        if member.borrowed_books:
            print("Cannot delete a member with borrowed books.")
            return

        self.members.remove(member)
        self.save_data()
        print("Member deleted successfully!")

    # TRANSACTION METHODS

    def create_transaction(self, book_id, member_id, action):
        transaction_id = f"T{len(self.transactions) + 1:06d}"

        transaction = {
            "transaction_id": transaction_id,
            "book_id": book_id,
            "member_id": member_id,
            "action": action,
            "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.transactions.append(transaction)

    def issue_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if not book:
            print("Book not found.")
            return

        if not member:
            print("Member not found.")
            return

        if not book.availability:
            print("Book is already issued.")
            return

        if not book.issue_book():
            print("Unable to issue book.")
            return

        member.borrowed_books.append(book.book_id)

        self.create_transaction(
            book.book_id,
            member.member_id,
            "Issue"
        )

        self.save_data()
        print("Book issued successfully!")

    def return_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if not book:
            print("Book not found.")
            return

        if not member:
            print("Member not found.")
            return

        if book.availability:
            print("This book is not currently issued.")
            return

        if book.book_id not in member.borrowed_books:
            print("This member did not borrow this book.")
            return

        if not book.return_book():
            print("Unable to return book.")
            return

        member.borrowed_books.remove(book.book_id)

        self.create_transaction(
            book.book_id,
            member.member_id,
            "Return"
        )

        self.save_data()
        print("Book returned successfully!")

    def show_transactions(self):
        print("\n========== TRANSACTION HISTORY ==========")

        if not self.transactions:
            print("No transactions found.")
            return

        for transaction in self.transactions:
            print("-" * 40)
            print("Transaction ID:", transaction.get("transaction_id", "N/A"))
            print("Book ID       :", transaction.get("book_id", "N/A"))
            print("Member ID     :", transaction.get("member_id", "N/A"))
            print("Action        :", transaction.get("action", "N/A"))
            print("Date & Time   :", transaction.get("date_time", "N/A"))

        print("-" * 40)

    def search_transactions(self, keyword):
        keyword = keyword.strip().lower()

        if not keyword:
            print("Search keyword cannot be empty.")
            return

        found = False

        for transaction in self.transactions:
            searchable = [
                str(value).lower()
                for value in transaction.values()
            ]

            if any(keyword in value for value in searchable):
                print(transaction)
                found = True

        if not found:
            print("No matching transactions found.")

    # BACKUP RESTORE

    def restore_data(self):
        confirmation = input(
            "Restore the latest backup for all data files? (yes/no): "
        ).strip().lower()

        if confirmation != "yes":
            print("Restore cancelled.")
            return

        if restore_all_files():
            self.books = load_books()
            self.members = load_members()
            self.transactions = load_transactions()

            print("Latest backups restored successfully!")
        else:
            print("Restore failed. No data files were changed.")
