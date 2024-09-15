import pytest
from data import books
from main import BooksCollector


@pytest.fixture()
def Set_books_collection():
    collector = BooksCollector()
    for i in books:
        collector.add_new_book(i[0])
        collector.set_book_genre(i[0], i[1])
    return collector


@pytest.fixture()
def Del_favorite():
    collector = BooksCollector()
    for i in books:
        collector.add_new_book(i[0])
        collector.set_book_genre(i[0], i[1])
    collector.add_book_in_favorites('Пила')
    collector.add_book_in_favorites('Чужой')
    collector.add_book_in_favorites('Илизиюм')
    return collector
