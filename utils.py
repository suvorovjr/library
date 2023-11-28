from library import Book


def get_books(books):
    all_books = []
    for book_item in books:
        book_id = book_item[0]
        book_title = book_item[1]
        book_author = book_item[2]
        book_description = book_item[3]
        book_genre = book_item[4]
        book = Book(book_id, book_title, book_author, book_description, book_genre)
        all_books.append(book)
    return all_books
