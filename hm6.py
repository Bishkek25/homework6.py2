class Book:
    def __init__(self, title, author, year, read=False):
        self.title = title
        self.author = author
        self.year = year
        self.read = read

    def mark_as_read(self):
        self.read = True

    def mark_as_unread(self):
        self.read = False

    def __str__(self):
        status = "Прочитана" if self.read else "Непрочитана"
        return f"{self.title} автор: {self.author} ({self.year}) - {status}"


class Library:
    def __init__(self):
        self.books = []  # Список книг в библиотеке

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def list_books(self):
        if not self.books:
            return "В библиотеке нет книг."
        return "\n".join(str(book) for book in self.books)


# Пример использования
library = Library()

book1 = Book("Гордость и предубеждение", "Джейн Остен", 1813)
book2 = Book("И восходит солнце", "Эрнест Хемингуэй", 1926)

library.add_book(book1)
library.add_book(book2)

print("Книги в библиотеке:")
print(library.list_books())

# Отметим книгу как прочитанную и выведем ее статус
book1.mark_as_read()
print("\nСтатус книги после прочтения:")
print(book1)

# Отметим книгу как непрочитанную и выведем ее статус
book2.mark_as_unread()
print("\nСтатус книги после отметки как непрочитанная:")
print(book2)
