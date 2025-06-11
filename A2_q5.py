from typing import Protocol

class Printable(Protocol):
    def to_string(self) -> str:
        ...

    
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def to_string(self) -> str:
        return f"Book: '{self.title}' by  {self.author}"
    

class Movie:
    def __init__(self, title: str, director: str):
        self.title = title
        self.director = director

    def to_string(self) -> str:
        return f"Movie: '{self.title}' by  {self.director}"
    

def print_item(item: Printable) -> None:
    print(item.to_string())


book = Book("Stranger in a Stange Land", "Robert A Heinlein")
movie = Movie("Isle of Dogs", "Wes Anderson")

print_item(book)
print_item(movie)