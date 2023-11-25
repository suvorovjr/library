class Book:

    def __init__(self, title, author, description, genre):
        """
        Конструктор класса
\        :param title: Название книги
        :param author: Автор книги
        :param description: Описание книги
        :param genre: Жанр книги
        """

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

        return f"Название: {self.title}\nАвтор: {self.author}\nОписание:{self.description}\nЖанр:{self.genre}"
