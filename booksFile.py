# Importing the dateTime module.
import dateTime

class Book():
    """ A class used to represent Books."""
    def __init__(self, instance):
        self.book_ID = instance[0]
        self.book_Name = instance[1]
        self.book_Author = instance[2]
        self.book_Stock = instance[3]
        self.book_Cost = instance[4]

    def check_Borrow(self, person_Name):
        ''' Checks borrow record and returns a boolean value.'''
        with open('borrow_Record.txt', 'r') as file:
            for line in file:
                lend = line.split(",")
                if lend[0] == self.book_ID and lend[1].lower() == person_Name.lower():
                    return True

    def update_Stock(self):
        ''' Updates the stocks.'''
        with open("books.txt", "r") as file:
            lines = file.readlines()
            new_Lines = []
            for line in lines:
                book = line.split(",")
                if book[0] == self.book_ID:
                    updated_Line = f"{self.book_ID},{self.book_Name},{self.book_Author},{self.book_Stock},{self.book_Cost}"
                    new_Lines.append(updated_Line)
                else:
                    new_Lines.append(line)
            with open("books.txt", "w") as file:
                file.writelines(new_Lines)

    def borrow(self, person_Name):
        ''' Reduces the stock.'''
        with open("borrow_Record.txt", "a") as file:
            date = dateTime.getDate()
            time = dateTime.getTime()            
            file.write(f"{self.book_ID},{person_Name},{date}{time}\n")
        self.book_Stock = int(self.book_Stock) - 1
        self.update_Stock()

    def return_Back(self, person_Name):
        ''' Exception handling is used here. 
            It increases the stock and deletes the records when returned.'''
        while True:
            try:
                duration = int(input(" Enter the borrowed duration (in days): "))
                with open("borrow_Record.txt", "r") as file:
                    lines = file.readlines()
                    new_Lines = []
                    with open("borrow_Record.txt", "w") as file:
                        for line in lines:
                            lend = line.split(",")
                            lend[-1] = str(lend[-1]).replace("\n", "")
                            if lend[0] == self.book_ID and lend[1] == person_Name:
                                new_Lines.append(
                                    f"{lend[0]},{lend[1]},{lend[2]},{duration}\n")
                            else:
                                new_Lines.append(line)
                        file.writelines(new_Lines)
                self.book_Stock = int(self.book_Stock) + 1
                self.update_Stock()
                break
            except ValueError:
                print("\n" + "-" *78)
                print(" Please input the borrowed duration in numeric value.")
                print("-" *78 + "\n")
