class UserInterface:

    @staticmethod
    def main_menu():
        """
        Функция отображения главного меню
        :return: выбор пользователя
        """

        while True:
            print("Вы в главном меню. Выберите дейтсвие:")
            print("1 - Добавить новую книгу")
            print("2 - Поиск книги по ключевому слову")
            print("3 - Поиск книги по жанру")
            print("4 - Показать все книги в библиотеке")
            user_input = input('5 - Выход из приложения\n')
            if user_input in ["1", "2", "3", "4"]:
                return user_input
            else:
                print("Ввод неверный. Укажите валидный номер.")

    @staticmethod
    def add_new_book(genres):
        """
        Функция пользовательского интерфейса для добавление новой книги.
        :param genres: список жанров
        :return: Данные новой книги.
        """

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
                    [print(f"{i + 1} - {genre}") for i, genre in enumerate(genres)]
                    genre_choice = int(input())
                    if 0 < genre_choice <= len(genres):
                        genre = genres[genre_choice - 1]
                        return title, author, description, genre, user_choice
                    else:
                        print("Ввод неверный. Укажите валидный номер.")
            elif user_choice == "2":
                genre = input("Введите свой жанр\n")
                return title, author, description, genre, user_choice
            else:
                print("Ввод неверный. Укажите валидный номер.")
