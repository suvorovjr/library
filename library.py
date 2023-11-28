class Book:

    def __init__(self, book_id: int, title: str, author: str, description: str, genre: str):
        """
        Конструктор класса
        :param title: Название книги
        :param author: Автор книги
        :param description: Описание книги
        :param genre: Жанр книги
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.description = description
        self.genre = genre

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, description={self.description}, genre={self.genre}"

    def __str__(self):
        return f"{self.book_id} - {self.title}"

    def get_all_information(self):
        """
        Выводит для пользователя всю информацию о книге.
        :return: Вся информация о книге
        """
        return f"Название: {self.title}, Автор: {self.author}, Описание:{self.description}, Жанр:{self.genre}"
