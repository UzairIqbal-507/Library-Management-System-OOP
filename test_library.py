
import unittest
from book import Book
from member import Member
from library import Library


class TestLibraryManagementSystem(unittest.TestCase):

    def setUp(self):
        # Create Library without loading or modifying JSON files
        self.library = Library.__new__(Library)

        self.library.books = []
        self.library.members = []
        self.library.transactions = []

        # Prevent tests from saving real data
        self.library.save_data = lambda: None

    # BOOK TESTS

    def test_book_issue(self):
        book = Book("B001", "Python", "John", "Programming")

        result = book.issue_book()

        self.assertTrue(result)
        self.assertFalse(book.availability)

    def test_book_return(self):
        book = Book("B001", "Python", "John", "Programming")
        book.issue_book()

        result = book.return_book()

        self.assertTrue(result)
        self.assertTrue(book.availability)

    def test_cannot_issue_already_issued_book(self):
        book = Book("B001", "Python", "John", "Programming")

        book.issue_book()
        result = book.issue_book()

        self.assertFalse(result)

    def test_cannot_return_available_book(self):
        book = Book("B001", "Python", "John", "Programming")

        result = book.return_book()

        self.assertFalse(result)

    # MEMBER TESTS

    def test_add_member_successfully(self):
        member = Member("M001", "Ali", "ali@gmail.com")

        self.library.add_member(member)

        self.assertEqual(len(self.library.members), 1)

    def test_duplicate_member_id(self):
        member1 = Member("M001", "Ali", "ali@gmail.com")
        member2 = Member("M001", "Ahmed", "ahmed@gmail.com")

        self.library.add_member(member1)
        self.library.add_member(member2)

        self.assertEqual(len(self.library.members), 1)

    def test_duplicate_member_email(self):
        member1 = Member("M001", "Ali", "ali@gmail.com")
        member2 = Member("M002", "Ahmed", "ALI@GMAIL.COM")

        self.library.add_member(member1)
        self.library.add_member(member2)

        self.assertEqual(len(self.library.members), 1)

    # LIBRARY ISSUE AND RETURN TESTS

    def test_issue_book_successfully(self):
        book = Book("B001", "Python", "John", "Programming")
        member = Member("M001", "Ali", "ali@gmail.com")

        self.library.books.append(book)
        self.library.members.append(member)

        self.library.issue_book("B001", "M001")

        self.assertFalse(book.availability)
        self.assertIn("B001", member.borrowed_books)

    def test_return_book_successfully(self):
        book = Book("B001", "Python", "John", "Programming")
        member = Member("M001", "Ali", "ali@gmail.com")

        self.library.books.append(book)
        self.library.members.append(member)

        self.library.issue_book("B001", "M001")
        self.library.return_book("B001", "M001")

        self.assertTrue(book.availability)
        self.assertNotIn("B001", member.borrowed_books)

    def test_cannot_issue_same_book_twice(self):
        book = Book("B001", "Python", "John", "Programming")
        member = Member("M001", "Ali", "ali@gmail.com")

        self.library.books.append(book)
        self.library.members.append(member)

        self.library.issue_book("B001", "M001")
        self.library.issue_book("B001", "M001")

        self.assertEqual(member.borrowed_books.count("B001"), 1)


if __name__ == "__main__":
    unittest.main()
