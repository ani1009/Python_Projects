class Library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books Present in this Library are :")
        for book in self.books:
            print("#" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f" You Have been Issued a {bookName}. Please Keep it Safe & Return it Within Time.")
            self.books.remove(bookName)
            return True
        else:
            print(" Sorry! This Book is Either Not Available Or Has Already been Issued to Someone Else.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks For Returning this Book! Hope You Enjoyed Reading it!")

class Student:
    def requestBook(self):
        self.book = input(" Which Book You Want to Borrow? : ")
        return self.book
    
    def returnBook(self):
        self.book = input(" Which Book You Want to Return? : ")
        return self.book

if __name__ == "__main__" :
    centralLibrary = Library(["History Of India","World Geography","Science & Tech","English Grammer"])
    student = Student()
    
    while(True):
        WelcomeMessage = ''' \n ******* Welcome to Central Library *******
        Please Select From Following Options :
        1. List Of All Books
        2. Request a Book
        3. Add / Return Book
        4. Exit the Library
        '''
        print(WelcomeMessage)
        a = int(input(" Enter Your Choice :"))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a ==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a ==3:
            centralLibrary.returnBook(student.returnBook())
        elif a ==4:
            print(" Thanks For Choosing Central Library! Visit again!")
            exit()
        
        else:
            print("Invalid Choice!")




