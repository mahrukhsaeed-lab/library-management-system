# LIBRARY MANAGEMENT SYSTEM



books=[]
all_books=[]

def add_book():
        try:    

            user_input=int(input("how many book you want to add: "))
            if user_input>=1:

                
                for i in range(0,user_input):
                    book=str(input("Enter the name of books you want to add: "))
                    
                    if not book.strip():
                        print("The field cannot be empty!")
                    else:    
                        books.append(book.strip()) 
                        all_books.append(book.strip())
                        print(books)
                        break
                  
 
            else:
                print("please enter positive number!")
                     
        except ValueError:
            print("Invalid input enter numberbs only!")


        
def show_books():
    
    print("Books in library are:")
    if books==[]:
        print("No books found")
    else: 
        for index,book in enumerate(books):   
            print(f"{index + 1}.{book}")



def search_book():
    
    name=input("Search Book:")
    if not name.strip():
        print("The field cannot be empty")
    elif name in books:
        print(f"{name} book found")
    else:
        print(f"{name}  book not found")


def issue_book():
    
    name=str(input("Enter the book name you want: "))
    if not name.strip():
        print("The field cannot be empty")
    else:    
        if name in books:
            books.remove(name)
            print(f" {name} book have been issued!")
        else:
            print("Not found") 

    


def return_book():
    
    name=input("Enter book name you want to return:")
    if name in all_books and name not in books:    
        books.append(name)
        print(f"{name} book returned successfully!")
    elif name in books:
        print(f"{name} book already found")
    else:
        print(f"Book {name} doesnt belong to our library!")    


def total_book():
    sum=0
    for book in range(len(books)+1):
        sum+=book
    print(f"Total number books in library are :{sum}")       

           

def exit_library():
    print("You have left library system")




while True:
    print(" -------- MENU --------")    
    print(f"1- Add books \n 2- Show books \n 3- Search book \n 4- Issue book \n 5- Return book \n 6- Total Books \n 7- Exit")
    choice=(input("select option: "))
    if choice=="1":
        add_book()
    elif choice=="2":
        show_books()
    elif choice=="3":
        search_book()
    elif choice=="4":
        issue_book()
    elif choice=="5":
        return_book()
    elif choice=="6":
        total_book() 
    elif choice=="7":
        exit_library()       
    else:
        print("invalid input")  


