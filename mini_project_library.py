from datetime import datetime
class Library:
    def __init__(self, book_name, lib_name):
        self.book_name = book_name
        self.lib_name = lib_name
        self.dic = {}

    def Display_book(self):
        print("Available books are: ")
        for book in self.book_name:
            print(book, end=", ")

    def Lend_book(self):
        book_name = input("Enter the book name: ")
        lend_book_name = book_name.upper()
        if lend_book_name in self.book_name:
            now = datetime.now()
            print("You can take this book at ",now)
            self.dic[lend_book_name] = lib_name
            self.book_name.remove(lend_book_name)
        elif lend_book_name in self.dic:
            print(f"This book already taken by {self.dic[lend_book_name]}")
        else:
            print("This book is not available in our library")

    def Return_book(self):
        book_name = input("Enter the book name: ")
        return_book_name = book_name.upper()
        if return_book_name in self.book_name:
            print("You have not issued it")
        elif return_book_name in self.dic:
            self.dic.pop(return_book_name)
            self.book_name.append(return_book_name)

    def Add_book(self):
        book_name = input("Enter the book name: ")
        add_book_name = book_name.upper()
        if add_book_name in self.book_name:
            print("This is already available in our library")
        elif add_book_name in self.dic:
            print("This is already available in our library, and taken by someone")
        else:
            print("Succesfully added this book")
            self.book_name.append(add_book_name)


print("*****Wellcome to collage library*****")
book_name = ["HARRY POTTER", 'POTHER PANCHALI', 'BYOKESH SOMOGRO']
lib_name = input("Enter your name: ")
Captain = Library(book_name, lib_name)

while True:
    user_input = int(input("\n Enter 1 for Display all books\n Enter 2 for Lend book\n Enter 3 for Return book\n Enter 4 for Add book\n Enter 5 for exit\n Enter: "))
    if user_input == 1:
        Captain.Display_book()
    elif user_input == 2:
        Captain.Lend_book()
    elif user_input == 3:
        Captain.Return_book()
    elif user_input == 4:
        Captain.Add_book()
    elif user_input == 5:
        print("Thanks for using our library")
        break
    else:
        print("Wrong input....")


