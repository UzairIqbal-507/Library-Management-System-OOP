class Member:
    def __init__(self,member_id,name,email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def display_member(self):
        print("------------------")
        print(self.member_id)
        print(self.name)
        print(self.email)
        if self.borrowed_books:
            print("Borrowed books:",self.borrowed_books)
        else:
            print(f'Borrowed books: NONE')

