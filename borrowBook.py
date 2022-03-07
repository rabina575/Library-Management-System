# Importing booksFile module.
import booksFile

def borrow_Book(person_Name, book_ID):
    ''' Validates borrowing user input.'''
    with open('books.txt', 'r') as file:
        for line in file:
            book = line.split(",")
            if book[0] == book_ID:
                book_ins = booksFile.Book(book)
                if not book_ins.check_Borrow(person_Name):
                    if int(book_ins.book_Stock) < 1:
                        print("-" *78)
                        print(" Book out of Stock.")
                        print("-" *78+ "\n")
                        return False
                    book_ins.borrow(person_Name)
                    return True
                else:
                    print("\n" +"-" *78)
                    print(" You have already borrowed this book.")
                    print("-" *78+ "\n")
                    return False
        print("\n"+"-" *78)
        print(" Book not found.")
        print("-" *78 + "\n")
