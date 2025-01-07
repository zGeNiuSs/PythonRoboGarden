class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def check_out(self):
        if self.is_available:
            self.is_available = False
            print(f"You have successfully checked out '{self.title}'.\n")
        else:
            print(f"Sorry, '{self.title}' is currently unavailable.\n")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"'{self.title}' has been successfully returned.\n")
        else:
            print(f"'{self.title}' was not checked out.\n")

    def display_info(self):
        status = "Available" if self.is_available else "Checked Out"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")

library_catalogue = []

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    book = Book(title, author)
    library_catalogue.append(book)
    print(f"Book '{title}' by {author} added to the catalogue.\n")

def list_books():
    if not library_catalogue:
        print("The catalogue is empty.\n")
    else:
        print("Books in the library catalogue:")
        for i, book in enumerate(library_catalogue, 1):
            print(f"{i}. ", end="")
            book.display_info()
        print()

def check_out_book():
    list_books()
    if library_catalogue:
        choice = int(input("Enter the number of the book you want to check out: ")) - 1
        if 0 <= choice < len(library_catalogue):
            library_catalogue[choice].check_out()
        else:
            print("Invalid choice. Please try again.\n")

def return_book():
    list_books()
    if library_catalogue:
        choice = int(input("Enter the number of the book you want to return: ")) - 1
        if 0 <= choice < len(library_catalogue):
            library_catalogue[choice].return_book()
        else:
            print("Invalid choice. Please try again.\n")

def main():
    while True:
        print("Library Catalogue System")
        print("1. Add a Book")
        print("2. List All Books")
        print("3. Check Out a Book")
        print("4. Return a Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
            check_out_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

main()
