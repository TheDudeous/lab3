class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
    def __str__(self):
        return f"Название: {self.name}, Автор: {self.author}"
    def __eq__(self, y):
        return self.name == y.name and self.author == y.author