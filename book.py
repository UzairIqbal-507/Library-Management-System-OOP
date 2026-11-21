class Book:
    def __init__(self, book_id, title, author, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.availability = True

    def display_book(self):
        status = "Available" if self.availability else "Issued"

        print("-" * 40)
        print(f"ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Category: {self.category}")
        print(f"Availability: {status}")
        print("-" * 40)

    def issue_book(self):
        if not self.availability:
            return False

        self.availability = False
        return True

    def return_book(self):
        if self.availability:
            return False

        self.availability = True
        return True