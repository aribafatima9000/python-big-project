import json

class Library:
    def __init__(self):
        self.books = []
        self.load_data()

    def add_book(self, title, author):
        book = {"title": title, "author": author, "issued": False}
        self.books.append(book)
        self.save_data()
        print(f"✅ Book '{title}' added successfully!")

    def display_books(self):
        if not self.books:
            print("📭 No books in library yet.")
            return
        print("\n📚 Library Books:")
        for i, book in enumerate(self.books, 1):
            status = "Issued" if book["issued"] else "Available"
            print(f"{i}. {book['title']} by {book['author']} [{status}]")

    def issue_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                if not book["issued"]:
                    book["issued"] = True
                    self.save_data()
                    print(f"📕 Book '{title}' issued successfully!")
                else:
                    print("⚠️ Book already issued!")
                return
        print("❌ Book not found!")

    def return_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                if book["issued"]:
                    book["issued"] = False
                    self.save_data()
                    print(f"📗 Book '{title}' returned successfully!")
                else:
                    print("⚠️ Book was not issued.")
                return
        print("❌ Book not found!")

    def search_book(self, keyword):
        results = [book for book in self.books if keyword.lower() in book["title"].lower()]
        if results:
            print("\n🔍 Search Results:")
            for book in results:
                status = "Issued" if book["issued"] else "Available"
                print(f"- {book['title']} by {book['author']} [{status}]")
        else:
            print("❌ No matching books found!")

    def save_data(self):
        with open("library.json", "w") as f:
            json.dump(self.books, f)

    def load_data(self):
        try:
            with open("library.json", "r") as f:
                self.books = json.load(f)
        except FileNotFoundError:
            self.books = []


# --- Main Program ---
def main():
    library = Library()
    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title, author)

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            title = input("Enter book title to issue: ")
            library.issue_book(title)

        elif choice == "4":
            title = input("Enter book title to return: ")
            library.return_book(title)

        elif choice == "5":
            keyword = input("Enter keyword to search: ")
            library.search_book(keyword)

        elif choice == "6":
            print("👋 Exiting Library System. Bye!")
            break

        else:
            print("❌ Invalid choice, try again!")

if __name__ == "__main__":
    main()
