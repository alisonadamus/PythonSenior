class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"'{self.title}' by {self.author}, published in {self.year}"


book1 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
book2 = Book("1984", "George Orwell", 1949)

print(book1.get_info())
print(book2.get_info())
