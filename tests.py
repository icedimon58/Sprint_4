import pytest
from data import books
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
    @pytest.mark.parametrize('film,genre', books)
    def test_add_new_book_get_genre(self, film, genre):
        collector = BooksCollector()
        collector.add_new_book(film)
        collector.set_book_genre(film, genre)
        assert collector.get_book_genre(film) == genre

    def test_add_new_book_name_more_40_result_0(self):
        collector = BooksCollector()
        collector.add_new_book('Книги с таким названием не существует,это для проверки')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_name_is_0_result_0(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    def test_get_books_for_children_result_3(self, Set_books_collection):
        assert len(Set_books_collection.get_books_for_children()) == 3

    def test_get_books_with_specific_genre_return_result_2(self, Set_books_collection):
        assert len(Set_books_collection.get_books_with_specific_genre('Детективы')) == 2

    def test_get_books_genre_return_result_true(self, Set_books_collection):
        assert Set_books_collection.get_book_genre('Пила') == 'Ужасы'

    def test_add_book_in_favorites_result_true(self, Set_books_collection):
        count1 = len(Set_books_collection.get_list_of_favorites_books())
        Set_books_collection.add_book_in_favorites('Пила')
        Set_books_collection.add_book_in_favorites('Чужой')
        count2 = len(Set_books_collection.get_list_of_favorites_books())
        assert count2 > count1

    def test_delete_book_from_favorites_result_true(self, Del_favorite):
        count1 = len(Del_favorite.get_list_of_favorites_books())
        Del_favorite.delete_book_from_favorites('Пила')
        count2 = len(Del_favorite.get_list_of_favorites_books())
        assert count2 < count1

    def test_get_list_of_favorites_books_result_true(self, Set_books_collection):
        Set_books_collection.add_book_in_favorites('Пила')
        assert Set_books_collection.get_list_of_favorites_books() == ['Пила']

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Пила')
        collector.set_book_genre('Пила', 'Ужасы')
        assert collector.get_book_genre('Пила') == 'Ужасы'
