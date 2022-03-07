# Importing all the modules.
import os
import booksFile
import borrowBook
import returnBook
import dateTime

LATE_FEES_PER_DAY = 0.5

def root():
    """ Main function of the project."""
    print()
    print("=" *78)
    print("\t\tWelcome to Library Management System.\(^0^)/" + u"\U0001F4DA")
    
    while True:
        ''' Shows the services provided by the system.
            Asks the user to select a choice.'''
        print("-" *78 + "\n")
        print(" To view the list of Books: PRESS 1")
        print(" To borrow a Book         : PRESS 2")
        print(" To return a Book         : PRESS 3")
        print(" To Exit                  : PRESS 4")
        print("\n" + "-" *78)
        # Exception handling is used.
        try:            
            choice = int(input(" Select your choice: "))
            print("-" *78)
            if choice == 1:
                print("_" *78)
                # View logic.
                books_List = []
                columns = [" BookID" , " Book Name","AuthorName", "Stock" , "  Cost"]

                with open("books.txt", 'r') as file:
                    for line in file:
                        book = line.split(',')
                        books_List.append(book)

                print("{:<5s} {:<30s} {:<20s} {:<10s} {}".format(
                    columns[0], columns[1], columns[2], columns[3], columns[4]))
                print("_" *78 +"\n")
                
                for book in books_List:
                    print("{:<5s} {:<30s} {:<20s}  {:<10s}{}".format(
                        " "+book[0], " "+book[1],book[2], book[3], u"\xA3" + book[4]), end="")

                print("_" *78 +"\n")
                
            elif choice == 2:
                # Borrow logic.
                add_to_receipt = []
                person_Name = input("\n Enter your full name: ")
                while True:
                    book_ID = input("\n"+" Enter the Book ID: ")
                    with open("books.txt","r") as file:
                        exists = False
                        for line in file:
                            book = line.split(",")
                            if book[0] == book_ID:
                                exists = True
                                break
                        if exists:
                            break
                        else:
                            print("\n" + "-" *78)
                            print(" Book not Found")
                            print("-" *78)
                            
                if borrowBook.borrow_Book(person_Name, book_ID):
                    add_to_receipt.append(book_ID)
                while True:
                    another = input(
                        " Do you want to add another book? (y/n): ")
                    if another.lower() == "n":
                        break
                    elif another.lower() == "y":
                        next_Book = input("\n Enter another Book ID: ")
                        if borrowBook.borrow_Book(person_Name, next_Book):
                            add_to_receipt.append(next_Book)
                    else:
                        print(" Enter a valid response!")

                data = []
                sub_total = 0
                with open("Books.txt", "r") as file:
                    for line in file:
                        book = line.split(",")
                        for each_id in add_to_receipt:
                            if book[0] == each_id:
                                data.append(
                                    [book[0], book[1], book[2], book[4]])
                                sub_total += float(book[4])
                for book in data:
                    book[-1] = str(book[-1]).replace("\n", "")
                    
                # Creating borrow receipt in txt and shell.
                with open(f"borrow_Receipt/{person_Name}.txt", "w+") as file:
                    file.write("="*72 + "\n\n")
                    file.write("                       Library Management System" + "\n")
                    file.write("_"*72 + "\n")
                    file.write(" Date: "+dateTime.getDate()+"                                 Time: " +dateTime.getTime()+"\n")
                    file.write("_"*72 + "\n")
                    file.write(f"\n Borrower Name: {person_Name}\n\n")
                    file.write("-"*72 + "\n")
                    file.write("{:<6s} {:<7s} {:<29s} {:<20s} {}".format(
                        " SNo.", "BookID","BookName", "AuthorsName", " Cost" +"\n"))
                    file.write("-"*72 + "\n")
                    SNo = 0
                    for book in data:
                        SNo = SNo + 1
                        file.write(
                            "{:<1s}{:<5d} {:<5s} {:<30s} {:<20s}{}\n".format("",SNo, book[0], book[1], book[2],"£"+book[3]))
                    file.write("-"*72 + "\n")                
                    file.write("\n Last date of Return: "+dateTime.getReturnDate()+"\n")
                    file.write(
                        f" Late fees per day after 10 days will be: £{LATE_FEES_PER_DAY}\n\n")
                    file.write("_"*72 + "\n\n")
                    file.write(f"\t\t\t\t\t\tSub-Total: £{sub_total} \n\n")
                    file.write("="*72)

                    print("\n  "+"-"*74)
                    print(f"   borrow_Receipt/{person_Name}.txt")
                    print("   "+"="*72)
                    print("\n                          Library Management System")
                    print("   "+"_"*72)
                    print("\n   "+" Date: "+dateTime.getDate()+"                                 Time: " +dateTime.getTime())
                    print("   "+"_"*72 )
                    print(f"\n    Borrower Name: {person_Name}\n")
                    print("   "+"-"*72)
                    print("{:<6s} {:<7s} {:<29s} {:<20s} {}".format(
                            "    SNo.", "BookID","BookName", "AuthorsName", " Cost"))
                    print("   "+"-"*72)
                    SNo = 0
                    for book in data:
                        SNo = SNo + 1
                        print(
                                "{:<1s}   {:<5d}{:<5s} {:<30s} {:<20s}{}\n".format("",SNo, book[0], book[1], book[2],"£"+book[3]))
                    print("   "+"-"*72)                
                    print("\n   "+" Last date of Return: "+dateTime.getReturnDate())
                    print(
                            f"    Late fees per day after 10 days will be: £{LATE_FEES_PER_DAY}\n")
                    print("   "+"-"*72 + "\n")
                    print(f"\t\t\t\t\t\t   Sub-Total: £{sub_total}\n")
                    print("   "+"="*72 + "\n")                    
                    print("  "+"-"*74 + "\n")

            elif choice == 3:
                # Return logic.
                data = []
                sub_total = 0
                total_late_fees = 0
                add_to_receipt = []
                
                # Checks whether name exists.
                while True:
                    person_Name = input("\n Enter your full name: ")
                    exists = False
                    with open("borrow_Record.txt","r") as file:
                        for line in file:
                            lend = line.split(",")
                            
                            if lend[1] == person_Name :
                                exists = True
                                break
                    if exists:
                        break
                    else:
                        print("\n" + "-" *78)
                        print(f" Cannot find borrow record with the name: {person_Name}")
                        print("-" *78)
                        
                # Checks whether book ID exists.       
                while True:
                    book_ID = input("\n"+" Enter the Book ID: ")
                    with open("borrow_Record.txt","r") as file:
                        exists = False
                        for line in file:
                            book = line.split(",")
                            if lend[0] == book_ID:
                                exists = True
                                break
                        if exists:
                            break
                        else:
                            print("\n" + "-" *78)
                            print(" Book not Found")
                            print("-" *78)

                
                if returnBook.return_Book(person_Name, book_ID):
                    with open("books.txt", "r") as file:
                        for line in file:
                            book = line.split(",")
                            if book[0] == book_ID:
                                with open("borrow_Record.txt", "r") as borrow_Bundle:
                                    lines = borrow_Bundle.readlines()
                                    new_Lines = []
                                    for line in lines:
                                        lend = line.split(",")
                                        lend[-1] = str(lend[-1]).replace("\n", "")
                                        if lend[0] == book_ID and lend[1].lower() == person_Name.lower():
                                            data.append(
                                                [book[0], book[1], book[2], lend[3], book[4]])
                                            sub_total += float(book[4])
                                            if int(lend[3]) > 10:
                                                total_late_fees += (int(lend[3]) - 10) * \
                                                    LATE_FEES_PER_DAY
                                        else:
                                            new_Lines.append(line)
                                    with open("borrow_Record.txt", "w") as file:
                                        file.writelines(new_Lines)

                while True:
                    another = input(" Do you want to return another book? (y/n): ")
                    if another.lower() == "n":
                        break
                    elif another.lower() == "y":
                        next_Book = input("\n Enter another Book ID: ")
                        if returnBook.return_Book(person_Name, next_Book):
                            with open("books.txt", "r") as file:
                                for line in file:
                                    book = line.split(",")
                                    if book[0] == next_Book:
                                        with open("borrow_Record.txt", "r") as borrow_Bundle:
                                            lines = borrow_Bundle.readlines()
                                            new_Lines = []
                                            for line in lines:
                                                lend = line.split(",")
                                                lend[-1] = str(lend[-1]).replace("\n", "")
                                                if lend[0] == next_Book and lend[1].lower() == person_Name.lower():
                                                    data.append(
                                                        [book[0], book[1], book[2], lend[3], book[4]])
                                                    sub_total += float(book[4])
                                                    if int(lend[3]) > 10:
                                                        total_late_fees += (int(lend[3]) - 10) * \
                                                            LATE_FEES_PER_DAY
                                                else:
                                                    new_Lines.append(line)
                                            with open("borrow_Record.txt", "w") as file:
                                                file.writelines(new_Lines)
                
                    else:
                        print(" Enter a valid response!")

                for book in data:
                    book[-1] = str(book[-1]).replace("\n", "")

                # Creating return receipt in txt and shell.
                with open(f"return_Receipt/{person_Name}.txt", "w+") as file:
                    file.write("="*72 + "\n\n")
                    file.write("                       Library Management System" + "\n")
                    file.write("_"*72 + "\n")
                    file.write(" Date: "+dateTime.getDate()+"                                 Time: " +dateTime.getTime()+"\n")
                    file.write("_"*72 + "\n")
                    file.write(f"\n Returned By: {person_Name}\n\n")
                    file.write("-"*72 + "\n")
                    file.write("{:<6s} {:<7s} {:<29s} {:<20s} {}".format(
                        " SNo.", "BookID","BookName", "AuthorsName", " Cost" +"\n"))
                    file.write("-"*72 + "\n")
                    SNo = 0
                    for book in data:
                        SNo = SNo + 1
                        file.write(
                            "{:<1s}{:<5d} {:<5s} {:<30s} {:<20s}{}\n".format("",SNo, book[0], book[1], book[2],"£"+book[4]))
                    file.write("-"*72 + "\n")                
                    file.write("\n Borrowed Duration in days: "+book[3])
                    file.write(
                        f"\n Late fees per day after 10 days will be: £{LATE_FEES_PER_DAY}\n\n")
                    file.write("_"*72 + "\n\n")
                    file.write(f"\t\t\t\t\t\tSub-Total: £{sub_total}\n")
                    file.write(f"\t\t\t\t\t\tLate-Fees: £{total_late_fees}\n")
                    total_fees = sub_total + total_late_fees
                    two_float = "{:.2f}".format(total_fees)
                    file.write(f"\t\t\t\t\t\tTotal    : £{total_fees}\n\n")
                    file.write("="*72)

                    print("\n  "+"-"*74)
                    print(f"   return_Receipt/{person_Name}.txt")
                    print("   "+"="*72)
                    print("\n                          Library Management System")
                    print("   "+"_"*72)
                    print("\n   "+" Date: "+dateTime.getDate()+"                                 Time: " +dateTime.getTime())
                    print("   "+"_"*72)
                    print(f"\n    Returned By: {person_Name}\n")
                    print("   "+"-"*72)
                    print("{:<6s} {:<7s} {:<29s} {:<20s} {}".format(
                            "    SNo.", "BookID","BookName", "AuthorsName", " Cost"))
                    print("   "+"-"*72)
                    SNo = 0
                    for book in data:
                        SNo = SNo + 1
                        print(
                                "{:<1s}   {:<5d}{:<5s} {:<30s} {:<20s}{}\n".format("",SNo, book[0], book[1], book[2],"£"+book[4]))
                    print("   "+"-"*72)
                    print("\n    Borrowed Duration in days: "+book[3])
                    print(
                            f"    Late fees per day after 10 days will be: £{LATE_FEES_PER_DAY}\n")
                    print("   "+"-"*72 + "\n")
                    print(f"\t\t\t\t\t\t   Sub-Total: £{sub_total}")
                    print(f"\t\t\t\t\t\t   Late-Fees: £{total_late_fees}")
                    total_fees = sub_total + total_late_fees
                    two_float = "{:.2f}".format(total_fees)
                    print(f"\t\t\t\t\t\t   Total    : £{total_fees}\n")
                    print("   "+"="*72 + "\n")
                    print("  "+"-"*74 + "\n")

            elif choice == 4:
                # Exit logic.
                print("\t\t\tThank You and Have a Nice Day!")
                print("="*78)
                break
            
            else:
                print(" Invalid choice. Try again.")
                
        except ValueError:
            print("\n" + "-" *78)
            print(" Please enter 1/2/3/4.")
            print("-" *78 + "\n")

if __name__ == "__main__":
    ''' Creates receipt destination if it does not exist.'''
    if not os.path.exists("borrow_Receipt"):
        os.makedirs("borrow_Receipt")
    if not os.path.exists("return_Receipt"):
        os.makedirs("return_Receipt")
    root()
