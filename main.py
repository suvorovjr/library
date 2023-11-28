import os
from user_interface import UserInterface
from library import Book
from utils import get_books
from DBManager import DBManager

DB_HOST = 'localhost'
DB_NAME = 'library'
DB_USER = 'postgres'
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")


def main():
    # Создание экземпляра класса DatabaseManager, передавая параметры для подключения к базе данных
    db_manager = DBManager(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)

    # Создание базы данных, если она еще не существует
    db_manager.create_database()

    # Создание таблиц в базе данных, если они еще не созданы
    db_manager.create_tables()

    print('Вас приветсвует приложение "Личная библиотека"')
    while True:
        user_input = UserInterface.main_menu()
        if user_input == "1":
            genres = [genre[0] for genre in db_manager.get_all_genres()]
            new_book = UserInterface.add_new_book(genres)
            if new_book[-1] == "2":
                db_manager.insert_new_genre([new_book[-2]])
            db_manager.insert_new_book(new_book[:-1])
            print("Книга успешно добавлена")
        elif user_input == "2":
            keyword = input("Введите ключевую фразу для поиска\n")
            book_by_keyword = db_manager.search_by_name(keyword)
            search_books = [book for book in get_books(book_by_keyword)]
            [print(f"{i} - {book}") for i, book in enumerate(search_books, start=1)]
            user_coise = UserInterface.book_interface()
            if user_coise != "3":
                try:
                    select_book = search_books[int(input("Выберите книгу по ее индексу:\n")) - 1]
                    if user_coise == "1":
                        print(select_book.get_all_information())
                    else:
                        db_manager.delete_book(select_book.title)
                except IndexError:
                    print("Указан неверный индекс.")
        elif user_input == "3":
            genres = [genre[0] for genre in db_manager.get_all_genres()]
            [print(f"{i} - {genre}") for i, genre in enumerate(genres, start=1)]
            genre_keyword = genres[int(input("Введите жанр для поиска\n")) - 1]
            print(genre_keyword)
            search_books = [book for book in get_books(db_manager.search_by_genre(genre_keyword))]
            print(search_books)
            [print(f"{i} - {book}") for i, book in enumerate(search_books, start=1)]
            user_coise = UserInterface.book_interface()
            if user_coise != "3":
                try:
                    select_book = search_books[int(input("Выберите книгу по ее индексу:\n")) - 1]
                    if user_coise == "1":
                        print(select_book.get_all_information())
                    else:
                        db_manager.delete_book(select_book.title)
                except IndexError:
                    print("Указан неверный индекс.")
        elif user_input == "4":
            all_books = [book for book in get_books(db_manager.get_all_books())]
            [print(f"{i} - {book}") for i, book in enumerate(all_books, start=1)]
            user_coise = UserInterface.book_interface()
            if user_coise != "3":
                try:
                    select_book = all_books[int(input("Выберите книгу по ее индексу:\n")) - 1]
                    if user_coise == "1":
                        print(select_book.get_all_information())
                    else:
                        db_manager.delete_book(select_book.title)
                except IndexError:
                    print("Указан неверный индекс.")
        elif user_input == "5":
            break


if __name__ == "__main__":
    main()
