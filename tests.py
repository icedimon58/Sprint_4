import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    @pytest.mark.skip(reason="Метод отсутсвует в классе BooksCollector")
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('film,genre',[['Терминатор', 'Ужасы'],['Шерлок Холмс', 'Детективы']])
    def test_add_new_book_get_genre(self,film,genre):
        collector = BooksCollector()
        collector.add_new_book(film)
        collector.set_book_genre(film, genre)
        assert collector.get_book_genre(film)==genre

# collector = BooksCollector()
# collector.add_new_book('Терминатор')
# collector.set_book_genre('Терминатор', 'Ужасы')
# print(collector.get_book_genre('Терминатор'))