
import re


def is_valid_text(value):
    return isinstance(value, str) and bool(value.strip())


def is_valid_email(email):
    if not isinstance(email, str):
        return False

    pattern = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"
    return re.match(pattern, email.strip()) is not None


def is_duplicate_book_id(books, book_id):
    return any(book.book_id.lower() == book_id.lower() for book in books)


def is_duplicate_member_id(members, member_id):
    return any(member.member_id.lower() == member_id.lower() for member in members)


def is_valid_choice(choice, minimum, maximum):
    try:
        number = int(choice)
        return minimum <= number <= maximum
    except (ValueError, TypeError):
        return False
