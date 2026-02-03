from pages.home_page import HomePage
from pages.results_page import ResultsPage


def test_search_book_by_title(page):
    home = HomePage(page)
    results = ResultsPage(page)

    home.open()
    home.search("Harry Potter")

    results.wait_for_results()
    assert results.results_count() > 0 


def test_search_with_no_results(page):
    home = HomePage(page)
    results = ResultsPage(page)

    home.open()
    home.search("asdasdasdqweqwe")

    assert results.results_count() == 0
    