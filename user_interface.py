"""user interface"""
import os
from DBManager import DBManager


DB_HOST = os.getenv('localhost')
DB_NAME = os.getenv('library')
DB_USER = os.getenv('postgres')
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")

DB_HOST = "127.0.0.1"
DB_NAME = 'my_db'
DB_USER = 'postgres'
DB_PASSWORD = '2512'

"""Module providing a class for user interface"""


class UserInterface:
    """A class for
    user interface
    """

    @staticmethod
    def main_menu() -> str:
        """
        Функция отображения главного меню
        :return: выбор пользователя
        """

        print("Вы в главном меню. Выберите дейтсвие:")
        print("1 - Добавить новую книгу")
        print("2 - Поиск книги по ключевому слову")
        print("3 - Поиск книги по жанру")
        print("4 - Показать все книги в библиотеке")
        user_input = input('5 - Выход из приложения\n')
        return user_input

    @staticmethod
    def add_new_book(genres: int):
        """
        Функция пользовательского интерфейса для добавление новой книги.
        :param genres: список жанров
        :return: Данные новой книги.
        """
        # Создаем экземпляр класса DatabaseManager, передавая параметры для подключения к базе данных
        db_manager = DBManager(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)

        title = input("Введите название книги\n")
        author = input("Введите автора книги\n")
        description = input("Введите описание книги\n")
        print("Как задать жанр?")
        while True:
            print("1 - Выбрать из имеющихся")
            user_choice = input("2 - Задать новый жанр\n")
            if user_choice == "1":
                while True:
                    print("Выберите жанр:")
                    listgenres = db_manager.get_all_genres()
                    for i, x in [(i, x[0]) for i, x in enumerate(listgenres)]:
                        print(f"{i+1} - {x}")
                    genre_choice = int(input())
                    if 0 < genre_choice <= len(listgenres):
                        genre = [x[0] for x in listgenres][genre_choice - 1]
                        return user_choice, title, author, description, genre
                    else:
                        print("Ввод неверный. Укажите валидный номер.")
            elif user_choice == "2":
                genre = input("Введите свой жанр\n")
                return user_choice, title, author, description, genre
            else:
                print("Ввод неверный. Укажите валидный номер.")
