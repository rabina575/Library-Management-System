# Importing booksFile module.
import booksFile

def return_Book(person_Name, book_ID):
    ''' Validates returning user input.'''
    with open("books.txt", "r") as file:
        for line in file:
            book = line.split(",")
            if book[0] == book_ID:
                book_ins = booksFile.Book(book)
                if book_ins.check_Borrow(person_Name):
                    book_ins.return_Back(person_Name)
                    return True
                else:
                    print("\n" +"-" *78)
                    print(" Borrow record not found.")
                    print("-" *78 + "\n")
                    return False
        print("\n" +"-" *78)
        print(" Book not found.")
        print("-" *78 + "\n")
