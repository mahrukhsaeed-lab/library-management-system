# LIBRARY MANAGEMENT SYSTEM


books=[]
def add_book():
    user_input=int(input("how many book you want to add: "))
    for i in range(0,user_input):
        book=input("Enter the name of books you want to add: ")
        books.append(book)
print(books)


def show_books():
    print("Books in library are:")
    for index,book in enumerate(books):
        print(f"{index}.{book}")



def search_book():
    name=input("Search Book:")
    if name in books:
        print(f"{name} book found")
    else:
        print(f"{book}  book not found")


def issue_book():
    name=input("Book name, you want to issue: ")
    if name in books:
        books.remove(name)
        print(f" {name} book have been issued!")
    else:
        print(f"{name} Book not found")  


def return_book():
    name=input("Enter book name you want to return:")
    if name not in books:
        books.append(name)
        print(f"{name} book returned successfully!")
    else:
        print(f"{name} book already found")


def total_book():
    sum=0
    for book in range(len(books)):
        sum+=book
    print(f"Total number books in library are :{sum}")       

           

def exit_library():
    print("You have left library system")

# choose the dersired option
while True:
    print(" -------- MENU --------")    
    print(f"1- Add books \n 2- Show books \n 3- Search book \n 4- Issue book \n 5- Return book \n 6- Total Books \n 7- Exit")
    choice=int(input("select option: "))
    if choice==1:
        add_book()
    elif choice==2:
        show_books()
    elif choice==3:
        search_book()
    elif choice==4:
        issue_book()
    elif choice==5:
        return_book()
    elif choice==6:
        total_book() 
    elif choice==7:
        exit_library()       
    else:
        print("invalid input")  

