class Book :
    def __init__(self,book_id,title,author,category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.availability = True

    def display_book(self):
        print ("---------------------")
        print ("ID:",self.book_id)
        print ("Title:",self.title)
        print ("Author:",self.author)
        print ("Category:",self.category)
        if self.availability:
            print ("Availability: Available")
        else:
            print ("Availability: Issued")

    def issue_book(self):
        if self.availability:
            self.availability = False
            print ("Book issued successfully!")
        else:
            print ("Book already issued")

    def return_book(self):
        if not self.availability:
            self.availability = True
            print ("Book returned successfully!")
        else:
            print("Book was not issued")
