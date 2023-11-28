import psycopg2


class DBManager:

    def __init__(self, db_host: str, db_name: str, db_user: str, db_password: str):
        """
        Конструктор класса.
        :param db_host: Хост базы данных.
        :param db_name: Имя базы данных.
        :param db_user: Имя пользователя базы данных.
        :param db_password: Пароль пользователя базы данных.
        """

        self.db_host = db_host
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password

    def get_connection(self) -> psycopg2.connect:
        """
        Устанавливает соединение с базой данных
        :return: Объект соединения с базой данных.
        """

        connection = psycopg2.connect(
            host=self.db_host,
            database=self.db_name,
            user=self.db_user,
            password=self.db_password
        )
        return connection

    def execute_query(self, query: str, data=None) -> None:
        """
        Выполняет SQL-запрос к базе данных.
        :param query: SQL-запрос.
        :param data: данные для ввода в БД
        :return: None
        """

        connection = self.get_connection()
        cursor = connection.cursor()
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()

    def create_database(self) -> None:
        """
        Создает БД если она не существует.
        :return: None
        """
        try:
            connection = psycopg2.connect(host=self.db_host, user=self.db_user, password=self.db_password)
            connection.autocommit = True
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE {self.db_name}")
        except psycopg2.Error as e:
            pass

    def create_tables(self) -> None:
        """
        Создает таблицы в базе данных, если они не существуют.
        :return: None
        """

        create_table_query = """
                CREATE TABLE IF NOT EXISTS genres (genre_name VARCHAR(255) UNIQUE);
    
                CREATE TABLE IF NOT EXISTS books (
                    book_id SERIAL PRIMARY KEY,
                    book_title VARCHAR(255) UNIQUE,
                    book_author VARCHAR(255),
                    book_description VARCHAR(255),
                    genre_name VARCHAR(255) REFERENCES genres(genre_name)
                );"""
        self.execute_query(create_table_query)

    def insert_new_genre(self, genre: list) -> None:
        """"
        Добавляет новый жанр введенный пользователем
        :param genre: Жанр введенный пользователем.
        :return: None
        """

        insert_genre_query = f"INSERT INTO genres (genre_name) VALUES (%s)"
        print(genre, type(genre))
        self.execute_query(insert_genre_query, genre)

    def insert_new_book(self, data) -> None:
        """
        Добавляет новую книгу в базу данных.
        :param data: Данные книги
        :return: None
        """

        symbols = ", ".join(["%s"] * len(data))
        keys = "book_title, book_author, book_description, genre_name"
        insert_book_query = f"INSERT INTO books ({keys}) VALUES ({symbols})"
        print(insert_book_query)
        self.execute_query(insert_book_query, data)

    def search_by_name(self, keyword):
        """
        Выполняет поиск по ключевой фразе в базе данных.
        :param keyword: ключевая фраза.
        :return: список книг найденных по ключевой фразе.
        """

        with self.get_connection() as connection, connection.cursor() as cursor:
            kyyword_search_query = f"SELECT * FROM books WHERE book_title LIKE LOWER('{keyword}')"
            cursor.execute(kyyword_search_query)
            search_result = cursor.fetchall()
            return search_result

    def search_by_genre(self, genre):
        """
        Выполняет поиск по ключевой фразе в базе дынных.
        :param genre: жанр для поиска.
        :return: список книг с указанным жанром.
        """

        with self.get_connection() as connection, connection.cursor() as cursor:
            genre_search_query = f"SELECT * FROM books WHERE genre_name LIKE LOWER('{genre}')"
            cursor.execute(genre_search_query)
            search_result = cursor.fetchall()
            return search_result

    def get_all_books(self):
        """
        Выводит все книги из базы данных.
        :return: список всех книг.
        """

        with self.get_connection() as connection, connection.cursor() as cursor:
            query = "SELECT * FROM books"
            cursor.execute(query)
            all_books = cursor.fetchall()
            return all_books

    def get_all_genres(self):
        """
        Получение всех жанров из базы данных.
        :return: Список всех жанров
        """

        with self.get_connection() as connection, connection.cursor() as cursor:
            query = "SELECT * FROM genres"
            cursor.execute(query)
            all_genres = cursor.fetchall()
            return all_genres

    def delete_book(self, book_title):
        """
        Удаление книги из базы данных
        :param book_title: Название книги
        :return: None
        """

        with self.get_connection() as connection, connection.cursor() as cursor:
            delete_book_query = f"DELETE FROM books WHERE book_title LIKE ('{book_title}')"
            print(delete_book_query)
            cursor.execute(delete_book_query)

    def test(self, data):
        query = f"INSERT INTO genres (genre_name) VALUES (%s)"
        self.execute_query(query, data)
