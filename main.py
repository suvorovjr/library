"""Docstring"""
import os
from user_interface import UserInterface
from DBManager import DBManager

DB_HOST = os.getenv('localhost')
DB_NAME = os.getenv('library')
DB_USER = os.getenv('postgres')
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")

DB_HOST="127.0.0.1"
DB_NAME='my_db'
DB_USER='postgres'
DB_PASSWORD='2512'


def main():
    """main func"""
    # Создаем экземпляр класса DatabaseManager, передавая параметры для подключения к базе данных
    db_manager = DBManager(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)

    # Создаем таблицы в базе данных, если они еще не созданы
    db_manager.create_tables()

    print('Вас приветсвует приложение "Личная библиотека"')
    while True:
        user_input = UserInterface.main_menu()
        if user_input == "1":
            genres = 1
            user_choice, *new_book = UserInterface.add_new_book(genres)
            if user_choice == "2":
                db_manager.insert_new_genre(new_book[-1])
            db_manager.insert_new_book(new_book)
        elif user_input == "2":
            keyword = input("Введите ключевую фразу для поиска\n")
            book_by_keyword = db_manager.search_by_name(keyword)
            print(book_by_keyword)
        elif user_input == "3":
            genre_keyword = input("Введите жанр для поиска\n")
            book_by_keyword = db_manager.search_by_genre(genre_keyword)
            print(book_by_keyword)
        elif user_input == "4":
            books = db_manager.get_all_books()
            print(books)
        elif user_input == "5":
            break


if __name__ == "__main__":
    main()
