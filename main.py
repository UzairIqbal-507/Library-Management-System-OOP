
from book import Book
from member import Member
from library import Library

from reports import (
    show_dashboard,
    show_available_books,
    show_issued_books
)


library = Library()


def main_menu():
    while True:
        print("\n")
        print("=" * 45)
        print("        LIBRARY MANAGEMENT SYSTEM")
        print("=" * 45)

        print("1.  Add Book")
        print("2.  View All Books")
        print("3.  Search Books")
        print("4.  Update Book")
        print("5.  Delete Book")
        print("6.  Add Member")
        print("7.  View All Members")
        print("8.  Search Members")
        print("9.  Update Member")
        print("10. Delete Member")
        print("11. Issue Book")
        print("12. Return Book")
        print("13. Transaction History")
        print("14. Search Transactions")
        print("15. Dashboard")
        print("16. Available Books")
        print("17. Issued Books")
        print("18. Restore Backup")
        print("0.  Exit")

        print("=" * 45)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            book_id = input("Enter Book ID: ").strip()
            title = input("Enter Title: ").strip()
            author = input("Enter Author: ").strip()
            category = input("Enter Category: ").strip()

            book = Book(book_id, title, author, category)
            library.add_book(book)

        elif choice == "2":
            library.show_books()

        elif choice == "3":
            keyword = input("Enter title, author, category or ID: ")
            library.search_books(keyword)

        elif choice == "4":
            book_id = input("Enter Book ID to update: ").strip()
            library.update_book(book_id)

        elif choice == "5":
            book_id = input("Enter Book ID to delete: ").strip()
            library.delete_book(book_id)

        elif choice == "6":
            member_id = input("Enter Member ID: ").strip()
            name = input("Enter Name: ").strip()
            email = input("Enter Email: ").strip()

            member = Member(member_id, name, email)
            library.add_member(member)

        elif choice == "7":
            library.show_members()

        elif choice == "8":
            keyword = input("Enter member ID, name or email: ")
            library.search_members(keyword)

        elif choice == "9":
            member_id = input("Enter Member ID to update: ").strip()
            library.update_member(member_id)

        elif choice == "10":
            member_id = input("Enter Member ID to delete: ").strip()
            library.delete_member(member_id)

        elif choice == "11":
            book_id = input("Enter Book ID: ").strip()
            member_id = input("Enter Member ID: ").strip()

            library.issue_book(book_id, member_id)

        elif choice == "12":
            book_id = input("Enter Book ID: ").strip()
            member_id = input("Enter Member ID: ").strip()

            library.return_book(book_id, member_id)

        elif choice == "13":
            library.show_transactions()

        elif choice == "14":
            keyword = input(
                "Search by transaction ID, book ID, member ID or action: "
            )
            library.search_transactions(keyword)

        elif choice == "15":
            show_dashboard(
                library.books,
                library.members,
                library.transactions
            )

        elif choice == "16":
            show_available_books(library.books)

        elif choice == "17":
            show_issued_books(library.books)

        elif choice == "18":
            library.restore_data()

        elif choice == "0":
            print("Thank you for using Library Management System!")
            break

        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main_menu()
